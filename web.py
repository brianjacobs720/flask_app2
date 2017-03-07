from flask import Flask, render_template, request
import yelp_api
import os
app = Flask(__name__)

@app.route("/")
def index():
    name = request.values.get('name')
    rating = request.values.get('rating')
    phone = request.values.get('phone')
    location = request.values.get('location')
    term = request.values.get('term')
    result = None
    if location and term:
        result = yelp_api.get_businesses(location, term)
    return render_template('index.html', result=result)

    address = request.values.get('address')
    forecast = None
    if address:
        forecast = weather.get_weather(address)
    return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
