import streamlit as st

st.set_page_config(
    page_title="乱码转换器",
    page_icon="🤖",
    layout="centered",
)

st.header("*乱码转换器*😎")
text = st.text_area("输入乱码文本")

CODELIST = ["GBK", "Shift_Jis", "iso-8859-1", "windows-1252", "Big5", "UTF-8"]

CODE = [(X, Y) for X in CODELIST for Y in CODELIST if X != Y]
btn, tip = st.columns(2)
with btn:
    clicked = st.button("Start")
with tip:
    st.write(
        "<span style='color:red'>转换可能导致字符丢失，并非100%可以转换</span>", unsafe_allow_html=True
    )

col1, col2, col3 = st.columns(3)
col1.write("输入编码")
col2.write("实际编码")
col3.write("输出")

for code in CODE:
    col4, col5, col6 = st.columns(3)
    col4.write(code[0])
    col5.write(code[1])
    if clicked:
        try:
            col6.write(text.encode(code[0]).decode(code[1], errors="ignore"))
        except UnicodeEncodeError:
            col6.write("Error")
    else:
        col6.write("")
