import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="سجل بصمتك", page_icon="📝")

# 2. تنسيق الخلفية والألوان (نفس الكود الخاص بكِ)
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
p {
    text-align: center;
    font-size: 1.2rem;
    color: #F8F7F4 !important;
}
</style>
"""
st.markdown(gradient_style, unsafe_allow_html=True)

# 3. عرض الشعار (تأكدي من وجود الصورة في GitHub)
st.image("DSCicon.png", width=200)

# 4. العناوين
st.markdown("<h1>نــــادي علــم البيــانات</h1>", unsafe_allow_html=True)
st.markdown("<p>اكتــب اسمــك واثبــت وجـــودك</p>", unsafe_allow_html=True)

# 5. رابط الجوجل فورم الخاص بك (الذي أرسلتيه لي)
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe-0h5i6vI_p4H8Y9W_Uq0K7M-lI-78W3kXn7N9-o8-8-8-8/viewform?embedded=true"
# ملاحظة: استبدلي الرابط أعلاه برابط الفورم الذي يبدأ بـ "viewform?embedded=true" لتحصلي على أفضل مظهر

# 6. تضمين الفورم داخل الصفحة
st.components.v1.iframe("https://forms.gle/XNMENfvqnxcFUv8P9", height=600, scrolling=True)

# رسالة تشجيعية
st.markdown("<p style='font-size: 0.9rem; margin-top: 20px;'>بعد الضغط على إرسال، ستظهر بصمتك في وعاء البيانات تلقائياً ✨</p>", unsafe_allow_html=True)
