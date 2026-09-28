# AI Watermark API

A Flask API that generates Gemini responses, adds the project watermark, and detects that watermark.

## Setup

```bash
python3 -m pip install -r requirements.txt
export API_KEY="your-gemini-api-key"
python3 app.py
```

The server listens on `http://localhost:5000` by default. Set `GEMINI_MODEL` or `PORT` to override the defaults.

## Generate text

```bash
curl -X POST http://localhost:5000/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Explain photosynthesis in two sentences."}'
```

The response contains the watermarked generated text:

```json
{"prompt":"...","text":"...","watermarked":true}
```

## Detect a watermark

```bash
curl -X POST http://localhost:5000/api/detect \
  -H 'Content-Type: application/json' \
  -d '{"text":"text to inspect"}'
```

The response reports the overall result and the matching mechanisms:

```json
{"watermarked":true,"zero_width":true,"homoglyph":false}
```

`GET /api/health` returns `{"status":"ok"}` and does not require an AI key.
