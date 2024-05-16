from flask import Flask, render_template, redirect, url_for
from forms import ChatForm

def register_routes(app):
    @app.route('/')
    def index():
        chat_form = ChatForm()
        return render_template('index.html', form=chat_form)