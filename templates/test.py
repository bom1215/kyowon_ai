import streamlit as st
from streamlit import session_state as state
import pandas as pd
import main

base = pd.read_csv("data/학교_초급.csv")
blank = pd.read_csv("data/학교생활-초급_blank.csv")
order = pd.read_csv("data/학교생활-초급_order.csv")

def set_test_quiz():    
    if 'test_quiz_counter' not in state:
        state.test_quiz_counter = 0
    
    if 'test_correct_answers' not in state:
        state.test_correct_answers = 0

    if state.condition == "test_quiz_score":
        test_quiz_score2(state.test_correct_answers)

quizzes = blank.sample(n = 3)

def home():
    st.set_page_config(page_title = "difficulty", layout="wide", initial_sidebar_state="collapsed")
    
    if state.condition != 'home':
        state.prev_condition = state.condition
        return state.condition
    
    else:
        for _ in range(8): st.write('')
        st.markdown(f"<h1 style='font-size:70px; text-align: center; color: black;'>AI야어여</h1>", unsafe_allow_html=True)

        for _ in range(6): st.write('')
        c1, c2, c3 = st.columns([1, 0.2, 1])
        if c2.button("시작하기"):
            state.condition = "assessment"
            st.experimental_rerun()

def assessment():
    st.set_page_config(page_title = "진단평가", layout="wide", initial_sidebar_state="collapsed")
    
    if 'test_answer' not in state:
        state.test_answer = 0
    
    if 'test_blank' not in state:
        state.test_blank = "______"

    if "test_answer_list" not in state:
        state.test_answer_list = [state.test_blank] * 10
    
    if state.test_quiz_counter == 6:
        for i in range(3):
            quiz = quizzes.iloc[i]
            answer = eval(quiz['options'])[quizzes['answer'].iloc[i]]
            if state.test_answer_list[i] == answer:
                state.test_correct_answers += 1
        del state.test_answer_list
        state.prev_condition = state.condition
        state.condition = "test_quiz_score"
        set_test_quiz()
    
    else:
        st.title("진단 평가")

        st.subheader(f"{state.test_quiz_counter + 1}번 문제")
        
        if state.test_quiz_counter < 3:
            quiz = blank.iloc[state.test_quiz_counter]
            c1, c2, c3 = st.columns([1, 3, 1])
            image_url = base.iloc[state.test_quiz_counter]['word_img']
            c2.image(image_url, width = 400)

            col1, col2, col3, col4 = st.columns(4)
            col_list = [col1, col2, col3, col4]
            for idx, col in enumerate(col_list):
                if col.button(eval(quiz['options'])[idx]):
                    state.test_answer = eval(quiz['options'])[idx]

                    if state.test_answer == quiz['word']:
                        state.test_correct_answers += 1
                        state.test_quiz_counter += 1
                    else:
                        state.test_quiz_counter += 1

                    st.experimental_rerun()
        
        elif state.test_quiz_counter < 6:
            quiz = quizzes.iloc[state.test_quiz_counter-3]
            c1, c2, c3 = st.columns([1, 8, 1])
            image_url = quiz['sen_img']
            c2.image(image_url, width = 350)
            
            container1 = c2.container()
            sent = quizzes['question'].iloc[state.test_quiz_counter-3]
            #answer = eval(quiz['options'])[blank['answer'].iloc[state.test_quiz_counter]]
            sent = "f'"+sent.replace('{}', ':blue[**{state.test_answer_list[state.test_quiz_counter-3]}**]')+"'"
            st.markdown("""
                    <style>
                        [data-testid="column"] {
                        text-align: center;
                        } 
                        [data-testid="stImage"] {
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                        }
                    </style>
                    """,
                        unsafe_allow_html=True,)
            container1.write(eval(sent))

            with container1:
                col1, col2, col3, col4 = st.columns(4)
                col_list = [col1, col2, col3, col4]
                for idx, col in enumerate(col_list):
                    if col.button(eval(quiz['options'])[idx]):
                        state.test_answer = idx
                        state.test_blank = eval(quiz['options'])[idx]
                        state.test_answer_list[state.test_quiz_counter-3] = state.test_blank
                        st.experimental_rerun()

            co1, co2, co3, co4 = st.columns([0.2, 1, 1, 0.2])
            if state.test_quiz_counter < 6:
                if col1.button("이전", disabled = (state.test_quiz_counter < 4)):
                    state.test_quiz_counter -= 1
                    st.experimental_rerun()
                if col4.button("다음", disabled = (state.test_quiz_counter > 6)):
                    state.test_quiz_counter += 1         
                    st.experimental_rerun()
            
def test_quiz_score2(score):
    if state.condition == "test_quiz_score":
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여 진단평가</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        
        if score > 4:
            color = 'green'
            diff = '고급'
        elif score > 2:
            color = 'orange'
            diff = '중급'
        else:
            color = 'red'
            diff = '초급'
        
        col1, col2 = st.columns([0.4, 1])
        col1.markdown(f"<h2 style='text-align: center; color: black;'>결과</h2>", unsafe_allow_html=True)
        col1.markdown(f"<h2 style='text-align: center; color: {color};'>{score}</h2>", unsafe_allow_html=True)
        #col1.title(f':{color}[{score*10}] 점')
        
        for _ in range(3): col2.write('')
        
        if score < 4:
            col2.info(f"{diff} 단계를 추천합니다. 추천 단계를 학습하신다면 다음 버튼을 눌러주세요")
        elif score < 8:
            col2.info(f"{diff} 단계를 추천합니다. 추천 단계를 학습하신다면 다음 버튼을 눌러주세요")
        else:
            col2.info(f"{diff} 단계를 추천합니다. 추천 단계를 학습하신다면 다음 버튼을 눌러주세요")
        
        for _ in range(3): st.write('')
        
        container1 = st.container()
        with container1:
            c1, c2, c3, c4, c5 = st.columns([1, 0.2, 0.2, 0.2, 1])
            home_button = c2.button("홈으로")
            next_button = c4.button("다음")
            
            if home_button:
                check = True
                state.condition = "choose_difficulty"
                st.experimental_rerun()
                
            if next_button:
                check = True
                state.difficulty = diff
                state.condition = "choose_topic"
                st.experimental_rerun()   
    else:
        main.main()
