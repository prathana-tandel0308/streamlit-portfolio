# app.py
import streamlit as st

st.set_page_config(page_title="👩‍💻 Your Name | Portfolio", layout="wide")

# Header
st.title("👋 Hello, I'm Prathana Tandel!")
st.subheader("Final Year CSE Student | Web Dev | AI/ML | Arduino Projects")

# About Section
st.markdown("## 📌 About Me")
st.write("""
I'm a Computer Science student passionate about AI/ML, Web Development, and Embedded Systems.  
I have experience with Streamlit, Arduino, OpenCV, Python, PHP, and SAP S/4HANA.
""")

# Projects Section
st.markdown("## 🚀 Projects")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧠 Driver Drowsiness Detection")
    st.write("Real-time face and eye monitoring using Python + OpenCV + Arduino.")
    st.markdown("[View Code](https://github.com/yourusername/project1)")

    st.markdown("### 🌿 CropDoctor: Plant Disease Detector")
    st.write("AI-powered disease classification using CNN + Streamlit app.")
    st.markdown("[Demo](https://your-cropdoctor-app.streamlit.app)")

with col2:
    st.markdown("### 🛒 E-commerce Website (PHP)")
    st.write("Dynamic website with login, cart, wishlist, and admin dashboard.")
    st.markdown("[GitHub](https://github.com/yourusername/shopzone)")

    st.markdown("### 🤖 AI Anomaly Detection")
    st.write("Built with Teachable Machine + Streamlit + Live Camera Interface.")
    st.markdown("[Try It](https://your-anomaly-app.streamlit.app)")

# Contact Section
st.markdown("## 📬 Contact Me")
st.write("""
- 📧 Email: your.email@example.com  
- 🔗 [LinkedIn](https://linkedin.com/in/yourusername)  
- 🐱 [GitHub](https://github.com/yourusername)
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Prathana Tandel")
