from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Flask 템플릿에 API 키 전달
    api_key = "01544cba51e9151764f5af8a7637154d"
    return render_template('test.html', api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)