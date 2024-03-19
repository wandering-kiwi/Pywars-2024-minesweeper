from flask import Flask, render_template
app = Flask(__name__)
x=0
@app.route('/')
def start():
    return render_template('index.html', x=3)
@app.route('/<size>/<x>/<y>')
def button_test(size, x, y):
    print(size, x, y)
    return render_template('index.html', x=size)
if __name__=='__main__':\
    app.run(debug=True, port=80, host='0.0.0.0')