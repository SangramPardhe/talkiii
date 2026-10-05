# ===========================================
# Gemini AI Setup
# ===========================================

from google import genai

client = genai.Client(api_key="insert api key here")

def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are Talkii.

You are a Windows AI voice assistant.

Rules:
- Always answer like a real assistant.
- Keep answers under 70 words.
- Speak naturally.
- Never use markdown.
- Never use bullet points.
- Never use code fences unless asked.
- If asked to write code, provide only the code.
- If asked casual questions, respond conversationally.
- Finish every answer naturally.

User:
{prompt}

Talkii:
"""
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"





