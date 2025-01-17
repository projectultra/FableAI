import os
from flask import Flask, render_template, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# Set Groq API endpoint and headers (replace with your API key)
GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Story generation route
@app.route("/generate", methods=["POST"])
def generate_story():
    data = request.json
    character = data.get("character", "")
    setting = data.get("setting", "")
    theme = data.get("theme", "")

    if not character or not setting or not theme:
        return jsonify({"error": "All fields are required."}), 400

    # Generate story using Groq API
    prompt = f"Write a short story with the following details:\nCharacter: {character}\nSetting: {setting}\nTheme: {theme}\n"
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(GROQ_API_ENDPOINT, headers=HEADERS, json=payload)
        response.raise_for_status()
        story = response.json()["choices"][0]["message"]["content"]
        print(story)
        return jsonify({"story": story})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
