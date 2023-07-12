import streamlit as st
from streamlit import session_state as state
import time
import pandas as pd

base = pd.read_csv("data/학교_초급.csv")
blank = pd.read_csv("data/학교생활-초급_blank.csv")
order = pd.read_csv("data/학교생활-초급_order.csv")
replay = pd.read_csv("data/추가 문제.csv")

def set_quiz():    
    if 'quiz_counter' not in state:
        state.quiz_counter = 0
    
    if 'correct_answers' not in state:
        state.correct_answers = 0

    if 'replay' not in state:
        state.replay = False

    if 'quiz_len' not in state:
        state.quiz_len = 10

    if state.condition == "quiz_score":
        quiz_score(state.correct_answers, state.quiz_len)


def word_quiz():
    st.set_page_config(page_title="단어 퀴즈", page_icon = "❓")

    if 'answer' not in state:
        state.answer = 0
    state.quiz_len = len(problems)

    if state.quiz_counter == state.quiz_len:
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        set_quiz()

    else:
        st.title("단어 퀴즈")

        st.subheader(f"{state.quiz_counter + 1}번 문제")
        quiz = blank.iloc[state.quiz_counter]
        c1, c2, c3 = st.columns([1, 3, 1])
        image_url = base.iloc[state.quiz_counter]['word_img']
        c2.image(image_url, width=400)

        col1, col2, col3, col4 = st.columns([1,1,1,1])
        col_list = [col1, col2, col3, col4]
        for idx, col in enumerate(col_list):
            if col.button(eval(quiz['options'])[idx]):
                state.answer = eval(quiz['options'])[idx]

                if state.answer == quiz['word']:
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
    st.set_page_config(page_title="문장 학습", page_icon = "❓")
    state.quiz_len = len(problems)
    if "answer_list" not in state:
        state.answer_list = ["______"] * 10

    if state.quiz_counter == state.quiz_len:
        for i in range(state.quiz_len):
            answer = problems[i]
            if state.answer_list[i] == answer:
                state.correct_answers += 1
        del state.answer_list
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        quiz_score(state.correct_answers, state.quiz_len)

    else:
        st.title("문장 퀴즈")
        st.subheader(f"{state.quiz_counter + 1}번 문제")

        c1, c2, c3 = st.columns([1, 8, 1])
        image_url = quiz['sen_img']
        c2.image(image_url, width=400)

        container1 = c2.container()

        sent = sents[state.quiz_counter]
        option = options[state.quiz_counter]
        #answer = eval(quiz['options'])[blank['answer'].iloc[state.quiz_counter]]
        sent = "f'"+sent.replace('{}', ':blue[**{state.answer_list[state.quiz_counter]}**]')+"'"
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
        container1.subheader(eval(sent))

        with container1:
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            col_list = [col1, col2, col3, col4]
            for idx, col in enumerate(col_list):
                if col.button(eval(quiz['options'])[idx]):
                    state.answer = idx
                    state.blank = eval(quiz['options'])[idx]
                    state.answer_list[state.quiz_counter] = state.blank
                    st.experimental_rerun()

        co1, co2, co3, co4 = st.columns([0.2, 1, 1, 0.2])
        if state.quiz_counter == 9:
            if co1.button("이전", disabled = (state.quiz_counter < 1)):
                state.quiz_counter -= 1
                st.experimental_rerun()
            if co4.button("완료", disabled = (state.quiz_counter > 10)):
                state.quiz_counter += 1         
                st.experimental_rerun()

        else:
            if co1.button("이전", disabled = (state.quiz_counter < 1)):
                state.quiz_counter -= 1
                st.experimental_rerun()
            if co4.button("다음", disabled = (state.quiz_counter > 10)):
                state.quiz_counter += 1            
                st.experimental_rerun()
    

def sent_quiz():
    st.set_page_config(page_title="문장 퀴즈 : 단어 배열", page_icon = "❓")
    if "sent_order" not in state:
        state.sent_order = [["______"] * 4] * 10

    quiz = order
    state.quiz_len = len(quiz)
    st.set_page_config(page_title="문장 만들기", page_icon = "❓")
    if state.quiz_counter == state.quiz_len:
        state.prev_condition = state.condition
        state.condition = "quiz_score"
        set_quiz()

    else:
        st.title("문장 퀴즈")
        st.subheader(f"{state.quiz_counter + 1}번 문제")
        quiz = quiz.iloc[state.quiz_counter]

        c1, c2, c3 = st.columns([1, 8, 1])
        image_url = quiz['sen_img']
        c2.image(image_url, width=400)

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
        container1 = c2.container()
        sent = ' '.join(state.sent_order[state.quiz_counter])
        container1.subheader(f'{sent}')

        with container1:
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            col_list = [col1, col2, col3, col4]
            for idx, col in enumerate(col_list):
                if col.button(eval(quiz['options'])[idx]):
                    
                    st.experimental_rerun()

        co1, co2, co3, co4 = st.columns([1,1,1,1])
        if state.quiz_counter == 9:
            if co1.button("이전", disabled = (state.quiz_counter < 1)):
                state.quiz_counter -= 1
                st.experimental_rerun()
            if co4.button("완료", disabled = (state.quiz_counter > 10)):
                state.quiz_counter += 1         
                st.experimental_rerun()

        else:
            if co1.button("이전", disabled = (state.quiz_counter < 1)):
                state.quiz_counter -= 1
                st.experimental_rerun()
            if co4.button("다음", disabled = (state.quiz_counter > 10)):
                state.quiz_counter += 1            
                st.experimental_rerun()




def quiz_score(score, length):
    st.set_page_config(page_title="결과", page_icon = "🏆", layout="wide")
    
    st.markdown("""
                <style>
                [data-testid="column"] {
                text-align : center;
                }
                </style>
                """,
                unsafe_allow_html=True)
    if state.condition == "quiz_score":
        st.title("학습 결과")
        st.markdown(f"<h4 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
        if (score/length) > 0.5:
            color = 'green'
        else:
            color = 'red'
        col1, col2, col3 = st.columns([1, 1, 1])
        col1.subheader("결과")
        col2.subheader("정답")
        col3.subheader("이동")

        col1, title, text, col3 = st.columns([1, 0.5, 0.5, 1])
        if col3.button("다시 풀기", disabled=((score/length) > 0.6)):
            state.condition = "loading"
            state.quiz_counter = 0
            state.correct_answers = 0
            st.experimental_rerun()
        
        if col3.button("홈 화면"):
            state.quiz_counter = 0
            state.correct_answers = 0
            state.condition = "choose_difficulty"
            st.experimental_rerun()

        col1.title(f':{color}[{score*10}] / {length*10} 점')

        if state.prev_condition == "word_quiz":
            quiz = base['word'].to_list()
        elif state.replay:
            quiz = problems
        elif state.prev_condition == "sent_learn":
            quiz = problems

        title.write(" ")
        text.write(" ")
        for i, a in enumerate(quiz):
            title.write(f"{i+1}번")
            text.write(f"{a}")

    else:
        import main
        main.main()


def loading():
    st.set_page_config(page_title = "로딩 중", layout="wide")
    st.markdown(f"<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black;'>퀴즈 생성 중</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown("""
                    <style>
                        .stButton {
                        text-align: center;
                        }
                    </style>
                    """,
                        unsafe_allow_html=True,)
    time.sleep(5)

    c1, c2, c3 = st.columns(3)
    if c2.button("퀴즈 생성 완료"):
        state.condition = state.prev_condition
        state.prev_condition = state.condition
        state.replay = True
        st.experimental_rerun()


if __name__ == "__main__":
    word_quiz()