from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demonstration purposes

posts = [
    {'author': 'John Doe', 'title': 'First post', 'content': 'This is my first post!', 'date_posted': 'April 1, 2024'},
    {'author': 'Jane Smith', 'title': 'Second post', 'content': 'Another day, another post.', 'date_posted': 'April 2, 2024'}
]

user_array=[]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', title='Post', post=posts[post_id])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add login logic here
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])  # Add methods=['GET', 'POST'] to allow both GET and POST requests
def register():
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        dob = request.form['dob']
        gender = request.form['gender']
        
        # Create user object
        user = {
            'full_name': full_name,
            'email': email,
            'password': password,
            'dob': dob,
            'gender': gender
        }
        
        # Add user to user_array
        user_array.append(user)
        
        # Redirect to login page
        return redirect(url_for('login'))
    else:
        # Handle GET request (render the register page)
        return render_template('register.html')


@app.route('/addpost', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        # Add date_posted logic here if needed
        new_post = {'author': author, 'title': title, 'content': content, 'date_posted': 'April 6, 2024'}  # Dummy date for demonstration
        posts.append(new_post)
        return redirect(url_for('home'))
    else:
        return render_template('add_post.html', title='Add Post')


if __name__ == '__main__':
    app.run(debug=True)
