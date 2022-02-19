from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "http://media.toucharger.com/web/toucharger/upload/image_domain/7/6/76060/76060.gif",
   "https://c.tenor.com/b6QMBjap5woAAAAC/hfr-finkielkraut.gif",
   "https://media1.giphy.com/media/hmxZRW8mhs4ak/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")