from flask import Flask,session,render_template
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]
        session["turn"] = "X"
    return render_template("game.html", board=session["board"], turn=session["turn"])
