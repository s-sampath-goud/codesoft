from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    
    try:
        result = eval(expression)
    except Exception as e:
        return jsonify(error=str(e))
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
