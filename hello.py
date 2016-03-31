
from flask import Flask, url_for
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/something_else")
def a_thing():
    return "something_else"

#### dynamically creating links
@app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user 
    return 'User %s' % username 

#### dynamically creating links
@app.route('/post/<int:post_id>') #in the folder 'post' , accept ints and assign to 'post_id'
def show_post(post_id):  # takes post_id as an argument (sould be an int)
# show the post with the given id, the id is an integer
    return 'Post %d' %post_id # returns a string with %d as the post_id

@app.route('/projects/')  #having specified the projects location with '/' that means you can call it with or without in address bar
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')

### outputs new urls below
### Why would I want to do this? 
# /
# /login
# /login?next=%2F
# /user/John%20Doe

### ok what's next?
### let's do something with static files
with app.test_request_context():
    print url_for('static', filename='style.css')

from flask import render_template
@app.route('/hello/') # when the route contains "/hello/"
@app.route('/hello/<name>') # when the route contains "<name>"
def hello(name=None):
    return render_template('hello.html', name=name) # render_template (use template passes name)



if __name__ == "__main__":
    # app.run()
    app.run(debug=True)  ### With debug=True the server will automatically update when you write to this file
###### NEVER USE IN PRODUCTION
