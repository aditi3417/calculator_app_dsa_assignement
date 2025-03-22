from flask import Flask, render_template, request
from helper import perform_calculation, convert_to_float
from circle import Circle

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Invalid operation selected.')

        try:
            value1 = convert_to_float(value1)
            value2 = convert_to_float(value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Invalid input")

        try:
            result = perform_calculation(value1, value2, operation)
            return render_template('calculator.html', printed_result=str(result))
        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="Cannot divide by zero.")

    return render_template('calculator.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            c = Circle(radius)
            result = c.perimeter()
        except ValueError:
            result = "Invalid input. Please enter a number."
    return render_template('circle.html', printed_result=result)

if __name__ == '__main__':
    app.run(debug=True)
