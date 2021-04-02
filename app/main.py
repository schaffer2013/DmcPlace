from flask import Flask, render_template
import os

app = Flask(__name__)

FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'winner.jpg')
    return render_template("index.html", user_image = full_filename)

@app.route('/')
def hello_world():
  return 'Hi Lillian, I have a website! from, Phil!'

if __name__ == '__main__':
  app.run()