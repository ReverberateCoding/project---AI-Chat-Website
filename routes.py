from flask import Flask, render_template, redirect, url_for
from forms import ChatForm
from response import generate_response

def register_routes(app):
    @app.route('/',methods=['GET','POST'])
    def index():
        chat_form = ChatForm()
        if chat_form.validate_on_submit():
            query = chat_form.query.data
            with open('query.txt','w') as file:
                file.write(str(query))
            return redirect(url_for('index'))
        query = ""
        with open('query.txt','r') as file:
            query = str(file.read())
        
        response = ""
        if query != "":
            response = generate_response(query=query)
        return render_template('index.html', form=chat_form, response=response)