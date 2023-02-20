from datetime import datetime
date = datetime.now()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "date and time is" + str(date)

if __name__ == "__main__":
    app.run(debug=True)
