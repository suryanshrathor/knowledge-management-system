from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize the OpenAI client with your API key
# Replace with your actual key
client = OpenAI(api_key="your_api_key")

# Path to your knowledge base folder
KNOWLEDGE_BASE_DIR = "knowledge_base"

# Function to load knowledge base files


def load_knowledge_base():
    knowledge = {}
    for filename in os.listdir(KNOWLEDGE_BASE_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(KNOWLEDGE_BASE_DIR, filename), "r", encoding="utf-8") as file:
                knowledge[filename] = file.read()
    return knowledge

# Function to search knowledge base for relevant content


def search_knowledge_base(query, knowledge_base):
    relevant_content = ""
    for filename, content in knowledge_base.items():
        if query.lower() in content.lower():  # Basic keyword matching
            relevant_content += f"\n\nFrom {filename}:\n{content}"
    return relevant_content if relevant_content else "No specific info found in the knowledge base."

# Route for the homepage


@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chatbot queries


@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')
    knowledge_base = load_knowledge_base()

    # Search knowledge base for relevant info
    context = search_knowledge_base(user_query, knowledge_base)

    # Construct prompt for ChatGPT
    prompt = f"User query: {user_query}\n\nKnowledge base context: {context}\n\nProvide a helpful response based on the query and context."

    # Call OpenAI API using the new client interface
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful knowledge management assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )

    answer = response.choices[0].message.content.strip()
    return jsonify({'response': answer})


if __name__ == '__main__':
    app.run(debug=True)
