import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

html_1 = """
<div style="background-color:#32C021;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


df=pd.read_csv("./data/TH.csv")
st.subheader("ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย")
st.write(df.head(10))

st.subheader("สถิติ")
st.write('ผลรวม')
cl4=st.columns(1)
cl4.write(dt['petal.width'].sum())

