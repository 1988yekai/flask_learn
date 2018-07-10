# import flask modules
from flask import Flask, render_template, request

# initializing a variable of Flask
app = Flask(__name__)


@app.route('/login')
def mylogin():
    return render_template('login.html')


@app.route('/FlaskTutorial', methods=['POST'])
def success():
    if request.method == 'POST':
        # email = request.form['email']
        parameter = request.form
        if 'email' in parameter:
            email = parameter['email']
        print(type(request.form))
        return render_template('success.html', email=email)
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)
