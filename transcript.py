import openai
import os
import base64
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.getenv("OPENAI_KEY") 

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "img/letter_lotte.png"  # oder .jpg etc.
base64_image = encode_image(image_path)

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Du bist ein hilfreicher Assistent, der Handschrift transkribiert."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Bitte transkribiere den handschriftlichen Text in diesem Bild so genau wie möglich."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=2000
)

print("\n📝 Transkription des Bildes:\n")
print(response['choices'][0]['message']['content'])