import streamlit as st
from streamlit import session_state as state

WORD_QUIZZES = [
    {
        "word" : "구름",
        "image" : "templates/ice-bear.jpg"
    },
    {
        "word" : "강아지",
        "image" :"templates/ice-bear.jpg"
    }
]

SEN_QUIZZES = [
    {
        "word" : "하늘이 파랗다",
        "image" : "templates/ice-bear.jpg"
    },
    {
        "word" : "사과가 빨갛다",
        "image" :"templates/ice-bear.jpg"
    }
]

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

def learning(difficulty, topic, type):
    st.set_page_config(page_title = "Learn", layout="wide")
    
    # difficulty, topic, type에 따라 QUIZZES에 들어가는 걸 바꾸시면 될 것 같아요
    if type == "단어":
        QUIZZES = WORD_QUIZZES
    elif type == "문장":
        QUIZZES = SEN_QUIZZES
            
    if difficulty == '초급' and topic == '학교생활':
            with open('학교_초급.csv', 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f)
                words = list(reader)[1:]
                
            if type == "단어":
                QUIZZES = []
                for i in words:
                    QUIZZES.append({"word":i[2], "image":i[4]})
            
            if type == "문장":
                QUIZZES = []
                for i in words:
                    QUIZZES.append({"word":i[1], "image":i[3]})
                    
    if state.condition != 'learn':
        state.prev_condition = state.condition
        return True
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>프로그램 제목</h1>", unsafe_allow_html=True)
        for _ in range(3):
            st.write('')

        # difficulty, topic, type에 따라 QUIZZES에 들어가는 걸 바꾸시면 될 것 같아요
        if type == "단어":
            QUIZZES = WORD_QUIZZES
        elif type == "문장":
            QUIZZES = SEN_QUIZZES
        
        if "page" not in state:
            state.page = 0


        def nextpage(): state.page += 1
        def prevpage(): state.page -= 1

        placeholder = st.empty()
        c1, c2 = st.columns(2)
        c3, c4, c5 = c2.columns([2, 2, 1])
        if state.page < len(QUIZZES):
            c1.button("이전", on_click = prevpage, disabled = (state.page < 1))
            c5.button("다음",on_click=nextpage,disabled=(state.page > len(QUIZZES)))

        for word in QUIZZES:
            st.sidebar.write(word["word"])
        
        for i in range(len(QUIZZES)):
            if state.page == i:
                c1, c2 = placeholder.columns(2)
                with c1:
                    c1.image(QUIZZES[i]["image"])
                word = QUIZZES[i]["word"]
                with c2:
                    c2.markdown(f"<h1 style='text-align: center; color: black;'>{word}</h1>", unsafe_allow_html=True)

        if state.page == len(QUIZZES):
            c1, c2, c3 = st.columns(3)
            c2.markdown(f"<h2 style='text-align: center; color: black;'>오늘 배운 단어</h2>", unsafe_allow_html=True)
            st.markdown('---')
            mygrid = make_grid(1, 4)
            for i in range(len(QUIZZES)):
                image0 = QUIZZES[i]['image']
                mygrid[0][2*i].image(image0)
                word = QUIZZES[i]["word"]
                mygrid[0][2*i+1].markdown(f"<h3 style='text-align: center; color: black;'>{word}</h3>", unsafe_allow_html=True)
            for i in range(3):
                st.write('')
            c1, c2, c3 = st.columns([1, 0.5, 1])
            if c2.button("학습 종료하기"):
                state.page = 0
                state.condition = 'choose_type'
                st.experimental_rerun()