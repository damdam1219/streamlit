import os
import folium
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from openai import OpenAI
import plotly.express as px
from dotenv import load_dotenv
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium
from datetime import datetime, timedelta
from streamlit_option_menu import option_menu
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# 파이썬 라이브러리 가지고오기 ----------------------------------
from login_logout import login, logout
from user import my_dashboard, chat_bot, hospital, content
from admin import user_management, evaluation, service_management, money_management
from unuser import u_my_dashboard

# 페이지 기본 설정
st.set_page_config(page_title="츄러스미 심리케어",layout='wide')

# 세션 상태 초기화 -------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    
# 회원 페이지 설정 --------------------------------------------------------
def user_dashboard():
    # 사이드바 메뉴
    with st.sidebar:
        selected = option_menu(
            "츄러스미 메뉴",
            ["나의 대시보드", "심린이랑 대화하기", "심린이 추천병원", "심린이 추천 콘텐츠", "로그아웃"],
            icons=['bar-chart', 'chat-dots', 'hospital', 'camera-video', 'box-arrow-right'],
            default_index=0,
            styles={
                "container": {"padding": "5px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#b3d9ff"},
            }
        )
    if selected == '나의 대시보드':
        my_dashboard()
    elif selected == '심린이랑 대화하기':
        chat_bot()
    elif selected == '심린이 추천병원':
        hospital()
    elif selected == '심린이 추천 콘텐츠':
        content()
    else:
        logout()


# 비회원 페이지 설정 -----------------------------------------------------
def unuser_dashboard():
    # 사이드바 메뉴
    with st.sidebar:
        selected = option_menu(
            "츄러스미 메뉴",
            ["나의 대시보드", "심린이랑 대화하기", "심린이 추천병원", "심린이 추천 콘텐츠", "로그아웃"],
            icons=['bar-chart', 'chat-dots', 'hospital', 'camera-video', 'box-arrow-right'],
            default_index=0,
            styles={
                "container": {"padding": "5px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#b3d9ff"},
            }
        )
      
    if selected == '나의 대시보드':
        u_my_dashboard()
    elif selected == '심린이랑 대화하기':
        chat_bot()
    elif selected == '심린이 추천병원':
        hospital()
    elif selected == '심린이 추천 콘텐츠':
        content()
    else:
        logout()


# 관리자 페이지 설정 ---------------------------------------------------------
def admin_dashboard():
    st.title("👮‍♂️ 츄러스미 관리자 Dash Board")

    # 사이드바 메뉴
    with st.sidebar:
        admin_menu = option_menu(
            "관리자 메뉴",
            ["사용자 통계", "고객 평가", "서비스 설정", "수익 관리", "로그아웃"],
            icons=["bar-chart-line", "chat-dots", "gear", "currency-dollar", "box-arrow-right"],
            menu_icon="gear",
            default_index=0
        )

    if admin_menu == "사용자 통계":
        user_management()
    elif admin_menu == "고객 평가":
        evaluation()
    elif admin_menu == "서비스 설정":
        service_management()
    elif admin_menu == "수익 관리":
        money_management()
    else:
        logout()

# 앱 구동 ----------------------------------------------------------------
if st.session_state.logged_in:
    if st.session_state.role == "admin":
        admin_dashboard()
    elif st.session_state.role == "user":
        user_dashboard()
    else:
        unuser_dashboard()
else:
    login()