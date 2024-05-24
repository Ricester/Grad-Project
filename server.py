from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route('/')
def website():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
    def generate_report():
        url = request.form['url']
        # Call the main.py functions with the provided URL
        main.assess_accessibility(url)
        # Generate the report using the results
        # Return the rendered report template
        return render_template('report.html')

if __name__ == '__main__':
    app.run()