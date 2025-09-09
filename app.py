from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})


@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    return jsonify({
        'message': f'你好，{name}！，你今年{age}岁'
    })


if __name__ == '__main__':
    app.run(debug=True)
