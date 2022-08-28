import streamlit as st
import os

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

st.title("Volleyball")
vball_pics = st.expander("Pics")
for f in os.listdir("images/vball"):
	vball_pics.image(f"images/vball/{f}", use_column_width=True)

st.title("Games")
games_pics = st.expander("Pics")
for f in os.listdir("images/games"):
	games_pics.image(f"images/games/{f}", width=100)

st.title("Traveling")
travel_pics = st.expander("Pics")
for f in os.listdir("images/travel"):
	travel_pics.image(f"images/travel/{f}", use_column_width=True)