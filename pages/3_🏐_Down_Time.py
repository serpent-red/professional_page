import streamlit as st
import os

st.set_page_config(
	page_title="Portfolio", 
	page_icon="🗂", 
	layout="centered", 
	initial_sidebar_state="auto", 
	menu_items=None
)

st.title("Volleyball")
st.markdown(
	"I have been an avid volleyball player since middle school and have been " +\
	"consistently playing the sport for the last 15 years. This includes " +\
	"everything from pickup games to national tournaments. However, the most " +\
	"enjoyable playtime since moving to Pittsburgh comes from playing in the " +\
	"[Steel City Volleyball League](https://www.steelcityvolleyball.org/)."
)
vball_pics = st.expander("Pics")
for f in os.listdir("images/vball"):
	vball_pics.image(f"images/vball/{f}", use_column_width=True)

st.title("Games")
st.write(
	"On the lighter side of my leisure activities is playing all kinds of games, " +\
	"including board games, card games, and video games. I've included a few of " +\
	"my favorites below!"
)
games_pics = st.expander("Pics")
for f in os.listdir("images/games"):
	games_pics.image(f"images/games/{f}", use_column_width=True)

st.title("Roadtrips")
st.write(
	"Having been homeschooled, I ended up doing a lot of school work in the car " +\
	"while traveling as I was growing up. My mom and I regularly did roadtrips " +\
	"around the eastern US and infrequently flew everywhere around the country. " +\
	"While flying is fun, the roadtrips were truly magical and as I have " +\
	"gotten older, my love of roadtrips continues to grow!"
)
travel_pics = st.expander("Pics")
for f in os.listdir("images/travel"):
	travel_pics.subheader(f.replace(".csv", "").replace("_", " "))
	travel_pics.image(f"images/travel/{f}", use_column_width=True)