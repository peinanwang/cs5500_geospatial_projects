
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from markupsafe import escape
from Visualize_in_browser.visualize_in_browser import visualize_in_browser
import os
import json
import sys


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        visualize_in_browser(file.filename)
    return render_template('/index.html', form=form)

'''
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('/index.html')
'''


'''
@app.route('/')
def new_page():
    return render_template('newpage.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/api/post/<int:post_id>', methods=['GET', 'POST'])
def show_certain_post(post_id):
    j_object = {"id":post_id,"content":"foo"}
    return json.dumps(j_object)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
'''

# This starts the flask app configured to listen on port 900
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5500))
    app.run(debug=True, host='0.0.0.0', port=port)


# curl -X GET http://localhost:800/api/post/42
# docker stop $(docker ps -a -q) && docker image build -t flask_docker . && docker run -p 5500:5500 -d flask_docker

