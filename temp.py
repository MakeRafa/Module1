from flask import Flask

app = Flask(__name__)

# creating routes
@app.route('/')
def displayHomepage():
    return "<h1>Welcome to your first website!</h1>"

@app.route('/route1')
def route1Info():
    return "<h3>congrats on making route1</h3>"

if __name__ == "__main__":
    app.run(debug=True, port=3000)