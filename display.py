import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. دالة جلب البيانات (الطريقة المباشرة والأضمن)
def load_data():
    try:
        # رابط الشيت بصيغة التصدير المباشر (CSV) ليتخطى كل مشاكل الروابط
        # هذا الرابط يقرأ البيانات فوراً بدون تعقيدات
        csv_url = "https://docs.google.com/spreadsheets/d/1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48/export?format=csv&gid=1728246321"
        
        # قراءة البيانات مباشرة
        df = pd.read_csv(csv_url)
        
        # حسب الصورة: الاسم أولاً (A)، الكلية ثانياً (B)، الطابع الزمني ثالثاً (C)
        # سنأخذ أول عمودين فقط لضمان عدم حدوث خطأ
        df = df.iloc[:, [0, 1]] 
        df.columns = ["name", "major"]
        
        return df
    except Exception as e:
        # سأعرض لكِ الخطأ في الجانب لتعرفي إذا كان هناك مشكلة في الرابط نفسه
        st.sidebar.error(f"تحقق من الرابط: {e}")
        return pd.DataFrame(columns=["name", "major"])

# 3. الستايل الشامل (CSS) 
full_custom_style = """
<style>
    .stApp {
        background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
    }
    .bowl-v3 {
        position: relative !important;
        width: 800px !important; 
        height: 600px !important;
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

# 4. جلب البيانات وعرضها
df = load_data()

if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    bowl_html = '<div class="bowl-v3">'
    for i, row in df.iterrows():
        if pd.isna(row['name']) or str(row['name']).strip() == "": continue
        
        random.seed(row['name'])
        c = colors[i % len(colors)]
        t = random.randint(15, 75)
        l = random.randint(15, 75)
        
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
    bowl_html += '</div>'
    st.markdown(bowl_html, unsafe_allow_html=True)
    
    # إجمالي البصمات
    st.markdown(f"<p style='text-align: center; color: white; font-size: 20px; font-weight: bold;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding: 50px;'><h3>بانتظار أول بصمة في الوعاء... ⏳</h3></div>", unsafe_allow_html=True)

# 5. التحديث التلقائي
time.sleep(10)
st.rerun()
