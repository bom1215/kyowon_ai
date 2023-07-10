from flask import Flask, render_template
from templates import function

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/blank/<keyword>')
def blank(keyword):
    sentence = function.make_sentence(keyword).strip()
    #sentence = '은하가 우주의 거대한 먼지와 가스 구름에서 형성됩니다'
    sentence, words = function.make_blank(sentence)
    return render_template('blank.html', sentence=sentence, words=words)


@app.route('/order/<keyword>')
def order(keyword):
    sentence = function.make_sentence(keyword).strip()
    #sentence = '은하가 우주의 거대한 먼지와 가스 구름에서 형성됩니다'
    parts = function.order(sentence)
    return render_template('order.html', parts=parts)


if __name__ == '__main__':
    app.run(port=8000)
