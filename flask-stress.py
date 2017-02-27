from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/content')
def hello_content():
    r = [x for x in range(10000)]
    return render_template('content.html')


if __name__ == '__main__':
    app.run(host='192.168.100.102')
