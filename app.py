import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
# from tkinter.tix import COLUMN
# from pyparsing import empty




from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main():
    st.title('**🐶:blue[신용점수 예측]🐼**')

    menu = ['Home','EDA','ML']

    with st.sidebar:
        choice = option_menu('앱 메뉴', menu,
                            icons=["bi bi-house","bi bi-bar-chart-line-fill",'bi bi-robot'],
                            menu_icon="bi bi-menu-up",default_index=0,
                            styles={
                            "container": {"padding": "5!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#02ab21"},    
                            })

    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        run_app_eda()
    else:
        run_app_ml()



if __name__ == '__main__':
    main()