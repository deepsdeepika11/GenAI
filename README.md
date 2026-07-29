# Gemini Chat Streamlit App

This repo contains a simple Streamlit app (`app.py`) that uses Gemini (Google Generative AI).

How to deploy to Streamlit Community Cloud

1. Initialize a Git repository and push to GitHub (replace placeholders):

```bash
git init
git add .
git commit -m "Add Gemini Chat app"
# create a new GitHub repository and replace URL below
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

2. In Streamlit Community Cloud, choose "New app" and connect the GitHub repo and branch.

3. Make sure `requirements.txt` is present (this repo includes it).

Notes & troubleshooting
- If you see a model 404 or deprecation message, you may need to update `GEMINI_MODEL` in `.env` or migrate to the Interactions API.
- If you see a quota error, ensure billing is enabled for the Google Cloud project that owns the API key in `.env`.
- Do NOT commit your `.env` file with the API key to a public repo. Use Streamlit secrets or GitHub Actions to inject secrets for production.

Local run

```bash
pip install -r requirements.txt
streamlit run app.py
```
