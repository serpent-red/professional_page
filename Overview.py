import streamlit as st

st.set_page_config(
	page_title="Portfolio", 
	page_icon="🗂", 
	layout="centered", 
	initial_sidebar_state="auto", 
	menu_items=None
)

st.title("Jacob Leisey-Bartsch's Portfolio")

st.markdown(
	"Welcome to my portfolio page! To get started, please use the navigation " +\
	"in the sidebar to the left side of this page. You can find my LinkedIn " +\
	"profile [here](https://www.linkedin.com/in/jacob-leisey-bartsch/) and my " +\
	"Github repositories, including the one powering this site, " +\
	"[here](https://github.com/serpent-red) (note that I'm in the process of " +\
	"making more of my repos public, but most of them are private for now)."
)

st.image("images/dog.gif", use_container_width=True)