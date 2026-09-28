import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from llm_call import LLMCall
from watermark import Watermark


load_dotenv()

app = Flask(__name__)
watermark = Watermark()


def _request_json():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, (jsonify(error="Request body must be a JSON object"), 400)
    return payload, None


@app.post("/api/generate")
def generate_text():
    payload, error = _request_json()
    if error:
        return error

    prompt = payload.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify(error="prompt must be a non-empty string"), 400

    api_key = os.getenv("API_KEY")
    if not api_key:
        return jsonify(error="AI service is not configured"), 503

    try:
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        response = LLMCall(model_name, api_key).call_gemini(prompt.strip())
        generated_text = response.text
        if not generated_text:
            return jsonify(error="AI service returned no text"), 502
    except Exception:
        app.logger.exception("AI generation failed")
        return jsonify(error="AI generation failed"), 502

    return jsonify(
        prompt=prompt,
        text=watermark.add_watermark(generated_text),
        watermarked=True,
    )


@app.post("/api/detect")
def detect_text():
    payload, error = _request_json()
    if error:
        return error

    text = payload.get("text")
    if not isinstance(text, str):
        return jsonify(error="text must be a string"), 400

    return jsonify(
        watermarked=watermark.detect_watermark(text),
        zero_width=watermark.detect_zerowidth_watermark(text),
        homoglyph=watermark.detect_homoglyph_watermark(text),
    )


@app.get("/api/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))