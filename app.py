from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    headers = None
    recommended_headers = ['Content-Type', 'Cache-Control', 'User-Agent', 'Content-Security-Policy',
                           'Permissions-Policy', 'X-Content-Type-Options', 'X-Frame-Options', 'Strict-Transport-Security', 'Referrer-Policy']

    if request.method == 'POST':
        url = request.form['url']
        headers = get_headers(url)

    return render_template('index.html', headers=headers, url=url, recommended_headers=recommended_headers)


def get_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.exceptions.RequestException:
        return None


if __name__ == '__main__':
    app.run(debug=True)
