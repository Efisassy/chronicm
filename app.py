
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy data to simulate a database
table_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        # Add user input to the table_data list
        table_data.append(user_input)
        return redirect('/report')
    
    return render_template('report.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)


