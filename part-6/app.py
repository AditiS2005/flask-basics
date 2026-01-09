from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial data
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High', 'due_date': '2026-01-10'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium', 'due_date': '2026-01-15'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low', 'due_date': '2026-01-20'},
]

@app.route('/')
def index():
    # Sort tasks by due_date: Soonest first
    TASKS.sort(key=lambda x: x.get('due_date', '9999-12-31'))
    
    stats = {
        'total': len(TASKS),
        'completed': len([t for t in TASKS if t['status'] == 'Completed']),
        'pending': len([t for t in TASKS if t['status'] != 'Completed'])
    }
    return render_template('index.html', tasks=TASKS, stats=stats)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Fixed: Capture due_date from the form
        new_id = max([t['id'] for t in TASKS], default=0) + 1
        new_task = {
            'id': new_id,
            'title': request.form.get('title'),
            'status': 'Pending',
            'priority': request.form.get('priority'),
            'due_date': request.form.get('due_date') # Added this line
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if not task:
        return "Task not found", 404

    if request.method == 'POST':
        task['title'] = request.form.get('title')
        task['priority'] = request.form.get('priority')
        task['due_date'] = request.form.get('due_date')
        task['status'] = request.form.get('status')
        return redirect(url_for('index'))
        
    return render_template('edit.html', task=task)

@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))

@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)