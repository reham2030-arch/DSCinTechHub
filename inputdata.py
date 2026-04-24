import streamlit as st
import pandas as pd
import os
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="سجل بصمتك", page_icon="📝")

gradient_style = """
<style>
.stApp {
    background: linear-gradient(135deg, #65c4aa 30%, #1a395d 50%, #ee794a 80%) !important;
}



.block-container {
    background-color: rgba(255, 255, 255, 0.08);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    max-width: 600px;
    margin: auto;
    box-shadow: 0 0 40px rgba(255, 122, 69, 0.3);
    }
h1 {
text-align: center;
font-size: 40px;
font-weight: bold;
color:#ffffff !important;
}


label {
    color: #F8F7F4 !important;
}

.stMarkdown p {
    color: #F8F7F4 !important;
}

.stButton button p {
    color: #ffffff !important;
}
</style>
   
"""
st.markdown(gradient_style, unsafe_allow_html=True)
colleges_list = [
    "كلية الحاسبات وتقنية المعلومات",
    "كلية الآداب والعلوم الانسانية",
    "كلية اللغات و الترجمة",
    "كلية العلوم والآداب",
    "كلية الاتصال والإعلام",
    "كلية الاقتصاد المنزلي",
    "كلية التصاميم والفنون للبنات",
    "كلية الاقتصاد والإدارة",
    "كلية الأرصاد والبيئة وزراعة المناطق الجافة",
    "كلية الأعمال",
    "كلية المجتمع",
    "كلية العلوم",
    "كلية العلوم للبنات",
    "كلية الطب",
    "كلية علوم البحار",
    "كلية الدراسات البحرية",
    "كلية علوم الأرض",
    "كلية الهندسة",
    "كلية تصاميم البيئة",
    "كلية طب الأسنان",
    "كلية الصيدلة",
    "كلية العلوم الطبية التطبيقية",
    "كلية علوم التأهيل الطبي",
    "معهد السياحة",
    "كلية التمريض",
    "كلية الحقوق",
    "الدراسات العليا التربوية"
]

st.image("DSCicon.png",width=200)
left, mid, right = st.columns([1,20, 1])
with mid:
    

# 2. العناوين (كل واحد في سطر منفصل وموسط يدوياً لضمان عدم التداخل)
 st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>نــــادي علــم البيــانات</h1>", unsafe_allow_html=True)

 st.markdown("<p style='text-align: center; font-size: 1.2rem;'> اكتــب اسمــك واثبــت وجـــودك</p>", unsafe_allow_html=True)
with st.form("visitor_form", clear_on_submit=True):


    name = st.text_input("الاسم")
    major = st.selectbox("الكلية",colleges_list )
    submit = st.form_submit_button("إرسال")

    # تأكدي أن كل الأسطر بعد الـ if مائلة لليمين بنفس المقدار
if submit:
    if name and major:
        # إنشاء الاتصال
        # بدلاً من سطر 98 و 101 القديم، جربي هذا التنسيق:
        url = "https://docs.google.com/spreadsheets/d/1Mn0tG4L6z28yWfIL_961Sv_PM7-ESYb5CZYcPN7My48/edit?usp=sharing"
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(spreadsheet=url, worksheet="Sheet1")
        
        # تجهيز السطر الجديد
        new_data = pd.DataFrame([{"name": name, "major": major}])
        
        # دمج البيانات
        updated_df = pd.concat([df, new_data], ignore_index=True)
        
        # التحديث (تأكدي من وجود هذه السطر)
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.success("تم تسجيل بصمتك!")
        st.balloons()
    else:
            # هذا الجزء يتفعل إذا ضغط إرسال والاسم فارغ
            st.warning("نسيـت اسمـك يارهيــب")
