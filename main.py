from flask import Flask, render_template
from Stations import stations_bp

app = Flask(__name__)
app.register_blueprint(stations_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<post_id>')
def blog_post(post_id):
    return render_template('posts/' + post_id + '.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def our_team():
    return render_template('team.html')
