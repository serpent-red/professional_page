import streamlit as st

st.set_page_config(
	page_title="Portfolio", 
	page_icon="🗂", 
	layout="centered", 
	initial_sidebar_state="auto", 
	menu_items=None
)

st.info(
	"🛠 This section is currently under construction and is actively being " +\
	"built out and completed."
)

st.header("Streetview Predictor")

st.header("Discord Bots")

st.header("Portfolio Dashboard")
src1_exp = st.expander("Source Code for this Page")

with open('pages/2_💻_Personal_Projects.py', 'r') as file:
    data = file.read()
    src1_exp.code(data, language="python")