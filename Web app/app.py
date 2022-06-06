from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def start():
    return render_template("start.html")


@app.route('/about')
def index():
    return render_template("about.html")


@app.route('/euler_function', methods=['GET', 'POST'])
def euler_function():
    if request.method == 'POST':
        number = int(request.form.get('num'))

        return render_template("answer.html", res=number - 1)


    else:

        return render_template("euler_function.html", method=request.method)


if __name__ == "__main__":
    app.run(debug=True)
