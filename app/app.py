from flask import Flask, render_template, request
from scraper import scrape_google_maps


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results', methods=['POST'])
def results():
    location = request.form['location']
    results = scrape_google_maps(location)
    return render_template('results.html', location=location, results=results)
if __name__ == '__main__':
    app.run(debug=True)




