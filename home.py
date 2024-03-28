import streamlit as st

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/Statistic.py", label="การทำนายข้อมูลด้วยสถิติ, icon="1️⃣")
st.page_link("pages/Chart.py", label="การทำนายข้อมูลด้วยเทคนิค Naive Baye", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")