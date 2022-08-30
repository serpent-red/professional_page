import streamlit as st

st.set_page_config(
	page_title="Portfolio", 
	page_icon="🗂", 
	layout="centered", 
	initial_sidebar_state="auto", 
	menu_items=None
)

st.info(
	"Due to the confidential/proprietary nature of many of these projects, I " +\
	"am unable to share code from these projects. However, I do discuss " +\
	"these projects at a high level and provide some details about tools and " +\
	"methods used."
)

st.header("Newton IM")
nim_exp = st.expander("Projects")
nim_exp.subheader("Dashboarding")
nim_exp.write(
	"Led internal research into state-of-the-art dashboarding technologies, " +\
	"presented findings to senior management, and ultimately convinced them " +\
	"to transition away from Dash and adopt Streamlit instead."
)

nim_exp.subheader("Dockerization")
nim_exp.write(
	"Containerized our python applications to support the proper testing " +\
	"of applications prior to deployments, which led to a significant decrease " +\
	"in the number of required redeployments. Additionally, I assembled a set of " +\
	"Dockerfiles that allowed the test environments to access hard-to-reach " +\
	"internal package repositories."
)


st.header("VISIMO")
vis_exp = st.expander("Projects")
vis_exp.subheader("Agility Prime")
vis_exp.write(
	"This project used Object Recognition algorithms on videos captured " +\
	"from drones to detect potential points of collision (such as other " +\
	"aircraft, trees, and buildings). We then provided users with a dashboard " +\
	"where they could upload and run detection on their own drone footage."
)

vis_exp.subheader("NIXN")
vis_exp.write(
	"We created a multi-page web application that allowed construction " +\
	"safety specialists to record workplace safety violations. Additionally, " +\
	"this application assisted the specialists by recommending remedial " +\
	"actions that would be most effective in reducing the risk caused by the " +\
	"initial violation. Moreover, administrative end users were provided with " +\
	"a portal where they could add/edit/remove violations and remedies from " +\
	"the website, so they could take primary ownership of the website's content."
)
vis_exp.subheader("Budgeting Application")
vis_exp.write(
	"We created a multi-page web application that allowed for the budgeting " +\
	"of clinical trials. Moreover, administrative end users were provided with " +\
	"a portal where they could add/edit/remove budgets items and clinical trials " +\
	"from the website, so they could take primary ownership of the website's " +\
	"content. One of the highlights of this application is that it allowed our " +\
	"client to fully adopt versioning, as the application automatically tracked " +\
	"changes to the budgets and stored all historical versions for easy recall."
)

vis_exp.subheader("Virtual Waiting Room")
vis_exp.write(
	"We created a multi-page web application that allowed doctor's offices " +\
	"to utilize a virtual waiting room. This was implemented at the height " +\
	"of the pandemic and allowed these offices to minimize unneccessary direct " +\
	"contact between patients. As part of this site, we built an in-house " +\
	"instant messaging system that could be accessed through the web portal. " +\
	"Additionally, we implemented an automated SMS system for any patient " +\
	"that opted into receiving text messages. Moreover, administrative end " +\
	"users were provided with a portal where they could add/edit/remove " +\
	"patient data from the website, so they could take primary ownership of " +\
	"the website's content."
)


st.header("SAP Ariba")
sap_exp = st.expander("Projects")
sap_exp.subheader("Demand Forecasting")
sap_exp.write(
	"Used a variety of time series algorithms, including temporal regression, " +\
	"ARIMA, and vector autoregression, to improve demand forecasting. In " +\
	"addition to coding the models, I also conducted testing and validation using" +\
	"a rolling horizon."
)


st.header("Mylan")
myl_exp = st.expander("Projects")
myl_exp.subheader("International Sales Markets")
myl_exp.write(
	"Worked as part of an intern team that conducted research on high " +\
	"potential international markets to enter. As part of this project, we " +\
	"found external demographic data, combined it with internal sales data, " +\
	"performed dimension reduction, and fit a regression model to the data. " +\
	"After all analysis had been completed, we presented our findings to the " +\
	"intern team leads and additional management."
)
