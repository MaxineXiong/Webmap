from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('webmap.html')  # render_template(' .html'): render .html template from the 'templates' folder

if __name__ == "__main__":
    app.run(debug = True)
