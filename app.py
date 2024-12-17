from flask import Flask, render_template, request, jsonify
from arithmo_compiler import ArithmoCompiler

app = Flask(__name__)
compiler = ArithmoCompiler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['expression']
    try:
        result = compiler.process_input(user_input)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
