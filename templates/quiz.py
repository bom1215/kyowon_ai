import streamlit as st
from streamlit import session_state as state
import time
import main

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

def set_quiz():    
    if 'quiz_counter' not in state:
        state.quiz_counter = 9
    
    if 'correct_answers' not in state:
        state.correct_answers = 0

    if state.condition == "quiz_score":
        quiz_score(state.correct_answers)


def word_quiz():
    st.set_page_config(page_title="단어 퀴즈", page_icon = "❓")

    if 'answer' not in state:
        state.answer = 0

    if state.quiz_counter == 10:
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        set_quiz()

    else:
        st.title("단어 퀴즈")

        st.subheader(f"{state.quiz_counter + 1}번 문제")
        quiz = QUIZZES[state.quiz_counter]

        image_url = quiz['image']
        st.image(image_url, use_column_width=True)

        col1, col2, col3, col4 = st.columns(4)
        col_list = [col1, col2, col3, col4]
        for idx, col in enumerate(col_list):
            if col.button(quiz['options'][idx]):
                state.answer = idx

                if state.answer == quiz['answer']:
                    #time.sleep(1)
                    st.success("맞았습니다!")
                    time.sleep(0.3)
                    state.correct_answers += 1
                    state.quiz_counter += 1
                else:
                    st.error("틀렸습니다!")
                    time.sleep(0.3)
                    state.quiz_counter += 1

                st.experimental_rerun()

def sent_learn():
    st.set_page_config(page_title="빈칸 퀴즈", page_icon = "❓")
    if 'blank' not in state:
        state.blank = "______"

    if state.quiz_counter == 10:
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        set_quiz()

    else:
        st.title("빈칸 학습")

        st.subheader(f"{state.quiz_counter + 1}번 문제")
        quiz = [
            {
                "question": "는 화성이다.",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": 0,
                "image" : 'templates/ice-bear.jpg'
            }
        ]
        quiz = quiz[0]
        image_url = quiz['image']
        st.image(image_url, use_column_width=True)
        container = st.container()
        container.write(f':blue[**{state.blank}**] {quiz["question"]}')

        with container:
            col1, col2, col3, col4 = st.columns(4)
            col_list = [col1, col2, col3, col4]
            for idx, col in enumerate(col_list):
                if col.button(quiz['options'][idx]):
                    state.answer = idx
                    state.blank = quiz['options'][idx]
                    st.experimental_rerun()

        co1, co2, co3, co4 = st.columns(4)
        if col2.button("이전"):
            state.quiz_counter -= 1
        if col3.button("다음"):
            state.quiz_counter += 1

            
            st.experimental_rerun()
    

def sent_quiz():
    st.set_page_config(page_title="문장 만들기", page_icon = "❓")
    if state.quiz_counter == 10:
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        set_quiz()

    else:
        st.title("문장 만들기")

def quiz_score(score):
    if state.condition == "quiz_score":
        st.title("단어 학습")

        if score > 5:
            color = 'green'
        else:
            color = 'red'
        col1, col2, col3 = st.columns(3)
        col1.subheader("결과")
        col1.title(f':{color}[{score*10}] 점')
        col2.subheader("정답")
        for i in range(10):
            quiz = QUIZZES[i]
            col2.text(f"{i+1}. {quiz['options'][quiz['answer']]}")

        if col3.button("다시 풀기"):
            state.condition, state.prev_condition = state.prev_condition, state.condition
            state.quiz_counter = 0
            state.correct_answers = 0
            st.experimental_rerun()
        
        if col3.button("홈 화면"):
            state.quiz_counter = 0
            state.correct_answers = 0
            state.condition = "choose_difficulty"
            st.experimental_rerun()
    else:
        main.main()

def click(stage):
    state.condition = stage

if __name__ == "__main__":
    word_quiz()