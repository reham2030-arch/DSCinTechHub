import streamlit as st
import pandas as pd
import random
import time

# 1. إعدادات الصفحة
st.set_page_config(layout="wide", page_title="DataHub Display")

# 2. الستايل (CSS) - وضعناه هنا في البداية لضمان ظهور الدائرة حتى لو لم توجد بيانات
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
    }
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

# 3. دالة جلب البيانات (الطريقة المباشرة)
def load_data():
    try:
        # الرابط المباشر لتحويل الشيت لملف CSV (تأكدي أن الشيت "عام" Anyone with link)
        sheet_id = "1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1728246321"
        
        df = pd.read_csv(csv_url)
        # نأخذ أول عمودين فقط (الاسم والكلية)
        df = df.iloc[:, [0, 1]]
        df.columns = ["name", "major"]
        return df
    except:
        return pd.DataFrame(columns=["name", "major"])

st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #eee;'>يوم الأحد - 26 أبريل 2026</h3>", unsafe_allow_html=True)

# 4. جلب البيانات وعرض الوعاء
df = load_data()

# عرض الوعاء دائماً
bowl_html = '<div class="bowl-v3">'
if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    for i, row in df.iterrows():
        if pd.isna(row['name']) or str(row['name']).strip() == "": continue
        random.seed(str(row['name']))
        c = colors[i % len(colors)]
        t = random.randint(15, 75)
        l = random.randint(15, 75)
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.9;">{row["major"]}</span>'
        bowl_html += '</div>'
else:
    # رسالة تظهر داخل الوعاء إذا كان فارغاً
    bowl_html += '<div style="display: flex; justify-content: center; align-items: center; height: 100%; color: white; opacity: 0.5;"><h3>⏳ بانتظار أول بصمة...</h3></div>'

bowl_html += '</div>'
st.markdown(bowl_html, unsafe_allow_html=True)

# 5. الإحصائيات (تظهر فقط إذا وجد بيانات)
if not df.empty:
    st.markdown("<br><h3>📊 إحصائيات الكليات</h3>", unsafe_allow_html=True)
    counts = df['major'].value_counts().reset_index()
    counts.columns = ['الكلية', 'العدد']
    st.bar_chart(data=counts, x='الكلية', y='العدد', color="#EF8D5A")
    st.markdown(f"<p style='text-align: center; color: white; font-size: 20px;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)

# 6. التحديث
time.sleep(4)
st.rerun()
