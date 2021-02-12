from flask import Flask, request, render_template
import json

# utilize route variables to get data from URL line 16
# utilize form data to collect large swaths of info at once

app = Flask(__name__)

# creating routes
@app.route('/')
def displayHomepage():
    return render_template('index.html')

@app.route('/formExample')
def firstForm():
    return render_template('form.html')

@app.route('/results', methods=['GET'])
def simple_pizza_results():

    context = {
        'pizza_flavor': request.args.get("pizza_flavor"),
        'crust': request.args.get("crust"),
        'individual_toppings': ['mushrooms', 'olives', 'garlic']
    }
    return render_template('confirmation_page.html', **context)


with open('exampleObj.json') as example_obj_file:
    print("raw file printed = ", example_obj_file)
    jsonData = json.load(example_obj_file)
    print("just the JSON data printed = ", jsonData)


@app.route('jsonExample', methods=['GET'])
def jsonRoute():
    return jsonData


if __name__ == "__main__":
    app.run(debug=True, port=3000)