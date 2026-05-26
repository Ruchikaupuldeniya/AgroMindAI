# AgroMindAI 🚜

A Flask web app that predicts crop yields based on soil and weather parameters.

## Live Demo

https://agromindai.onrender.com  <!-- Replace with your actual Render URL after deployment -->

## Installation (local)

```bash
pip install -r requirements.txt
python app.py
```

## Deploy to Render (already configured)

1. Create a **Web Service** in Render.
2. Connect the `AgroMindAI` GitHub repo.
3. Use the following settings:
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free
4. Click **Create Web Service** and wait for the deployment.

---

*Free Render services may sleep after inactivity; the first request may take 30‑60 seconds.*
