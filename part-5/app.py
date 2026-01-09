"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Aditi Gite',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'aditigite2005@gmail.com',
    'github': 'https://github.com/AditiS2005',
    'linkedin': 'https://www.linkedin.com/in/aditi-gite-00994432b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 50},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 80},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Why I Started Learning Flask',
        'content': 'Flask helped me understand backend development step by step.',
        'date': 'Jan 2026'
    },
    {
        'id': 2,
        'title': 'My First API Project',
        'content': 'Working with APIs taught me how real-world applications fetch data.',
        'date': 'Jan 2026'
    }
]
# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,
        posts=BLOG_POSTS
    )

@app.route('/skill/<skill_name>')
def skill(skill_name):
    # Convert 'HTML-CSS' back to 'HTML/CSS' for matching
    original_skill_name = skill_name.replace('-', '/')
    
    # Use lowercase for safer matching
    search_term = original_skill_name.lower()
    
    related_projects = []
    for project in PROJECTS:
        # Create a lowercase version of tags for comparison
        project_tech_lowered = [t.lower() for t in project['tech']]
        
        # Check if the skill matches
        if search_term in project_tech_lowered:
            related_projects.append(project)
        elif search_term == "sql" and "sqlite" in project_tech_lowered:
            related_projects.append(project)
        # Special check: if the skill is HTML/CSS, match projects that have 'HTML' or 'CSS'
        elif search_term == "html/css" and ("html" in project_tech_lowered or "css" in project_tech_lowered):
            related_projects.append(project)

    return render_template(
        'skill.html',
        info=PERSONAL_INFO,
        skill_name=original_skill_name, # Display the nice "HTML/CSS" name
        projects=related_projects
    )

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
