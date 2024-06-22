from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return jsonify(success=True)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks.pop(task_id)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
