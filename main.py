# from dotenv import load_dotenv  # api key loading
# load_dotenv()

from langchain_openai import ChatOpenAI  # 대화형 AI
chat_model = ChatOpenAI()  # 모델 객체 생성

import streamlit as st  # streamlit 라이브러리 임포트

st.title(" 디지털 정보 검색 " + "(" + chat_model.model + ")")
# subject = st.text_input("글 쓸 주제를 입력해 주세요", "사과")
subject = st.text_input(" 궁금한 내용을 입력해 주세요. ")

if st.button("궁금증 해결해줘~", type="primary", icon="🔥"):
    with st.spinner("Wait for it...", show_time=True):
    # with st.spinner("Wait for it..."):
        response = chat_model.invoke(subject + "에 대해 설명 해 줘")
        st.success("완료!!!")
        st.write(response.content)  # 화면 출력
