import streamlit as st
import requests

# 1. إعداد الصفحة
st.set_page_config(page_title="DSChub", page_icon="💻")

# 2. تنسيق الخلفية والألوان (تنسيقك الأصلي 10/10)
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
    text-align: center;
}

/* تنسيق زر الإرسال */
.stButton button {
    background-color: #ee794a !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    width: 100%;
}
</style>
"""
st.markdown(gradient_style, unsafe_allow_html=True)

# قائمة الكليات (نفس قائمتك)
colleges_list = [
    "كلية الحاسبات وتقنية المعلومات", "كلية الآداب والعلوم الانسانية", "كلية اللغات و الترجمة",
    "كلية العلوم والآداب", "كلية الاتصال والإعلام", "كلية الاقتصاد المنزلي",
    "كلية التصاميم والفنون للبنات", "كلية الاقتصاد والإدارة", "كلية الأرصاد والبيئة وزراعة المناطق الجافة",
    "كلية الأعمال", "كلية المجتمع", "كلية العلوم", "كلية العلوم للبنات", "كلية الطب",
    "كلية علوم البحار", "كلية الدراسات البحرية", "كلية علوم الأرض", "كلية الهندسة",
    "كلية تصاميم البيئة", "كلية طب الأسنان", "كلية الصيدلة", "كلية العلوم الطبية التطبيقية",
    "كلية علوم التأهيل الطبي", "معهد السياحة", "كلية التمريض", "كلية الحقوق", "الدراسات العليا التربوية"
]

# 3. عرض المحتوى
st.image("DSCicon.png", width=200)
st.markdown("<h1>نــــادي علــم البيــانات</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem;'> اكتــب اسمــك واثبــت وجـــودك</p>", unsafe_allow_html=True)

# 4. النموذج (Form)
with st.form("visitor_form", clear_on_submit=True):
    name = st.text_input("الاسم")
    major = st.selectbox("الكلية", colleges_list)
    submit = st.form_submit_button("إرسال")

# 5. السحر: إرسال البيانات في الخلفية
if submit:
    if name and major:
        # رابط الإرسال (تعديل بسيط على رابطك ليصبح رابط إرسال استجابة)
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfwuJAr_OlNvJvwVjsxKtPsYQju2J1P94W-8KiD66owHw3gZA/formResponse"
        
        # الأكواد التي استخرجناها من رابطك
        payload = {
            "entry.1619147897": name,
            "entry.1723191584": major
        }
        
        try:
            # إرسال البيانات بدون أن يشعر المستخدم
            requests.post(form_url, data=payload)
            st.success("✨! سعدنا بمرورك .. اسمك الآن يزين لوحة زوارنا")
            st.balloons()
        except:
            st.error("عذراً، حدث خطأ في الاتصال.")
    else:
        st.warning("نسيـت اسمـك يارهيــب")
