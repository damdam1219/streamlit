from PIL import Image
import streamlit as st

# 사용자 DB -------------------------------------------
User_DB = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
    "unuser":{"password":"unuser123", "role":"unuser"}
} 

# 로그인 UI ------------------------------------------
def login():
    col1, col2, col3 = st.columns([3,2,3])
   
    with col2:
        img = Image.open("츄러스미_1.png")  # 츄러스미 이미지 삽입
        st.image(img, use_container_width=True)
    
        st.subheader("🔐로그인")
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type = 'password')
        
        col1, col2 = st.columns([4, 2])
        with col1:
            login_button = st.button("로그인")

        with col2:
            st.text('회원가입하기')
            
        if login_button:
            if username in User_DB and User_DB[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = User_DB[username]["role"]
                st.rerun()  # 🔥 rerun으로 로그인 UI 지우고 새로 그림
            else:
                st.error("아이디 또는 비밀번호가 틀렸습니다😓")

# 로그아웃 UI --------------------------------------------------
def logout():
    st.subheader("👋 로그아웃")

    if st.session_state.get("logged_in", False):
        st.warning("로그아웃하시겠습니까?")
        if st.button("✅ 로그아웃"):
            st.session_state.logged_in = False
            st.success("성공적으로 로그아웃되었습니다!")
            st.rerun()
            login()
    else:
        st.info("이미 로그아웃된 상태입니다.")