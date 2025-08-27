import pandas as pd
import numpy as np
import streamlit as st

# 관리자 임의 데이터--------------------------------------------
def create_sample_user_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    data = pd.DataFrame({
        '날짜': dates,
        '가입 수': np.random.randint(5, 50, size=30),
        '성별': np.random.choice(['남성', '여성'], size=30),
        '나이': np.random.choice(range(10, 70, 10), size=30),
        '사용 시간': np.random.uniform(5, 120, size=30),
        '이용 빈도': np.random.randint(1, 10, size=30),
        '감정': np.random.choice(['기쁨', '슬픔', '분노', '불안', '평온'], size=30)
    })
    return data

# 관리자 대시보드 ------------------------------------------------
def user_management():
    user_data = create_sample_user_data()
    
    # ---------- 상단 지표 카드 ----------
    col1, col2 = st.columns([1.5,1])
    
    with col1:
        st.error("여기는 관리자가 접근할 수 있는 영역입니다.")
        st.subheader("📊 사용자 통계")
        
    with col2:
        col6, col7, col8 = st.columns(3)

        # 평균 사용 시간 delta 계산
        delta_time = user_data["사용 시간"].iloc[-1] - user_data["사용 시간"].iloc[-2]
        delta_freq = user_data["이용 빈도"].iloc[-1] - user_data["이용 빈도"].iloc[-2]
        delta_age = user_data["나이"].iloc[-1] - user_data["나이"].iloc[-2]
        # Metric 카드
        col6.metric("⏱ 평균 사용 시간", f"{user_data['사용 시간'].mean():.0f}분", f"{delta_time:+.2f}")
        col7.metric("📈 평균 이용 빈도", f"{user_data['이용 빈도'].mean():.0f}회", f"{delta_freq:+.2f}")
        col8.metric("🎂 평균 나이", f"{user_data['나이'].mean():.0f}세", f"{delta_age:+.2f}")
    st.markdown("---")  # 구분선

    # ---------- 하단 차트 영역 ----------
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    
    # 1) 가입 추이
    with col1:
        st.markdown("🆕 **가입 추이**")
        fig_line = px.line(
            user_data, x='날짜', y='가입 수',
            markers=True,
            color_discrete_sequence=["#636EFA"]
        )
        fig_line.update_layout(height=300, width=300, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_line, use_container_width=False)
    
    # 2) 성별 비율
    with col2:
        st.markdown("👫 **성별 비율**")
        fig_pie = px.pie(user_data, names='성별', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        fig_pie.update_layout(height=300, width=300, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_pie, use_container_width=False)
    
    # 3) 나이대 분포
    with col3:
        st.markdown("🎂 **나이대 분포**")
        fig_hist = px.histogram(user_data, x='나이', nbins=10, color_discrete_sequence=["#EDB7AD"])
        fig_hist.update_layout(height=300, width=300, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_hist, use_container_width=False)
    
    # 4) 감정 트렌드
    with col4:
        st.markdown("😊 **감정 트렌드**")
        fig_emotion = px.histogram(user_data, x='감정', color='감정', 
                                   color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_emotion.update_layout(height=300, width=300, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_emotion, use_container_width=False)

def evaluation():
    st.subheader("⭐ 고객 평가")

    st.markdown("### ✅ 사용자 리뷰")
    reviews = [
        {"사용자": "user01", "리뷰": "정말 유용했어요!", "별점": 5},
        {"사용자": "user02", "리뷰": "조금 아쉬워요.", "별점": 3},
        {"사용자": "user03", "리뷰": "많은 도움이 되었어요.", "별점": 4},
    ]
    st.dataframe(pd.DataFrame(reviews))

    st.markdown("### 🚨 신고 접수 목록")
    st.warning("※ 신고 데이터는 현재 샘플 상태입니다.")
    st.write("- user02 → 챗봇 응답 부적절")
    st.write("- user05 → 욕설 포함된 리뷰")

def service_management():
    st.subheader("⚙️ 서비스 설정")

    st.markdown("### 📢 공지사항")
    st.text_area("공지사항 입력", "예: 9월 1일 서버 점검 예정입니다.")

    st.markdown("### 🛠️ 점검 모드")
    st.checkbox("서비스 점검 모드 활성화")

    st.markdown("### 🤖 챗봇 모델 선택")
    selected_model = st.selectbox("사용할 챗봇 모델을 선택하세요", ["v1.0", "v1.5", "v2.0", "GPT-4"])

def money_management():
    st.subheader("💰 수익 관리")

    st.markdown("### 🏥 병원 제휴 및 광고")
    st.write("- 행복정신과 (광고 계약 월 30만원)")
    st.write("- 마음편한의원 (심리상담 연계)")

    st.markdown("### 👩‍⚕️ 심리상담사 연결")
    st.write("현재 등록된 상담사 수: 8명")

    st.markdown("### ⭐ 프리미엄 유료 구독")
    st.metric("구독 사용자 수", 142)

    st.markdown("### 🏢 기업용 직원 감정 케어")
    st.write("기업 등록 수: 5곳")
    st.write("이용 기업: LG전자, 스타트업A 등")