from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    # Add logic to handle registration (e.g., save to database)
    return f'User {username} with email {email} registered successfully!'

if __name__ == '__main__':
    app.run(debug=True)
