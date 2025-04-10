import streamlit as st
import requests

st.set_page_config(page_title="Codeforces Cheat Detector", layout="centered")
st.title("🕵️‍♂️ Codeforces Cheat Detector")

username = st.text_input("Enter Codeforces Username")

if st.button("Check for Cheating"):
    if not username:
        st.warning("Please enter a username.")
    else:
        with st.spinner("Checking submissions..."):
            url = f"https://codeforces.com/api/user.status?handle={username}"
            try:
                response = requests.get(url)
                data = response.json()

                if data["status"] != "OK":
                    st.error("❌ Invalid username or error fetching data.")
                else:
                    verdicts = [sub.get("verdict") for sub in data["result"]]
                    skipped_count = verdicts.count("SKIPPED")

                    if skipped_count > 0:
                        st.error(f"❌ {username} may be cheating ({skipped_count} skipped submissions found).")
                    else:
                        st.success(f"✅ {username} appears to be clean! No skipped verdicts found.")
            except Exception as e:
                st.error(f"Error: {e}")
