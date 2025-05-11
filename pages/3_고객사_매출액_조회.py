from config import Config
from openai import OpenAI
from functions import get_customer_sales_from_query
from openai_helpers import generate_text
import streamlit as st

client = OpenAI(api_key=Config.openai_api_key)

def generate_response(query: str):
    docs = get_customer_sales_from_query(query)
    print(docs)
    content ='\n'.join(docs)
    text = generate_text(f"""
                        당신은 제품에 대한 질문에 대해 제공된 Text 내에서 답을 찾는 POC 용 AI 에이전트입니다. 
                        질문에 대한 답을 Text에서 찾아 적절한 답변을 작성하세요.  
                        제공된 Text에 기반해서 충실한 내용이지만 명확하게 답변하세요. 하지만 반말은 삼가해 주세요.
                        답변에서는 제공된 Text라는 말은 사용하지 말아주세요.
                         
                         {content}
                        """, query, "gpt-4o")
    return text

if __name__ == "__main__":
    st.title("POC 고객사 매출액 조회 모듈 (From Dart 보고서 데이터)")

    # 세션 상태에 메시지 저장
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 이전 채팅 기록 보여주기
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 사용자 입력
    prompt = st.chat_input("어떤 고객사의 매출액 정보를 알고 싶으신가요?")

    # 입력이 들어오면 처리
    if prompt:
        # 사용자 메시지 저장 및 출력
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = generate_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    