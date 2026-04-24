import streamlit as st
import pandas as pd
import random
import time
import os
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. دالة جلب البيانات
def load_data():
    file_path = "database.csv"
    if os.path.exists(file_path):
        try:
            return pd.read_csv(file_path, encoding='utf-8-sig')
        except:
            return pd.DataFrame(columns=["name", "major"])
    return pd.DataFrame(columns=["name", "major"])

# 3. الستايل الشامل (CSS) - تم تغيير الأسماء لضمان عدم التكرار
full_custom_style = """
<style>
    .stApp {
        background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
    }
    .bowl-v3 {
        position: relative !important;
        width: 900px !important; 
        height: 800px !important;
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
        font-size: 15px !important;
        font-weight: bold !important;
        text-align: center !important;
    }

    h1, h3 { color: white !important; text-align: center; }
    [data-testid="stMetric"] { background: rgba(255,255,255,0.1) !important; border-radius: 10px; }
</style>
"""
st.markdown(full_custom_style, unsafe_allow_html=True)

# 4. العناوين والتاريخ (هنا تأكدت من وجود التاريخ)
st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #eee;'>يوم الأحد - 27 أبريل 2026</h3>", unsafe_allow_html=True)

# 5. بناء الدائرة والأشكال
df = load_data()
colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]

bowl_html = '<div class="bowl-v3">'
for i, row in df.iterrows():
    random.seed(row['name'])
    c = colors[i % len(colors)]
    t = random.randint(15, 75)
    l = random.randint(15, 75)
    
    # بناء الشكل السداسي بأسلوب يمنع ظهور النص
    bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
    bowl_html += f'{row["name"]}<br><span style="font-size: 12px; opacity: 0.8;">{row["major"]}</span>'
    bowl_html += '</div>'

bowl_html += '</div>'

# عرض الدائرة مرة واحدة فقط
st.markdown(bowl_html, unsafe_allow_html=True)

# 6. الإحصائيات بشكل بياني (Bar Chart)
st.markdown("<br><h3>📊 إحصائيات الكليات</h3>", unsafe_allow_html=True)
counts = df['major'].value_counts().reset_index()
counts.columns = ['الكلية', 'عدد البصمات']

if not counts.empty:
    # إنشاء الرسم البياني باستخدام Plotly
    fig = px.bar(
        counts, 
        x='الكلية', 
        y='عدد البصمات',
        text='عدد البصمات', # إظهار الرقم فوق العمود
        color='الكلية', # تلوين كل عمود بلون مختلف
        color_discrete_sequence=["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    )

    # تحسين مظهر الرسم ليتناسب مع الخلفية الشفافة
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="white",
        showlegend=False,
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(
            showgrid=False, 
            title="",
            tickfont=dict(color='white', size=14, family="Arial") # جعل الأسماء بيضاء وكبيرة
        ),
        
        # تعديل خط الأرقام في المحور العمودي (Y)
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.1)', 
            title="",
            tickfont=dict(color='white', size=12) # جعل أرقام المحور بيضاء
        )
    )
    
    # تحسين وضع الأرقام فوق الأعمدة
    fig.update_traces(textposition='outside', marker_line_width=0)

    # عرض الرسم في ستريمليت
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

st.markdown(f"<p style='text-align: center; color: white; font-size: 20px; font-weight: bold;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)

# 7. التحديث
time.sleep(5)
st.rerun()
