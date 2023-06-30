from flask import Flask, render_template
import function

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/solve/<keyword>')
def solve(keyword):
    sentence = function.make_sentence(keyword).strip()
    #sentence = '은하가 우주의 거대한 먼지와 가스 구름에서 형성됩니다'
    sentence, words = function.make_blank(sentence)
    return render_template('problem.html', sentence=sentence, words=words)


if __name__ == '__main__':
    app.run(port=8000)
