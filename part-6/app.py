"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from datetime import datetime

# Updated data with due dates
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High', 'due_date': '2026-01-10'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium', 'due_date': '2026-01-15'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low', 'due_date': '2026-01-20'},
]

# 1. Home Route - List all tasks
@app.route('/')
def index():
    # Calculate Statistics
    stats = {
        'total': len(TASKS),
        'completed': len([t for t in TASKS if t['status'] == 'Completed']),
        'pending': len([t for t in TASKS if t['status'] != 'Completed'])
    }
    return render_template('index.html', tasks=TASKS, stats=stats)
# 2. Add Route - Form to add a task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Logic to "add" a task (it stays in memory until restart)
        new_id = len(TASKS) + 1
        new_task = {
            'id': new_id,
            'title': request.form.get('title'),
            'status': 'Pending',
            'priority': request.form.get('priority')
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))
    return render_template('add.html')

# 3. Task Detail Route - View single task
@app.route('/task/<int:id>')
def task_detail(id):
    # Find task by ID
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

# 4. About Route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    # This creates a new list excluding the task with the matching ID
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)