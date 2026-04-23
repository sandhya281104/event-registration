from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("CI/CD demo run")
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)