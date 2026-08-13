from google import genai
class LLMCall:
    def __init__(self,model_name,api_key):
        self.model_name = model_name
        self.api_key = api_key
        self.client = genai.Client(api_key=self.api_key)

    def call_gemini(self,prompt):
        response = self.client.models.generate_content(
            model=self.model_name,
            contents={'text': prompt},
            config={
                'temperature': 0,
                'top_p': 0.95,
                'top_k': 20,
            },
        )
        return response