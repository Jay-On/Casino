from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello-world')
def view_hello_world():
    return render_template('hello_world.html')