import requests
import os

USE_LOCAL = os.getenv("USE_LOCAL", "true")


def ask_model(prompt):
    if USE_LOCAL == "true":
        return ask_ollama(prompt)
    else:
        return ask_api(prompt)


def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt},
        timeout=60
    )
    return response.json().get("response", "")


def ask_api(prompt):
    # temporary fallback (you can upgrade later)
    return "Demo mode: Model not available in cloud deployment."