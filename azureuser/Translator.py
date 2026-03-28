import requests
import uuid

# ========= Azure Translator Credentials =========
KEY = "2IUBVSmofeqB6aOmVUjU56KxAzrkUuyqT7fcAEu00XyFPVVK6XrVJQQJ99CAAC3pKaRXJ3w3AAAbACOGaB3B"
ENDPOINT = "https://api.cognitive.microsofttranslator.com"
REGION = "eastasia"   # e.g. centralindia

# ========= Language Options =========
languages = {
    "1": ("Hindi", "hi"),
    "2": ("French", "fr"),
    "3": ("Spanish", "es"),
    "4": ("German", "de"),
    "5": ("Tamil", "ta")
}

print("\n--- Azure Translator ---")
print("Choose a language:")

for num, lang in languages.items():
    print(f"{num}. {lang[0]}")

choice = input("\nEnter your choice (1-5): ")

if choice not in languages:
    print("❌ Invalid choice")
    exit()

text = input("\nEnter text to translate: ")

# ========= API Request =========
path = "/translate"
params = {
    'api-version': '3.0',
    'from': 'en',
    'to': languages[choice][1]
}

headers = {
    'Ocp-Apim-Subscription-Key': KEY,
    'Ocp-Apim-Subscription-Region': REGION,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{'text': text}]

url = ENDPOINT + path

response = requests.post(url, params=params, headers=headers, json=body)

# ========= Result =========
result = response.json()
translated_text = result[0]['translations'][0]['text']

print(f"\nTranslated to {languages[choice][0]}:")
print(translated_text)