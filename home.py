import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd
import matplotlib.pyplot as plt

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/58b420f5-455d-4ff0-a50a-b24a54208bf7/mC47twAfec.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")


st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/Statistic.py", label="การทำนายข้อมูลด้วยสถิติ",icon="1️⃣")
st.page_link("pages/Chart.py", label="การนำเสนอ", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")

df=pd.read_csv("./data/TH.csv")
st.subheader("ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย")
st.write(df.head(10))

# เลือกคอลัมน์ที่ต้องการแสดง
df_plot = df[['ปี', 'ค่าดัชนี', 'ค่าเฉลี่ย', 'ค่าสูงสุด']]

# กำหนดจำนวนแถวและคอลัมน์ของกราฟ
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

# วาดกราฟ
for i, ax in enumerate(axes.flatten()):
    ax.plot(df_plot['ปี'], df_plot.iloc[:, i+1])
    ax.set_title(df_plot.columns[i+1])

# ปรับแต่งกราฟ
plt.tight_layout()
plt.show()