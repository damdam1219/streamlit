import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go

def u_my_dashboard():
    st.subheader(f"{st.session_state.username}님의 심리 대시보드 💉")
    st.error("🔒 회원가입 후 로그인하면, 아래 화면과 유사한 전용 대시보드 화면이 나타납니다", icon="⚠️")
    
    col1, col2, col3 = st.columns([2,2,2])
    with col2:
        st.markdown("### 가입하면 이런 기능을 쓸 수 있어요!")
        col7, col4,col5 = st.columns([1,2,1])
        st.markdown("**⭐개인 맞춤형 감정 분석 차트**")
        st.markdown(" **⭐시간별 우울 점수 변화 추이**")
        st.markdown(" **⭐심리 챗봇과 연계된 맞춤 행동 추천**")
        st.markdown(" **⭐심리 맟춤 미디어 추천까지!!!**")
        with col4:
            img = Image.open("설명하는츄러스미.png")
            st.image(img, width=450) # 츄러스미 이미지 삽입

    with col1:
        col5, col6 = st.columns([1,2])
        with col6:
            st.divider()
            st.metric(
                label="오늘 사용 시간",
                value="1시간 30분",
                delta="+30분"  
            )
            st.divider()
            st.metric(
            label="오늘 우울 점수",
            value="😔 25 점",
            delta="+0.5"  
        )
            st.divider()
            st.metric(
            label="최근 최고 우울 점수",
            value="📈 75 점",
            delta="+1.0"  # 전일 대비 변화 예시
        )
            st.divider()

    with col3:
        st.markdown(''' **🔯감정상태분석**''')
        # 가상 감정 데이터
        emotions = ["행복", "슬픔", "분노", "불안", "놀람", "평온"]
        values = [80, 40, 30, 60, 70, 90]  # 가상 수치

        # 레이더 차트 생성
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=values + [values[0]],
            theta=emotions + [emotions[0]],
            fill='toself',
            name='감정 점수',
            text=[f"{emo}: {val}" for emo, val in zip(emotions, values)] + [f"{emotions[0]}: {values[0]}"],
            hoverinfo='text'
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False,
            margin=dict(l=30, r=30, t=30, b=30),
            height=250,
            paper_bgcolor='#f5faff'
        )

        # Streamlit 출력
        st.plotly_chart(fig_radar, use_container_width=True)
        st.divider()    
        # ✅ 가상 데이터 생성
        dates = pd.date_range(start="2025-08-20", periods=7, freq="D")
        scores = [25, 30, 28, 40, 35, 45, 50]  # 가상의 우울 점수

        df_psych = pd.DataFrame({
            "날짜": dates,
            "우울점수": scores
        })

        # ✅ 우울 점수 변화 추이 카드
        st.markdown(''' **📉 우울점수변화추이**''')

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=df_psych['날짜'],
            y=df_psych['우울점수'],
            mode='lines+markers',
            line=dict(shape='spline', color='#EF553B'),
            marker=dict(size=8, color='#EF553B'),
            name='우울점수'
        ))
        fig_line.update_layout(
            xaxis_title='날짜',
            yaxis_title='우울점수',
            yaxis_range=[0, 100],
            height=250,
            margin=dict(l=30, r=30, t=30, b=30),
            paper_bgcolor='#f5faff'
        )

        st.plotly_chart(fig_line, use_container_width=True)
        
