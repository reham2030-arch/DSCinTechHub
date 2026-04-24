import streamlit as st
import pandas as pd
import random
import time

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="TechHub Display")

# 2. دالة جلب البيانات - الطريقة "السهلة" (رابط مباشر)
def load_data():
    try:
        # هذا الرابط يحول الشيت لملف CSV فوراً، وهو أضمن طريقة للقراءة
        csv_url = "https://docs.google.com/spreadsheets/d/1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48/export?format=csv&gid=1728246321"
        
        # قراءة البيانات مباشرة
        df = pd.read_csv(csv_url)
        
        # تسمية الأعمدة (الاسم، الكلية) ليتعرف عليها الكود
        df = df.rename(columns={df.columns[0]: "name", df.columns[1]: "major"})
        
        return df
    except Exception as e:
        return pd.DataFrame(columns=["name", "major"])

# 3. الستايل (CSS) - ليعود التصميم الجميل
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

st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #eee;'>يوم الأحد - 26 أبريل 2026</h3>", unsafe_allow_html=True)

# 4. جلب البيانات وعرض الأشكال السداسية
df = load_data()

if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    bowl_html = '<div class="bowl-v3">'
    for i, row in df.iterrows():
        if pd.isna(row['name']) or str(row['name']).strip() == "": continue
        
        random.seed(row['name']) # لضمان بقاء كل شخص في مكانه
        c = colors[i % len(colors)]
        t = random.randint(15, 75)
        l = random.randint(15, 75)
        
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
    bowl_html += '</div>'
    st.markdown(bowl_html, unsafe_allow_html=True)
    
    st.markdown(f"<p style='text-align: center; color: white; font-size: 20px; font-weight: bold; margin-top:20px;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding: 50px;'><h3>بانتظار أول بصمة في الوعاء... ⏳</h3></div>", unsafe_allow_html=True)

# 5. التحديث التلقائي كل 10 ثوانٍ
time.sleep(10)
st.rerun()
