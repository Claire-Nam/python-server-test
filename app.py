from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# def hello_world():
#     return 'Hello World!'
def home():
    return render_template('index.html')

@app.route('/second')
def page2():
    return render_template('second.html')

@app.route('/third')
def page3():
    return render_template('third.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug=True)