import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def run_app_eda():
    st.subheader('이 메뉴는 데이터 분석메뉴입니다')
    st.text('데이터 출처:https://www.kaggle.com/')

    df = pd.read_csv('data/Credit Score Classification Dataset.csv',
                     encoding='ISO-8859-1')
    print(df)

    df_new = pd.DataFrame()
    df_new['Age'] = df['Age']
    df_new['Gender'] = df['Gender'].replace('Male',0).replace('Female',1)
    # df_new['Gender'] = df['Gender'].replace('Female',1) 

    df_new['Income'] = df['Income']
    df_new['Education'] = df['Education'].replace('High School Diploma',0).replace("Associate's Degree",1).replace("Bachelor's Degree",2).replace("Master's Degree",3).replace('Doctorate',4) 
    # df_new['Education'] = df['Education'].replace("Associate's Degree",1)
    # df_new['Education'] = df['Education'].replace("Bachelor's Degree",2)
    # df_new['Education'] = df['Education'].replace("Master's Degree",3)
    # df_new['Education'] = df['Education'].replace('Doctorate',4)
    df_new['Marital Status'] = df['Marital Status'].replace('Married',0).replace('Single',1)
    # df_new['Marital Status'] = df['Marital Status'].replace('Single',1) 

    df_new['Number of Children'] = df['Number of Children']
    df_new['Home Ownership'] = df['Home Ownership'].replace('Owned',0).replace('Rented',1)
    # df_new['Home Ownership'] = df['Home Ownership'].replace('Rented',1)

    df_new['Credit Score'] = df['Credit Score'].replace('Low',0).replace('Average',1).replace('High',2)
    # df_new['Credit Score'] = df['Credit Score'].replace('Average',1)
    # df_new['Credit Score'] = df['Credit Score'].replace('High',2) 


    st.subheader('데이터 프레임 보기')
    st.dataframe(df)

    if st.checkbox('숫자로 바꾼 데이터 프레임 보기'):
        st.dataframe(df_new)
  
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    if st.checkbox('숫자로 바꾼 기본 통계 데이터 보기'):
        st.dataframe(df_new.describe())

    st.subheader('Nan데이터 확인')
    st.dataframe(df_new.isna().sum())

    st.subheader('컬럼 별 히스토그램')
    
    column = st.selectbox('파이차트 확인할 컬럼을 선택하세요.', df.columns[0:])
    bins = st.number_input('빈의 갯수를 입력하세요.',10,30,20)

    
    fig = plt.figure(figsize=(10,8))
    df[column].hist(bins=bins)

    plt.title(column + " Histogram")
    plt.xlabel(column)
    plt.ylabel("count")

    st.pyplot(fig)


    st.subheader('상관 관계 분석')

    column_list = st.multiselect('상관분석 하고싶은 컬럼을 선택하세요.', df_new.columns[0:])

    if len(column_list) >= 2 :
        fig2 = plt.figure()
        sns.heatmap(data=df_new[column_list].corr(),
            annot=True, vmin=-1,vmax=1,cmap='coolwarm',
            fmt='.2f', linewidths = 0.5)
        st.pyplot(fig2)

    print(column_list)