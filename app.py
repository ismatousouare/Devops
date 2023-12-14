from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Word!'


def index():
    return "Bienvenue sur la page"

@app.route('/about')
def about():
    return 'Ceci est la page "À propos".'

if __name__ == "__main__":
    app.run(debug=True)