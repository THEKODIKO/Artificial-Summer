import os
import google.generativeai as genai



apiKey= os.getenv("GEMINI_API_KEY")

genai.configure(api_key= apiKey)



model= genai.GenerativeModel("models/gemini-1.5-pro-latest")

flash_model= genai.GenerativeModel("models/gemini-1.5-flash")
image_model= genai.GenerativeModel("models/gemini-pro-vision")
image_1_0_model= genai.GenerativeModel("models/gemini-1.0-pro-vision-latest")



def ai_respond(context):
    global model
    
    try:
        resp= model.generate_content(context).text
    except:
        resp= "Sorry, but can we talk about something else?"

    return resp

