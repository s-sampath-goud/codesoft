from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return ''
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length', 12)
    use_uppercase = data.get('use_uppercase', False)
    use_lowercase = data.get('use_lowercase', False)
    use_numbers = data.get('use_numbers', False)
    use_symbols = data.get('use_symbols', False)
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
