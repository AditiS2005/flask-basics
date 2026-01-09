"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open: http://127.0.0.1:5000/
"""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# ---------------- MAIN ROUTES ----------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post=post, post_id=post_id)

@app.route('/links')
def show_links():
    links_data = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links_data)

# ---------------- PRODUCT ROUTES ----------------
@app.route('/product/')
def product():
    return render_template('product.html', product=None, product_id=None)

@app.route('/product/<int:product_id>')
def show_product(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 55000},
        2: {'name': 'Mobile', 'price': 25000},
        3: {'name': 'Headphones', 'price': 3000},
    }
    product_data = products.get(product_id)
    return render_template(
        'product.html',
        product=product_data,
        product_id=product_id
    )

# ---------------- CATEGORY ROUTES ----------------
@app.route('/categories/')
def show_categories():
    categories_list = {
        "electronics": [1, 2],
        "audio_devices": [3]
    }
    return render_template('categories.html', categories=categories_list)

@app.route('/categories/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    categories_data = {
        "electronics": {
            1: {"name": "Laptop", "price": 50000},
            2: {"name": "Phone", "price": 20000}
        },
        "audio_devices": {
            3: {"name": "Headphones", "price": 3000}
        }
    }

    product_data = categories_data.get(category_name, {}).get(product_id)

    return render_template(
        'category_product.html',
        category=category_name,
        product=product_data,
        product_id=product_id
    )

# ---------------- SEARCH ROUTE ----------------
@app.route('/search')
def search():
    query = request.args.get('query', '')
    items = ["Laptop", "Mobile", "Headphones", "Flask Tutorial"]
    results = [i for i in items if query.lower() in i.lower()] if query else []
    return render_template('search.html', query=query, results=results)

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
