from flask import Flask, render_template
from markupsafe import escape
import json
import os
import sys


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

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
    port = int(os.environ.get('PORT', 900))
    app.run(debug=True, host='0.0.0.0', port=port)


# curl -X GET http://localhost:800/api/post/42
# docker stop $(docker ps -a -q) && docker image build -t flask_docker . && docker run -p 900:900 -d flask_docker