import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

genai.configure(
    api_key=GEMINI_API_KEY
)


def analyze_visual_change(
        old_image,
        new_image):

    model = genai.GenerativeModel(
        GEMINI_MODEL
    )

    with open(old_image, "rb") as f:
        old_bytes = f.read()

    with open(new_image, "rb") as f:
        new_bytes = f.read()

    prompt = """
Compare these two website screenshots.

Identify:

1. Layout changes
2. Design updates
3. New sections
4. Removed sections
5. CTA changes
6. Visual positioning changes

Return a concise report.
"""

    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/png",
                "data": old_bytes
            },
            {
                "mime_type": "image/png",
                "data": new_bytes
            }
        ]
    )

    return response.text