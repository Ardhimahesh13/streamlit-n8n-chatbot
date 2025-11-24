# 🤖 n8n + Streamlit Chatbot

This is a synchronous chatbot built using Streamlit (frontend) and n8n (backend).

## 📂 Project Structure
- `app.py`: The Streamlit frontend application.
- `workflow.json`: The n8n backend workflow (Import this into n8n).
- `requirements.txt`: Python dependencies.

## 🚀 How to Run locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt

2. **Setup n8n**
- `Import workflow.json into your n8n instance.`

- `Activate the workflow.`

- `Update the N8N_WEBHOOK_URL in app.py with your production URL.`


**Run the App**
streamlit run app.py

