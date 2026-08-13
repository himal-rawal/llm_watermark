from google import genai
from llm_call import LLMCall
from dotenv import load_dotenv
import os
def main():
    load_dotenv()  
    model_name = "gemini-2.5-flash"  
    api_key =  os.getenv("API_KEY") 
    print(f"Using API Key: {api_key}")
    llm_call = LLMCall(model_name, api_key)
    prompt = "Say Himal"
    response = llm_call.call_gemini(prompt)
    print(response.text)   
main()