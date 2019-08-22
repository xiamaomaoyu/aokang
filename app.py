from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/AntiguaAndBarbuda')
def antigua():
    return render_template('AntiguaAndBarbuda.html')


@app.route('/sai')
def sai():
    return render_template('Sai.html')

@app.route('/491subclass')
def subclass491():
    return render_template('491subclass.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)
