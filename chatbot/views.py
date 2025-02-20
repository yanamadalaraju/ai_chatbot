# from ast import Import
# from django.shortcuts import render
# import openai
# from django.http import JsonResponse
# from django.conf import settings
# import google.generativeai as genai
# import json
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

# # Configure Gemini API key
# genai.configure(api_key=settings.GEMINI_API_KEY)

# @csrf_exempt
# def chat(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             prompt = data.get("prompt", "")

#             if not prompt:
#                 return JsonResponse({"error": "Prompt is empty"}, status=400)

#             # Initialize Gemini model
#             model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" for text-based chat
#             response = model.generate_content(prompt)

#             return JsonResponse({"response": response.text})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)




# def chat_page(request):
#     return render(request, "chat.html")



# import json
# import google.generativeai as genai
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt

# genai.configure(api_key=settings.GEMINI_API_KEY)

# @csrf_exempt
# def translate_text(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             text = data.get("text", "")
#             target_language = data.get("language", "")

#             if not text or not target_language:
#                 return JsonResponse({"error": "Invalid input"}, status=400)

#             # Create translation prompt
#             prompt = f"Translate the following text into {target_language}: \n{text}"

#             # Generate translation using Gemini API
#             model = genai.GenerativeModel("gemini-pro")
#             response = model.generate_content(prompt)

#             return JsonResponse({"translated_text": response.text})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)


# def translation_page(request):
#     return render(request, "translate.html")

import google.generativeai as genai
import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")
            language = data.get("language", "English")  # Default to English

            if not prompt:
                return JsonResponse({"error": "Prompt is empty"}, status=400)

            # Generate response in English first
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            response_text = response.text

            # If language is not English, translate the response
            if language != "English":
                translation_prompt = f"Translate the following into {language}:\n{response_text}"
                translation_response = model.generate_content(translation_prompt)
                response_text = translation_response.text

            return JsonResponse({"response": response_text})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

# Serve the chat page
from django.shortcuts import render

def chat_page(request):
    return render(request, "chat.html")
