# Knowledge Management System (KMS)

A web-based KMS built with Flask and Hugging Face's Inference API (`distilgpt2`).

## Setup
1. Clone the repo: `git clone https://github.com/your-username/kms_project.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with `HF_API_TOKEN=your-hugging-face-token`
4. Run: `python app.py`
5. Visit: `http://127.0.0.1:5000`

## Features
- Query a local knowledge base.
- Generate responses using `distilgpt2`.

## Notes
- Replace `HF_API_TOKEN` with your own from [huggingface.co](https://huggingface.co).
