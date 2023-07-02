import streamlit as st
from streamlit import session_state as state
from streamlit_extras.switch_page_button import switch_page
from learn import learning
from menu import *
import quiz

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
        difficulty = choose_difficulty()
        if difficulty is not None:
            state.condition = "choose_topic"
            main()
    
    elif state.condition == "choose_topic":
        topic = choose_topic(state.difficulty)
        if topic is not None:
            state.condition = "choose_type"
            main()
    
    elif state.condition == "choose_type":
        condition = choose_type()
        if condition not in ["learn", "word_quiz"]:
            if condition == 'learn':
                state.condition = "learn"
                main()
        
    elif state.condition == "learn":
        condition = learning(state.difficulty, state.topic, state.type)
        if condition == True:
            state.condition = "choose_type"
            main() 
    
    elif state.condition == "word_quiz":
        quiz.set_quiz()
        quiz.word_quiz()

    elif state.condition == "sent_learn":
        quiz.set_quiz()
        quiz.sent_learn()

    elif state.condition == "sent_quiz":
        quiz.set_quiz()
        quiz.sent_quiz()

    elif state.condition == "quiz_score":
        quiz.set_quiz()

if __name__ == "__main__":
    main()