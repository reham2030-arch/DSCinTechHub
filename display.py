import streamlit as st
import pandas as pd
import random
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(layout="wide", page_title="DataHub Display")

# 2. دالة جلب البيانات (أبسط طريقة في العالم)
def load_data():
    try:
        # الرابط المباشر لتحويل الشيت إلى CSV
        # تأكدي أن هذا الرابط يفتح معك في المتصفح ويحمل ملف
        sheet_id = "1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1728246321"
        
        # قراءة البيانات مباشرة من الرابط
        df = pd.read_csv(csv_url)
        
        # إعادة تسمية الأعمدة (الاسم هو العمود الأول، والكلية هي العمود الثاني)
        # نحن نستخدم أرقام الأعمدة [0, 1] لنتجنب مشاكل اللغة العربية
        df = df.iloc[:, [0, 1]]
        df.columns = ["name", "major"]
        
        return df
    except Exception as e:
        # إذا فشل، لا تظهر خطأ أحمر، فقط اترك الوعاء فارغاً
        return pd.DataFrame(columns=["name", "major"])

# 3. الستايل (CSS) - لإرجاع التصميم الأصلي
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
    }
    .bowl-v3 {
        position: relative; width: 850px; height: 650px;
        border-radius: 50%; background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px); border: 4px solid rgba(255, 255, 255, 0.3);
        margin: 20px auto; overflow: hidden; box-shadow: 0 0 50px rgba(0,0,0,0.2);
    }
    .hex-v3 {
        position: absolute; width: 100px; height: 100px;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        display: flex; flex-direction: column; justify-content: center;
        align-items: center; color: white; font-size: 13px;
        font-weight: bold; text-align: center; padding: 8px;
        transition: all 0.5s ease;
    }
    h1, h3 { color: white !important; text-align: center; font-family: 'Arial'; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>✨ DataHub: بصمة حضور✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='opacity: 0.8;'>يوم الأحد - 26 أبريل 2026</h3>", unsafe_allow_html=True)

# 4. التنفيذ
df = load_data()

if not df.empty:
    colors = ["#224074", "#EF8D5A", "#44B18F", "#FF5C5C", "#7A57D1"]
    bowl_html = '<div class="bowl-v3">'
    for i, row in df.iterrows():
        # تجاهل الصفوف الفارغة
        if pd.isna(row['name']) or str(row['name']).strip() == "": continue
        
        # نستخدم الاسم كـ Seed ليبقى كل سداسي في مكانه الثابت
        random.seed(str(row['name'])) 
        c = colors[i % len(colors)]
        t = random.randint(15, 75)
        l = random.randint(15, 75)
        
        bowl_html += f'<div class="hex-v3" style="background-color: {c}; top: {t}%; left: {l}%;">'
        bowl_html += f'{row["name"]}<br><span style="font-size: 10px; opacity: 0.8;">{row["major"]}</span>'
        bowl_html += '</div>'
    bowl_html += '</div>'
    st.markdown(bowl_html, unsafe_allow_html=True)
    
    st.markdown(f"<p style='text-align: center; color: white; font-size: 22px; font-weight: bold;'>إجمالي البصمات: {len(df)}</p>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding: 100px; color: white;'><h3>⏳ بانتظار أول بصمة لتظهر في الوعاء...</h3></div>", unsafe_allow_html=True)

# 5. تحديث تلقائي (كل 10 ثواني)
time.sleep(4)
st.rerun()
