from flask import Flask, render_template, redirect, url_for

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = 'replace later'
    from routes import register_routes
    register_routes(app)
    return app
  