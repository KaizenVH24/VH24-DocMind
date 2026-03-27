import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(prompt, model="mistral"):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "")

    except Exception as e:
        print("Ollama error:", e)
        return None


if __name__ == "__main__":
    reply = ask_ollama("Explain AI in one line")
    print(reply)