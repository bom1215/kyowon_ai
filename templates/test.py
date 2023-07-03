import streamlit as st
from streamlit import session_state as state
import pandas as pd
import main

blank = pd.read_csv("data/학교생활-초급_blank.csv")
order = pd.read_csv("data/학교생활-초급_order.csv")

QUIZZES = [
    {
        "question": "1",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": 1,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "2",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "3",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "4",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "5",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "6",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "7",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "8",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "9",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    },
    {
        "question": "10",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0,
        "image" : "templates/ice-bear.jpg"
    }
    
]

def set_test_quiz():    
    if 'test_quiz_counter' not in state:
        state.test_quiz_counter = 0
    
    if 'test_correct_answers' not in state:
        state.test_correct_answers = 0

    if state.condition == "test_quiz_score":
        test_quiz_score(state.test_correct_answers)

quizzes = blank.sample(n = 3)

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
        state.condition = "test_quiz_score"
        set_test_quiz()
    
    else:
        st.title("진단 평가")

        st.subheader(f"{state.test_quiz_counter + 1}번 문제")
        
        if state.test_quiz_counter < 3:
            quiz = QUIZZES[state.test_quiz_counter]
            image_url = quiz['image']
            st.image(image_url, use_column_width=True)

            col1, col2, col3, col4 = st.columns(4)
            col_list = [col1, col2, col3, col4]
            for idx, col in enumerate(col_list):
                if col.button(quiz['options'][idx]):
                    state.test_answer = idx

                    if state.test_answer == quiz['answer']:
                        state.test_correct_answers += 1
                        state.test_quiz_counter += 1
                    else:
                        state.test_quiz_counter += 1

                    st.experimental_rerun()
        
        elif state.test_quiz_counter < 6:
            c1, c2, c3 = st.columns([0.5, 1, 0.5])
            quiz = quizzes.iloc[state.test_quiz_counter-3]
            image_url = quiz['sen_img']
            c2.image(image_url, use_column_width=True)
            container1 = st.container()
            sent = quizzes['question'].iloc[state.test_quiz_counter-3]
            #answer = eval(quiz['options'])[blank['answer'].iloc[state.test_quiz_counter]]
            sent = "f'"+sent.replace('{}', ':blue[**{state.test_answer_list[state.test_quiz_counter-3]}**]')+"'"
            
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
                if col1.button("이전", disabled = (state.test_quiz_counter < 3)):
                    state.test_quiz_counter -= 1
                    st.experimental_rerun()
                if col4.button("다음", disabled = (state.test_quiz_counter > 6)):
                    state.test_quiz_counter += 1         
                    st.experimental_rerun()
            
def test_quiz_score(score):
    if state.condition != "test_quiz_score":
        print('main')
        main.main()
        
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여 진단평가</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        
        if score > 7:
            color = 'green'
            diff = '고급'
        elif score > 3:
            color = 'yellow'
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
        c1, c2, c3, c4, c5 = st.columns([1, 0.2, 0.2, 0.2, 1])
        
        if c2.button("홈으로"):
            state.condition = "choose_difficulty"
            state.test_quiz_counter = 0
            state.test_correct_answers = 0
            st.experimental_rerun()
            
        if c4.button("다음"):
            state.difficulty = diff
            state.test_quiz_counter = 0
            state.test_correct_answers = 0
            state.condition = "choose_topic"
            st.experimental_rerun()    
