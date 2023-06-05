import streamlit as st
import numpy as np
import joblib
import math
# from tkinter.tix import COLUMN
# from pyparsing import empty




def run_app_ml():
    st.subheader('이 메뉴는 신용점수를 예측하는 메뉴입니다.')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.radio(':man::woman:성별 선택', ['남자','여자'])
        if gender == '남자' :
            gender = 0
        else :
            gender = 1

    with col2:
        MaritalStatus = st.radio(':couple:결혼 여부 선택', ['미혼','기혼'])
        if MaritalStatus == '기혼' :
            MaritalStatus = 0
        else :
            MaritalStatus = 1

    with col3:
        HomeOwnership = st.radio(':house:주택 소유 선택', ['소유','임대'])
        if HomeOwnership == '소유' :
            HomeOwnership = 0
        else :
            HomeOwnership = 1

    with col4:
        Education = st.radio(':male-student:최종 학력을 선택하세요.',['고등학교 졸업','대학교 졸업','학사 학위','석사 학위','박사 학위'])
        if Education == '고등학교 졸업' :
            Education = 0
        elif Education == '대학교 졸업' :
            Education = 1
        elif Education == '학사 학위' :
            Education = 2
        elif Education == '석사 학위' :
            Education = 3
        else:
            Education = 4
    age = st.number_input('나이를 입력해주세요.', 18,100)

    NumberofChildren = st.number_input('자녀 수를 입력해주세요.', 0,10)

    Income = st.number_input('연봉을 입력해주세요.', 5000,1000000)


    if st.button('신용점수 예측'):
        new_data = np.array([age,gender,Income,Education,MaritalStatus,NumberofChildren,HomeOwnership])
        new_data = new_data.reshape(1,7)

        regressor = joblib.load('model/regressor1.pkl')

        y_pred = regressor.predict(new_data)
        print(y_pred)

        print(y_pred[0].round(1))

        price = y_pred[0].round(1)
        print(f'고객님의 신용점수는 {price}점 입니다.')

        if price < 0 :
            st.subheader('죄송합니다. 0점 미만은 표시할 수 없습니다.')
        else :
            st.subheader(f'고객님의 신용점수는 {price}점입니다.')
            st.text('0점:낮음\n1점:보통\n2점:높음')