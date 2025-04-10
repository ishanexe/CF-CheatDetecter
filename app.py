import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Codeforces Cheater Detector", layout="centered")
st.title("🚨 Codeforces Cheater Detector")

st.markdown("""
<style>
    .reportview-container {
        background: #f5f7fa;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

username = st.text_input("👤 Enter Codeforces Username:")

if st.button("🔍 Check Submissions"):
    if not username:
        st.warning("Please enter a username.")
    else:
        with st.spinner("Fetching submissions from Codeforces..."):
            url = f"https://codeforces.com/api/user.status?handle={username}&from=1&count=10000"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                submissions = data.get("result", [])

                skipped_count = sum(1 for sub in submissions if sub.get("verdict") == "SKIPPED")
                accepted_count = sum(1 for sub in submissions if sub.get("verdict") == "OK")
                total = len(submissions)

                cheat_probability = (skipped_count / total) * 100 if total > 0 else 0

                labels = ['Accepted', 'Skipped', 'Others']
                others_count = total - accepted_count - skipped_count
                values = [accepted_count, skipped_count, others_count]
                colors = ['#28a745', '#dc3545', '#ffc107']

                st.subheader("📊 Submission Statistics")
                fig, ax = plt.subplots()
                ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
                ax.axis('equal')
                st.pyplot(fig)

                st.subheader("📉 Cheat Probability")
                st.info(f"User {username} has a {cheat_probability:.2f}% probability of being a cheater.")

                if skipped_count > 0:
                    st.error(f"❌ Verdict: User {username} is likely a CHEATER!")
                else:
                    st.success(f"✅ Verdict: User {username} is a LEGIT USER!")

            else:
                st.error("Failed to fetch data. Please check the username and try again.")
