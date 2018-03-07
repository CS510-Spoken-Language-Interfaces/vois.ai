from flask import Flask,render_template

app = Flask("__name__")



@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/vois.ai/')
def display():
    return render_template('home.html')

@app.route('/vois.ai/recording/')
def record():
    return render_template('recording.html')


if __name__ == '__main__':
	app.run(debug=True)


