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
st.write(
	"This project is an image classifier built in python's Tensorflow " +\
	"library. This classifier could take a google streetview image " +\
	"as an input and predict the country of origin with about 20% " +\
	"accuracy. I was inspired to start this project when the " +\
	"[GeoGuessr](https://www.geoguessr.com/) trend started towards " +\
	"the beginning of the pandemic."
)

st.header("Discord Bots")
st.write(
	"This project contains a variety of python bots that are housed " +\
	"in multiple discord servers that I have set up and maintain. " +\
	"Some of these bots provide utility (data collection and recall), " +\
	"while others are simply there for amusement (sending funny messages)." 
)

st.header("Portfolio Dashboard")
src1_exp = st.expander("Source Code for this Page")

with open('pages/2_💻_Personal_Projects.py', 'r') as file:
    data = file.read()
    src1_exp.code(data, language="python")