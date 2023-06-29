import bardapi
import os
import openai
import re

# api key setting
openai.api_key = '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'
os.environ['_BARD_API_KEY'] = "YAhNS1UWSLEy0sY5PiorpmKA1qJlAuVaUTrefhcM3tivexEDgpKesbpu17SKf4RzenC9IA."


def isKoreanIncluded(sentence):
    '''
    :param word: 문장
    :return: 문장에 한글이 포함되어 있으면 True, 포함되어 있지 않으면 False
    '''
    for i in sentence:
        if int('0x1100', 16) < ord(i) < int('0x11ff', 16):
            return True
        if int('0x3131', 16) < ord(i) < int('0x318e', 16):
            return True
        if int('0xa960', 16) < ord(i) < int('0xa97c', 16):
            return True
        if int('0xac00', 16) < ord(i) < int('0xd7a3', 16):
            return True
        if int('0xd7b0', 16) < ord(i) < int('0xd7fb', 16):
            return True

    return False


def make_sentence(keyword):
    '''
    :param keyword: 문장 생성에 사용할 키워드
    :return: bard를 사용해서 생성한 keyword 관련 문장
    '''

    # 프롬프트 문장+사용자 키워드
    input_text = f'이미지 생성 모델에 사용 가능하고 {keyword}에 관련된 문장을 1개 생성한 뒤 생성한 문장의 처음과 끝부분에 $을 추가해서 출력해 줘'

    # 문장 생성시 기대하지 않은 결과가 나오는 경우가 존재하므로 예외처리를 통해 잘못된 문장이 생성되는 것 방지
    while True:
        try:
            response = bardapi.core.Bard().get_answer(input_text)
            sentence = response['choices'][0]['content'][0].split('$')[1]
        except:
            print('bard 문장 생성 오류')
        else:
            # 문장이 한글 대신 다른 언어로 작성된 경우 다시 생성
            if isKoreanIncluded(sentence):
                break
            else:
                continue
    return sentence


def make_blank(sentence):
    '''
    :param sentence: 빈칸을 만들 문장
    :return: 빈칸이 생긴 문장
    '''
    input_text = f'\'{sentence}\' 문장에서 단어 1개를 ___으로 대체해서 출력하고 ___ 자리에 있던 단어를 출력해 줘'

    while True:
        # gpt에서 제대로된 답변을 했는지 확인
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "문장에서 단어 1개를 ___으로 대체해서 출력하고 ___ 자리에 있던 단어를 출력해달라는 요청을 받으면 반드시 '단어 1개를 ___으로 대체한 문장':'___ 자리에 있던 단어' 형식으로 출력해줘"},
                {"role": "user", "content": '\'우주에는 수없이 많은 별이 빛나고 있습니다.\' 문장에서 단어 1개를 ___으로 대체해서 출력하고 ___ 자리에 있던 단어를 출력해 줘'},
                {"role": "assistant", "content": '우주에는 수없이 많은 ___이 빛나고 있습니다.\':\'별\''},
                {"role": "user", "content": '\'천문학자는 별을 보지 않는다\' 문장에서 단어 1개를 ___으로 대체해서 출력하고 ___ 자리에 있던 단어를 출력해 줘'},
                {"role": "assistant", "content": '___는 별을 보지 않는다\':\'천문학자\''},
                {"role": "user", "content": '\'그래도 좋은 날이 앞으로 많기를\' 문장에서 단어 1개를 ___으로 대체해서 출력하고 ___ 자리에 있던 단어를 출력해 줘'},
                {"role": "assistant", "content": '그래도 ___ 날이 앞으로 많기를\':\'좋은\''},
                {"role": "user", "content": input_text}
            ]
        )
        generated_sentence, word = response.choices[0].message.content.split(':')[:2]
        generated_sentence, word = generated_sentence.strip(), word.strip()
        generated_sentence, word = re.sub('\'', '', generated_sentence), re.sub('\'', '', word)
        if re.sub('___', word, generated_sentence) == sentence:
            break
    return generated_sentence, word