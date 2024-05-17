from flask import Flask, render_template, redirect, url_for
from forms import ChatForm

def register_routes(app):
    import response
    @app.route('/',methods=['GET','POST'])
    def index():
        chat_form = ChatForm()
        if chat_form.validate_on_submit():
            query = chat_form.query.data
            queries = query.split('\n')
            with open('query.txt', 'a') as file:
                file.write("\n")
                file.writelines(queries)
            return redirect(url_for('index'))
        chat_history = []
        query = ""
        with open('query.txt','r') as file:
            chat_history = file.readlines()
            if "\n" in chat_history:
                chat_history.remove("\n")
            if len(chat_history) > 0:
                n = len(chat_history)
                query = chat_history[n-1]
        ai_response = ""
        if query != "":
            ai_response = response.generate_response(query=query)
        return render_template('index.html', form=chat_form, response=ai_response, chat_history=chat_history)