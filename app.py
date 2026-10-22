import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Malam yang Tak Ingin Kulupa", layout="centered")

with open("foto.jpg", "rb") as f:
    foto = base64.b64encode(f.read()).decode()

with open("index.html", encoding="utf-8") as f:
    html = f.read().replace("foto.jpg", f"data:image/jpeg;base64,{foto}")

components.html(html, height=1100, scrolling=True)