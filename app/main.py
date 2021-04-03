from flask import Flask, render_template, request
from Grid import Grid
import os
from PIL import Image
import numpy
from skimage.color import rgb2gray
from skimage.filters import threshold_sauvola

app = Flask(__name__)

FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))
imageFile=os.path.join(basedir, app.config['UPLOAD_FOLDER'], 'winner.jpg')

im = Image.open(imageFile)
pix = numpy.array(im)
img = rgb2gray(pix)

window_size = 25
thresh_sauvola = threshold_sauvola(img, window_size=window_size)
binary_sauvola = img > thresh_sauvola

image = Image.fromarray(binary_sauvola)
image.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], 'gray.jpg'))

full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'winner.jpg')
gray_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'gray.jpg')

array_filename=os.path.join(basedir, app.config['UPLOAD_FOLDER'], 'array.jpg')
g=Grid(250,122,array_filename)
g.update(10,10,True)
g.update(10,20,True)


@app.route('/image')
def show_index():
    return render_template("index.html", user_image = full_filename)

@app.route('/gray')
def show_gray_index():
    return render_template("index.html", user_image = gray_filename)

@app.route('/post', methods = ['POST', 'GET'])
def posting():
    if request.method== 'POST':
      g.update(request.form['x'],request.form['y'],request.form['value'])
      return "Posted!"
    return "No post."

@app.route('/')
def hello_world():
  return render_template("index.html", user_image = array_filename)

if __name__ == '__main__':
  app.run()