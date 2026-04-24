import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. الستايل (CSS) - نضعه في البداية لضمان ظهور التصميم فوراً
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important; }
    .bowl-v3 {
        position: relative; width: 800px; height: 600px;
        border-radius: 50%; background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px); border: 4px solid rgba(255, 255, 255, 0.4);
        margin: auto; overflow: hidden;
    }
    .hex-v3 {
        position: absolute; width: 100px; height: 100px;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; color: white; font-size: 13px;
        font-weight: bold; text-align: center; padding: 5px;
    }
    h1, h3 { color: white !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. جلب البيانات
def load_data():
    try:
        # الرابط المباشر (تأكدي من الـ gid من شريط العنوان في متصفحك)
        sheet_id = "1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=210446684"
        df = pd.read_csv(csv_url)
        # نأخذ أول عمودين (الاسم والكلية)
        df = df.iloc[:, [0, 1]]
        df.columns = ["name", "major"]
        return df
    except:
        return pd.DataFrame(columns=["name", "major"])

st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #eee;'>يوم الأحد - 26 أبريل 2026</h3>", unsafe_allow_html=True)

# 4. عرض الوعاء (الدائرة)
df = load_data()
bowl_html = '<div class="bowl-v3">'
if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    for i, row in df.iterrows():
        if pd.isna(row['name']): continue
        random.seed(str(row['name']))
        c = colors[i % len(colors)]
        t = random.randint(15, 75)
        l = random.randint(15, 75)
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
else:
    bowl_html += '<div style="display: flex; justify-content: center; align-items: center; height: 100%; color: white; opacity: 0.5;"><h3>⏳ بانتظار البصمات...</h3></div>'
bowl_html += '</div>'
st.markdown(bowl_html, unsafe_allow_html=True)

# 5. الإحصائيات (أجبرناها على الظهور بشكل أجمل)
# 5. الإحصائيات (نسخة مطابقة للصورة)
st.markdown("<br><h3 style='text-align: center; color: white;'>📊 إحصائيات الكليات</h3>", unsafe_allow_html=True)

if not df.empty:
    # حساب عدد البصمات لكل كلية
    counts = df['major'].value_counts().reset_index()
    counts.columns = ['الكلية', 'العدد']
    
    # إنشاء الرسم البياني الملون
    fig = px.bar(
        counts, 
        x='الكلية', 
        y='العدد', 
        color='الكلية', 
        text='العدد',
        color_discrete_sequence=["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    )
    
    # تعديل المظهر ليكون شفافاً وبألوان بيضاء للنصوص
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="white",
        showlegend=False,
        height=400,
        xaxis=dict(showgrid=False, title="", tickfont=dict(size=14)),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title="")
    )
    
    # وضع الأرقام فوق الأعمدة
    fig.update_traces(textposition='outside', marker_line_width=0)
    
    # عرض الرسم البياني
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # عرض إجمالي البصمات في المنتصف
    st.markdown(f"<p style='text-align: center; color: white; font-size: 24px; font-weight: bold;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)
else:
    st.info("بانتظار البيانات لرسم الإحصائيات...")

time.sleep(5)
st.rerun()
