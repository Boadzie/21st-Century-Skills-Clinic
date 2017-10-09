from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_admin import Admin

app = Flask(__name__)
db = MongoEngine()
app.config['MONGODB_SETTINGS'] = {
    'db': 'people',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)
admin = Admin(app, name='flaskcom', template_mode='bootstrap3')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/clinics')
def clinics():
    return render_template('clinics.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/reach_us')
def reach_us():
    return render_template('reach_us.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
