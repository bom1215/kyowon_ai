import streamlit as st
from streamlit import session_state as state
from learn import learning
from menu import choose_difficulty, choose_topic, choose_type
import test
import quiz

def main():
    if 'prev_condition' not in state:
        state.prev_condition = "assessment"
    
    if 'condition' not in state:
        state.condition = "assessment"
        
    if 'difficulty' not in state:
        state.difficulty = ''
    
    if 'topic' not in state:
        state.topic = ''
    
    if 'type' not in state:
        state.type = ''

    if state.condition == "assessment":
        test.set_test_quiz()
        test.assessment()
    
    elif state.condition == "choose_difficulty":
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

    elif state.condition == "loading":
        quiz.loading()

if __name__ == "__main__":
    main()