import streamlit as st
from streamlit import session_state as state
import learn
import random
import quiz as quiz_code
import function
from image import *

TOPIC = {
        "초급" : ["자기소개", "학교생활"],
        "중급" : ["감정/기분 표현하기", "취미"],
        "고급" : ["식문화", "대중문화"]
    }


def choose_difficulty():
    st.set_page_config(page_title = "난이도 선택", layout="wide", initial_sidebar_state="collapsed")
    st.image('templates/user.png', width=200)


    if state.condition != 'choose_difficulty':
        state.prev_condition = state.condition
        return state.difficulty
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        c1, c2, c3, c4, c5, c6, c7 = st.columns([1, 0.1, 1, 0.1, 1, 0.1, 1])

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
            submit = cc2.form_submit_button("선택", disabled=True)
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
            submit = cc2.form_submit_button("선택", disabled=True)
            if submit:
                state.difficulty = '고급'
                state.condition = "choose_topic"
                st.experimental_rerun()

        fourth = c7.form("자유주제")
        with fourth:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>자유주제</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.6, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.difficulty = '자유주제'
                state.condition = "choose_topic"
                st.experimental_rerun()


def choose_topic(difficulty):
    st.set_page_config(page_title = "Topic",layout="wide", initial_sidebar_state="collapsed")
    st.image('templates/user.png', width=200)

    
    if state.condition != 'choose_topic':
        state.prev_condition = state.condition
        return state.topic
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>AI야어여</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        if state.difficulty != '자유주제':
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
        else:
            c1, c2, c3 = st.columns([0.1, 1, 0.1])
            first = c2.form('주제 선택')
            with first:
                free_topic = st.text_input("주제를 입력하세요")
                cc1, cc2, cc3 = st.columns([1, 0.4, 1])
                submit = cc2.form_submit_button("선택")
                if submit:
                    state.topic = 'free:'+free_topic
                    state.condition = "choose_type"
                    st.experimental_rerun()


def choose_type():
    st.set_page_config(page_title = "Type",layout="wide", initial_sidebar_state="collapsed")
    st.image('templates/user.png', width=200)

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
                div.stButton {
                    text-align: center;
                }
                div.stButton > button:first-child {
                    background-color: rgb(254, 174, 0);
                    color:White;
                    height:auto;
                    
                }
                </style>""", unsafe_allow_html=True)

            learning = cc2.form_submit_button("📖   학습하기")
            quiz = cc2.form_submit_button("🧩   퀴즈풀기")
            if learning:
                state.type = '단어'
                state.condition = 'learn'
                if state.difficulty == '초급' and state.topic == '학교생활':
                        for word in learn.words:
                            path = create_image(word)
                            learn.QUIZZES.append({"word": word, "image": path})
                            #learn.QUIZZES.append({"word": word, "image": './templates/ice-bear.jpg'})

                st.experimental_rerun()
            if quiz:
                state.type = '단어'
                state.condition = 'word_quiz'
                quiz_code.problems = random.sample(quiz_code.words, 10)
                for word in quiz_code.problems:
                    option = random.sample(quiz_code.words, 4)
                    if word not in option:
                        option[random.randint(0, 3)] = word
                    quiz_code.options.append(option)
                    path = create_image(word)
                    quiz_code.images.append(path)
                    # quiz_code.images.append('./templates/ice-bear.jpg')
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
                state.condition = 'learn'
                if state.difficulty == '초급' and state.topic == '학교생활':
                    learn.QUIZZES = []
                    for word in learn.words:
                        sent = function.make_sentence_subject(word)
                        path = create_image(sent)
                        learn.QUIZZES.append({"word": sent, "image": path})
                        #learn.QUIZZES.append({"word": sent, "image": './templates/ice-bear.jpg'})
                elif 'free:' in state.topic:
                    topic = state.topic.split(':')[1]
                    learn.QUIZZES = []
                    for i in range(2):
                        sent = function.make_sentence_free(topic)
                        path = create_image(sent)
                        learn.QUIZZES.append({"word": sent, "image": path})
                        #learn.QUIZZES.append({"word": sent, "image": './templates/ice-bear.jpg'})
                st.experimental_rerun()
            if quiz:
                state.type = '문장'
                state.condition = "sent_learn"
                if state.difficulty == '초급' and state.topic == '학교생활':
                    quiz_code.problems = random.sample(quiz_code.words, 3)
                    quiz_code.sents, quiz_code.options = function.init_sent_quiz(quiz_code.problems)
                    quiz_code.images = []
                    for sent, word in zip(quiz_code.sents, quiz_code.problems):
                        path = create_image(sent.replace('{}',word))
                        quiz_code.images.append(path)
                        # quiz_code.images.append('./templates/ice-bear.jpg')
                    quiz_code.wrong = []
                elif 'free:' in state.topic:
                    topic = state.topic.split(':')[1]
                    quiz_code.problems = []
                    quiz_code.sents = []
                    quiz_code.options = []
                    quiz_code.images = []
                    for i in range(2):
                        sent = function.make_sentence_free(topic)
                        generated_sent, option, answer = function.make_blank_free(sent)
                        quiz_code.problems.append(answer)
                        quiz_code.sents.append(generated_sent.replace('___', '{}'))
                        quiz_code.options.append(option)
                        path = create_image(sent)
                        quiz_code.images.append(path)
                        #quiz_code.images.append('./templates/ice-bear.jpg')

                st.experimental_rerun()


