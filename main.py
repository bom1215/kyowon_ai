import streamlit as st
from streamlit import session_state as state
from streamlit_extras.switch_page_button import switch_page

def main():
    if 'prev_condition' not in state:
        state.prev_condition = "choose_difficulty"
    
    if 'condition' not in state:
        state.condition = "choose_difficulty"
        
    if 'difficulty' not in state:
        state.difficulty = ''
    
    if 'topic' not in state:
        state.topic = ''
    
    if 'type' not in state:
        state.type = ''
    
    if state.condition == "choose_difficulty":
        choose_difficulty()
    
    elif state.condition == "choose_topic":
        choose_topic()
    
    elif state.condition == "choose_type":
        choose_type()
        
    elif state.condition == "learn":
        learning()

        
def choose_difficulty():
    st.set_page_config(page_title = "Difficulty", layout="wide", initial_sidebar_state="collapsed")

    if state.condition != 'choose_difficulty':
        state.prev_condition = state.condition
        main()
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>프로그램 제목</h1>", unsafe_allow_html=True)
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

        
def choose_topic():
    st.set_page_config(page_title = "Topic",layout="wide", initial_sidebar_state="collapsed")
    if state.condition != 'choose_topic':
        state.prev_condition = state.condition
        main()
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>프로그램 제목</h1>", unsafe_allow_html=True)
        for _ in range(3): st.write('')
        c1, c2, c3, c4, c5 = st.columns([0.1, 1, 0.1, 1, 0.1])
        
        first = c2.form("자기소개")
        with first:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>자기소개</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.4, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.topic = '자기소개'
                state.condition = "choose_type"
                st.experimental_rerun()
                
        second = c4.form("학교생활")
        with second:
            for _ in range(3):
                st.write('')
            st.markdown(f"<h1 style='text-align: center; color: black;'>학교생활</h1>", unsafe_allow_html=True)
            for _ in range(2):
                st.write('')
            cc1, cc2, cc3 = st.columns([1, 0.4, 1])
            submit = cc2.form_submit_button("선택")
            if submit:
                state.topic = '학교생활'
                state.condition = "choose_type"
                st.experimental_rerun()

def choose_type():
    st.set_page_config(page_title = "Type",layout="wide", initial_sidebar_state="collapsed")
    if state.condition != 'choose_type':
        state.prev_conditon = state.condition
        main()
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>프로그램 제목</h1>", unsafe_allow_html=True)
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
            # if quiz:
            #     state.quiz = True
            #     st.experimental_rerun()
            
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
                st.experimental_rerun()
        
        
QUIZZES = [
    {
        "word" : "구름",
        "image" : "ice-bear.jpg"
    },
    {
        "word" : "강아지",
        "image" :"ice-bear.jpg"
    }
]

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

def learning():
    st.set_page_config(page_title = "Learn", layout="wide")
    if state.condition != 'learn':
        state.prev_condition = state.condition
        main()
    
    else:
        st.markdown(f"<h1 style='text-align: center; color: gray;'>프로그램 제목</h1>", unsafe_allow_html=True)
        for _ in range(3):
            st.write('')

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
                mygrid[0][2*i+1].markdown(f"<h2 style='text-align: center; color: black;'>{word}</h2>", unsafe_allow_html=True)
            for i in range(3):
                st.write('')
            c1, c2, c3 = st.columns([1, 0.5, 1])
            if c2.button("학습 종료하기"):
                state.page = 0
                state.condition = 'choose_type'
                st.experimental_rerun()   

if __name__ == "__main__":
    main()