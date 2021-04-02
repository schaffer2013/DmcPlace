from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/index')
def show_index():
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    return render_template("index.html", user_image = 'static/winner.jpg')

@app.route('/')
def hello_world():
  return 'Hi Lillian, I have a website! from, Phil'

if __name__ == '__main__':
  app.run()