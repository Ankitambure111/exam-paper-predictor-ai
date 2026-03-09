import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    print("Testing connection...")
    # This model is the standard for 2026
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite", 
        contents="Hi! If you can read this, say 'System Online'."
    )
    print("✅ SUCCESS! AI says:", response.text)

except Exception as e:
    print("❌ ERROR OCCURRED:", e)
    print("\nLet's check which models you CAN use:")
    # This part helps us find the right 'menu item' if the one above is missing
    for m in client.models.list():
        print(f" - {m.name}")