import streamlit as st
from streamlit import session_state as state

TOPIC = {
        "초급" : ["자기소개", "학교생활"],
        "중급" : ["감정/기분 표현하기", "취미"],
        "고급" : ["식문화", "대중문화"]
    }

def choose_difficulty():
    st.set_page_config(page_title = "difficulty", layout="wide", initial_sidebar_state="collapsed")

    if state.condition != 'choose_difficulty':
        state.prev_condition = state.condition
        return state.difficulty
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        c1, c2, c3, c4, c5 = st.columns([1, 0.1, 1, 0.1, 1])

        first = c1.form("초급")
        with first:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>초급</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.6, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.difficulty = '초급'
                state.condition = "choose_topic"
                st.experimental_rerun()
                
        second = c3.form("중급")
        with second:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>중급</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.6, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.difficulty = '중급'
                state.condition = "choose_topic"
                st.experimental_rerun()
                
        third = c5.form("고급")
        with third:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>고급</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.6, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.difficulty = '고급'
                state.condition = "choose_topic"
                st.experimental_rerun()

        
def choose_topic(difficulty):
    st.set_page_config(page_title = "Topic",layout="wide", initial_sidebar_state="collapsed")
    
    if state.condition != 'choose_topic':
        state.prev_condition = state.condition
        return state.topic
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        c1, c2, c3, c4, c5 = st.columns([0.1, 1, 0.1, 1, 0.1])
        
        topics = TOPIC[difficulty]
        
        first = c2.form(topics[0])
        with first:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>{topics[0]}</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.4, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.topic = topics[0]
                state.condition = "choose_type"
                st.experimental_rerun()
                
        second = c4.form(topics[1])
        with second:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>{topics[1]}</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.4, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.topic = topics[1]
                state.condition = "choose_type"
                st.experimental_rerun()

def choose_type():
    st.set_page_config(page_title = "Type",layout="wide", initial_sidebar_state="collapsed")
    
    if state.condition != 'choose_type':
        state.prev_conditon = state.condition
        return state.condition
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        c1, c2, c3, c4, c5 = st.columns([0.1, 1, 0.1, 1, 0.1])
        
        first = c2.form("단어")
        with first:
            for _ in range(2):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>단어</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([0.2, 1, 0.2])
            m = st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: rgb(254, 174, 0);
                    color:White;
                    height:auto;
                    padding-top:10px;
                    padding-bottom:10px;
                    padding-right:100px;
                    padding-left:100px;
                }
                </style>""", unsafe_allow_html=True)

            learning = cc2.form_submit_button("📖   학습하기")
            quiz = cc2.form_submit_button("🧩   퀴즈풀기")
            if learning:
                state.type = '단어'
                state.condition = 'learn'
                st.experimental_rerun()
            if quiz:
                state.type = '단어'
                state.condition = 'word_quiz'
                st.experimental_rerun()
            
        second = c4.form("문장")
        with second:
            for _ in range(2):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>문장</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([0.2, 1, 0.2])
            m = st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: rgb(254, 174, 0);
                    color:White;
                    height:auto;
                    padding-top:10px;
                    padding-bottom:10px;
                    padding-right:100px;
                    padding-left:100px;
                }
                </style>""", unsafe_allow_html=True)

            learning = cc2.form_submit_button("📖   학습하기")
            quiz = cc2.form_submit_button("🧩   퀴즈풀기")
            if learning:
                state.type = '문장'
                state.condition = 'sent_learn'
                st.experimental_rerun()
            if quiz:
                state.type = '문장'
                state.condition = "sent_learn"
                st.experimental_rerun()