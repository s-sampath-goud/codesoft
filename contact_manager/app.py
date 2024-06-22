from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load contacts from JSON file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Save contacts to JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

@app.route('/')
def index():
    contacts = load_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_contact = {
            "name": request.form['name'],
            "phone": request.form['phone'],
            "email": request.form['email'],
            "address": request.form['address']
        }
        contacts = load_contacts()
        contacts.append(new_contact)
        save_contacts(contacts)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/update/<int:contact_id>', methods=['GET', 'POST'])
def update_contact(contact_id):
    contacts = load_contacts()
    if request.method == 'POST':
        contacts[contact_id] = {
            "name": request.form['name'],
            "phone": request.form['phone'],
            "email": request.form['email'],
            "address": request.form['address']
        }
        save_contacts(contacts)
        return redirect(url_for('index'))
    contact = contacts[contact_id]
    return render_template('update_contact.html', contact=contact, contact_id=contact_id)

@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    contacts = load_contacts()
    contacts.pop(contact_id)
    save_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_contact():
    query = request.args.get('query')
    contacts = load_contacts()
    filtered_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return jsonify(filtered_contacts)

if __name__ == '__main__':
    app.run(debug=True)
