check out the website:https://cf-cheatdetecter-qm3hjphixjvwabd9z8v6qg.streamlit.app/
# 🚨 Codeforces Cheater Detector

A fun tool to visualize whether a Codeforces user might be involved in cheating based on skipped submissions.

## 🔍 How it works
- Enter a Codeforces username.
- The app fetches all submissions from the official Codeforces API.
- If any submission is marked as `SKIPPED`, the user is considered **suspicious**.
- A pie chart shows Accepted, Skipped, and Other submissions.
- A simple cheat probability score is displayed.

## 📦 Features
- Uses official Codeforces API
- Stylish Streamlit web interface
- Visual stats with `matplotlib`
- Cheat probability calculator

## 🧠 Tech Stack
- Python
- Streamlit
- Matplotlib
- Requests

## 🚀 How to Run
```bash
pip install streamlit requests matplotlib
streamlit run app.py
