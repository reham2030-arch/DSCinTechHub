import streamlit as st
import pandas as pd
import random
import time
from streamlit_gsheets import GSheetsConnection
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. دالة جلب البيانات من Google Sheets (التعديل الجوهري هنا)
def load_data():
    try:
        # إنشاء الاتصال بمكتبة gsheets
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # رابط الشيت الخاص بك
        url = "https://docs.google.com/spreadsheets/d/1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48/edit?usp=sharing"
        
        # القراءة من الورقة الظاهرة في صورتك "Form Responses 1"
        df = conn.read(spreadsheet=url, worksheet="Form Responses 1")
        
        # حسب الصورة: العمود الأول الاسم، الثاني الكلية، الثالث الوقت
        # سنقوم بتسميتها ليتعرف عليها الكود بالأسفل
        df.columns = ["name", "major", "timestamp"]
        
        return df
    except Exception as e:
        # في حال وجود خطأ يظهر تنبيه بسيط للمطور
        st.sidebar.error(f"تحقق من اتصال الشيت: {e}")
        return pd.DataFrame(columns=["name", "major"])

# 3. الستايل الشامل (CSS) - كما هو بجماله
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

# 4. بناء الدائرة والأشكال
df = load_data()
colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]

if not df.empty:
    bowl_html = '<div class="bowl-v3">'
    for i, row in df.iterrows():
        # التأكد من عدم وجود قيم فارغة
        if pd.isna(row['name']): continue
        
        random.seed(row['name'])
        c = colors[i % len(colors)]
        t = random.randint(10, 80) # تعديل النطاق ليناسب حجم الوعاء الجديد
        l = random.randint(10, 80)
        
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
    bowl_html += '</div>'
    st.markdown(bowl_html, unsafe_allow_html=True)

    # 5. الإحصائيات (Bar Chart) - كما هي
    st.markdown("<br><h3>📊 إحصائيات الكليات</h3>", unsafe_allow_html=True)
    counts = df['major'].value_counts().reset_index()
    counts.columns = ['الكلية', 'عدد البصمات']

    fig = px.bar(
        counts, x='الكلية', y='عدد البصمات',
        text='عدد البصمات', color='الكلية',
        color_discrete_sequence=colors
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="white", showlegend=False, height=350,
        xaxis=dict(showgrid=False, title="", tickfont=dict(size=14)),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title="")
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown(f"<p style='text-align: center; color: white; font-size: 20px; font-weight: bold;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)

else:
    st.markdown("<div style='text-align:center; padding: 50px;'><h3>بانتظار أول بصمة في الوعاء... ⏳</h3></div>", unsafe_allow_html=True)

# 6. التحديث كل 10 ثوانٍ (أفضل للأداء)
time.sleep(4)
st.rerun()
