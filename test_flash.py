import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Hello")
    print(response.text)
except Exception as e:
    print("ERROR:")
    print(e)