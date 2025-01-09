
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask import Flask, render_template, request

app = Flask(__name__)

# Home route with input form
@app.route('/')
def home():
    return render_template('index.html')



# # Route to process form input and display output
# @app.route('/result', methods=['POST'])
# def result():
#     # Retrieve user input
#     text_input = request.form['text_input']
#     selected_option = request.form['options']

#     # Generate a response or perform a simple operation
#     response = f"You wrote: '{text_input}' and selected: '{selected_option}'"

#     # Pass the response to the result page
#     return render_template('result.html', response=response)

if __name__ == "__main__":
    app.run(debug=True)


