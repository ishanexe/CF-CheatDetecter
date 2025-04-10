import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Codeforces Cheater Detector", layout="centered")
st.title("🚨 Codeforces Cheater Detector")

# 🌈 Custom Styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .stButton > button {
        background-color: #dc3545;
        color: white;
        font-weight: bold;
        border-radius: 6px;
    }
    h1 {
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

# 🔎 Form-based input (better for mobile)
with st.form("cf_form"):
    username = st.text_input("👤 Enter Codeforces Username:").strip()
    submit = st.form_submit_button("🔍 Check Submissions")

if submit:
    if not username:
        st.warning("Please enter a username.")
    else:
        with st.spinner("⏳ Fetching submissions from Codeforces..."):
            try:
                url = f"https://codeforces.com/api/user.status?handle={username}&from=1&count=10000"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    submissions = data.get("result", [])

                    skipped_count = sum(1 for sub in submissions if sub.get("verdict") == "SKIPPED")
                    accepted_count = sum(1 for sub in submissions if sub.get("verdict") == "OK")
                    total = len(submissions)
                    others_count = total - accepted_count - skipped_count

                    cheat_probability = (skipped_count / total) * 100 if total > 0 else 0

                    # 📊 Pie Chart
                    st.subheader("📊 Submission Stats (Accepted vs Skipped)")
                    fig, ax = plt.subplots()
                    ax.pie(
                        [accepted_count, skipped_count, others_count],
                        labels=['Accepted', 'Skipped', 'Others'],
                        colors=['#28a745', '#dc3545', '#ffc107'],
                        autopct='%1.1f%%',
                        startangle=140
                    )
                    ax.axis('equal')
                    st.pyplot(fig)

                    # 📉 Cheat Probability
                    st.subheader("📉 Cheat Probability")
                    st.info(f"Cheat Probability: **{cheat_probability:.2f}%**")

                    # ✅ Verdict
                    if skipped_count > 0:
                        st.error(f"❌ Verdict: User **{username}** is likely a CHEATER.")
                    else:
                        st.success(f"✅ Verdict: User **{username}** is a LEGIT USER.")
                else:
                    st.error("❌ Failed to fetch data. Please check the username and try again.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
