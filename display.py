import streamlit as st
import pandas as pd
import random
import time
from streamlit_gsheets import GSheetsConnection
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. دالة جلب البيانات
def load_data():
    try:
        # هنا نخبر البرنامج أن يأخذ الرابط "النظيف" من الـ Secrets
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # القراءة بدون تحديد الرابط هنا (لأنه موجود في Secrets)
        df = conn.read(worksheet="Form Responses 1")
        
        # التأكد من أسماء الأعمدة (الاسم أولاً ثم الكلية)
        df.columns = ["name", "major", "timestamp"]
        
        return df
    except Exception as e:
        # إذا استمر الخطأ، سيظهر لنا هنا لنعالجه
        st.sidebar.error(f"تحقق من الربط: {e}")
        return pd.DataFrame(columns=["name", "major"])
        # إذا فشل، سيظهر الخطأ هنا بشكل بسيط لنعرف مكانه

# --- (باقي كود الـ CSS والأشكال السداسية كما هو دون تغيير) ---
full_custom_style = """
<style>
    .stApp {
        background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
    }
    .bowl-v3 {
        position: relative !important;
        width: 900px !important; 
        height: 700px !important;
        border-radius: 50% !important;
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 4px solid rgba(255, 255, 255, 0.4) !important;
        margin: 10px auto !important; 
        overflow: hidden !important;
    }
    .hex-v3 {
        position: absolute !important;
        width: 100px !important; 
        height: 100px !important;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        color: white !important;
        font-size: 13px !important;
        font-weight: bold !important;
        text-align: center !important;
        padding: 5px;
    }
    h1, h3 { color: white !important; text-align: center; }
</style>
"""
st.markdown(full_custom_style, unsafe_allow_html=True)

st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #eee;'>يوم الأحد - 26 أبريل 2026</h3>", unsafe_allow_html=True)

df = load_data()

if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    bowl_html = '<div class="bowl-v3">'
    for i, row in df.iterrows():
        if pd.isna(row['name']): continue
        random.seed(row['name'])
        c = colors[i % len(colors)]
        t = random.randint(10, 80)
        l = random.randint(10, 80)
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
    bowl_html += '</div>'
    st.markdown(bowl_html, unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding: 50px;'><h3>بانتظار أول بصمة في الوعاء... ⏳</h3></div>", unsafe_allow_html=True)

time.sleep(10)
st.rerun()
