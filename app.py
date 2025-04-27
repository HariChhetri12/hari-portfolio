import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --- Page Configuration ---
st.set_page_config(page_title="Hari Chhetri | Portfolio", page_icon="😎", layout="centered")

# --- Custom CSS for Background and Font ---
st.markdown("""
    <style>
    /* Background color */
    body {
        background-color: #f9f9f9;
    }
    /* Font and Center Text */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    /* Title Styling */
    .css-10trblm {
        font-size: 48px;
        font-weight: bold;
        color: #4A90E2;
    }
    h1, h2, h3 {
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Function to Load Lottie Animation ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Assets ---
profile_image = Image.open(r"C:\Users\Chhet\OneDrive\Desktop\photo\H.C12.JPG")

# Fun waving astronaut animation
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t24tpvcu.json")

# --- Main Section (Hero Section) ---
col1, col2 = st.columns(2)

with col1:
    st.image(profile_image, width=220)

with col2:
    st.title("Hari Chhetri 😎")
    st.subheader("CEO | Trader | Lifelong Learner")
    st.write("Welcome to my digital world where passion meets innovation!")

# --- Animation below ---
st_lottie(lottie_animation, height=300, key="hello-astronaut")

st.write("---")

# --- About Me Section ---
st.header("📖 About Me")
st.write("""
Hi, I'm **Hari Chhetri**, passionate about trading, technology, and entrepreneurship.  
Founder and CEO of **H.C12 Company**.  
I believe in lifelong learning, innovation, and building solutions that make an impact.
""")

# --- Skills Section ---
st.header("🧠 Skills")
st.markdown("""
- 💻 **Python Programming**
- 📊 **Data Analysis & Business Intelligence**
- 🌐 **Web Development**: Streamlit
- 🎵 **Music Production**: FL Studio 21
- 🛠️ **Tools**: Wallet App, VS Code, GitHub
""")

# --- Experience Section ---
st.header("💼 Experience")
st.write("""
**Founder & CEO — H.C12 Company (2025 - Present)**  
- Leading innovation in trading and business solutions.
- Managing teams, technology development, and strategic decisions.

**Student — [Your College Name] (2025 - Present)**  
- Pursuing Bachelor's Degree while building my business career.
""")

# --- Education Section ---
st.header("🎓 Education")
st.write("""
**Bachelor's Degree (Ongoing)**  
[Your Major] — [Your College Name]  
Expected Graduation: 202*
""")

# --- Contact Section ---
st.header("📫 Contact Me")
st.markdown("""
- 📧 Email: [harichhetri.hc12@gmail.com](mailto:harichhetri.hc12@gmail.com)
- 📞 Phone: 17794981
- 🏢 CEO at **H.C12 Company**
""")

# --- Footer ---
st.write("---")
st.caption("Made with ❤️ by Hari Chhetri • Powered by Streamlit • © 2025")
