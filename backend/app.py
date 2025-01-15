from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/generate", methods=["POST"])
def generate_component():
    try:
        # Get user query from request
        data = request.json
        user_query = data.get("query", "")

        # Chat messages for the assistant
        messages = [
            {"role": "system", "content": "You are an assistant that generates React components based on user requests."},
            {"role": "user", "content": f"Generate a React component for: {user_query}"}
        ]

        # Use ChatCompletion API with the latest models
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if needed
            messages=messages,
            max_tokens=200
        )

        # Extract the generated component code
        component_code = response.choices[0].message.content.strip()
        return jsonify({"componentCode": component_code})

    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

