from flask import Flask, render_template
import function

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/make_sentence/<keyword>')
def make_sentence_test(keyword):
    sentence = function.make_sentence(keyword).lstrip()
    #sentence = '비가 와 오랜만에 비가 오지 말라 했어'
    #sentence = function.make_blank(sentence)
    return render_template('problem.html', sentence=sentence)

if __name__ == '__main__':
    app.run(port=8000)
