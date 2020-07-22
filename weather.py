from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def weather():
    return render_template('index.html')

# @app.route("index")
# def index():
#     return 

if __name__ == '__main__':
    app.run(debug=True)