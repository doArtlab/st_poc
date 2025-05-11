from config import Config
from openai import OpenAI
from functions import get_product_contents_from_query
from openai_helpers import generate_text
import streamlit as st

client = OpenAI(api_key=Config.openai_api_key)

# def generate_response(query: str):
#     docs = get_product_contents_from_query(query)
#     content ='\n'.join(docs)
#     text = generate_text(f"""
#                         당신은 제품에 대한 질문에 대해 제공된 Text 내에서 답을 찾는 POC 용 AI 에이전트입니다. 
#                         질문에 대한 답을 Text에서 찾아 적절한 답변을 작성하세요.  
#                         제공된 Text에 기반해서 충실한 내용이지만 명확하게 답변하세요. 하지만 반말은 삼가해 주세요.
#                         답변에서는 제공된 Text라는 말은 사용하지 말아주세요.
                         
#                          {content}
#                         """, query, "gpt-4o")
#     return text

if __name__ == "__main__":
    st.title("POC")
    st.markdown("""
    ### 주요 기능
    1. **브랜드 정보 조회**: 브랜드에 대한 상세 정보를 조회할 수 있습니다.
    2. **제품 정보 조회**: 제품에 대한 상세 정보를 조회할 수 있습니다.
    3. **제품 성분 분석**: 제품에 대한 성분 정보를 조회할 수 있습니다.
    4. **고객사 매출액 조회**: 고객사 매출액 정보를 조회할 수 있습니다.

    왼쪽 사이드바에서 원하는 기능을 선택하여 이용해보세요.
    """)


    # # 세션 상태에 메시지 저장
    # if "messages" not in st.session_state:
    #     st.session_state.messages = []

    # # 이전 채팅 기록 보여주기
    # for msg in st.session_state.messages:
    #     with st.chat_message(msg["role"]):
    #         st.markdown(msg["content"])

    # # 사용자 입력
    # prompt = st.chat_input("메시지를 입력하세요")

    # # 입력이 들어오면 처리
    # if prompt:
    #     # 사용자 메시지 저장 및 출력
    #     st.session_state.messages.append({"role": "user", "content": prompt})
    #     with st.chat_message("user"):
    #         st.markdown(prompt)

    #     response = generate_response(prompt)

    #     st.session_state.messages.append({"role": "assistant", "content": response})
    #     with st.chat_message("assistant"):
    #         st.markdown(response)

    