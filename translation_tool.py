import requests

def translate_text(text, source_language, target_language):
    url = "https://libretranslate.com/translate"

    data = {
        "q": text,
        "source": source_language,
        "target": target_language,
        "format": "text"
    }

    try:
        response = requests.post(url, data=data)

        if response.status_code == 200:
            result = response.json()
            return result["translatedText"]
        else:
            return "Translation service is currently unavailable."

    except Exception as e:
        return "Error: " + str(e)


print("===================================")
print("       LANGUAGE TRANSLATION TOOL")
print("===================================")

text = input("Enter text: ")

print("\nSupported examples:")
print("en = English")
print("hi = Hindi")
print("fr = French")
print("es = Spanish")
print("de = German")

source = input("\nEnter source language code: ")
target = input("Enter target language code: ")

translated = translate_text(text, source, target)

print("\nOriginal Text:")
print(text)

print("\nTranslated Text:")
print(translated)