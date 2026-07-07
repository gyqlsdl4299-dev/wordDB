import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="속초 1박 2일 여행", page_icon="🌊", layout="wide")

html = (pathlib.Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
