from flask import Flask, render_template, request
import main.py as main

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report')
def generate_report():
        url = request.args.get('url')
        # Call the main.py functions with the provided URL
        report = main.assess_accessibility(url)
        # Generate the report using the results
        # Return the rendered report template
        return render_template('report.html', report=report)

if __name__ == '__main__':
    app.run()