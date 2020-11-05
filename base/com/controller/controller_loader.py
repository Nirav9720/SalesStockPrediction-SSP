from base import app,render_template

@app.route('/')
def index():
    return render_template('home/index.html')

@app.route('/new')
def new():
    return render_template('registration/new_user.html')

@app.route('/reroute')
def reroute():
    return render_template('home/index.html')