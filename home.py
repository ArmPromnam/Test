import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd
import seaborn as sns

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/58b420f5-455d-4ff0-a50a-b24a54208bf7/mC47twAfec.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")


st.page_link("home.py", label="หน้าแรก", icon="")
st.page_link("pages/Statistic.py", label="การทำนายข้อมูลด้วยสถิติ",icon="1️⃣")
st.page_link("pages/Chart.py", label="การนำเสนอ", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="")

df=pd.read_csv("./data/TH.csv")
st.subheader("ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย")
st.write(df.head(10))

# อ่านข้อมูลจากตาราง
years = []
scores = []
for row in df:
    years.append(row[1])
    scores.append(row[3])

# seaborn แทน matplotlib
sns.set_theme(style="whitegrid")

# สร้างกราฟแท่ง
sns.barplot(x=years, y=scores,palette="rocket")

# ตั้งชื่อแกน X และ Y
plt.xlabel("ปี")
plt.ylabel("คะแนน")

# เพิ่มชื่อกราฟ
plt.title("ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย")

# แสดงกราฟใน Streamlit
st.pyplot(plt)
