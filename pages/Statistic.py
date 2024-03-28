import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import pandas as pd

# กำหนด URL ของ Lottie animation
lottie_url = "https://assets.lottiefiles.com/packages/lf20_jkgb4v7h.json"

# โหลด Lottie animation
lottie_animation = load_lottieurl(lottie_url)

# โหลดข้อมูล CSV
df = pd.read_csv("./data/TH.csv")

# แสดงหัวข้อ
st.title("ดัชนีสมรรถนะสิ่งแวดล้อมของประเทศไทย")

# แสดง Lottie animation
st_lottie(lottie_animation, key="lottie")

# แสดงข้อมูล
st.write(df.head(10))

# แสดงสถิติ
# หาปีที่มีคะแนนสูงสุดสำหรับแต่ละคอลัมน์
max_years = {}
for col in df.columns[2:]:
    max_years[col] = df[col].argmax() + 2565

# แสดงผลลัพธ์
st.subheader("สถิติ")
for col, year in max_years.items():
    st.write(f"{col}: {year}")
