import streamlit as st
from PIL import Image

def run_app_home():
    st.subheader('안녕하십니까 고객님~:smile:')
    # st.markdown('***이 앱은 고객 데이터와 신용 점수 데이터에 대한 내용입니다***')
    st.markdown('**이 앱은 데이터 분석도 가능하고, 고객님 정보를 넣으면 신용 점수도 예측해 줍니다.**')

    st.text('테스트 결과 정확률은 94%이고\nMSE값은 0.05입니다.')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqGAgFJCb-URTPng0VCd_M8PyGOWKAwXrNCg&usqp=CAU',width=500)
    




    st.markdown('**:red[자동 배포]** 처리 된 앱입니다')