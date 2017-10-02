from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    print app
    print "request.args:"
    print request.args
    print "request.form:"
    print request.form
    return render_template("form.html")

@app.route("/result")
def result():
    args = request.args
    form = request.form
    print "request.args:"
    print args
    print "request.form:"
    print form
    return render_template("result.html", args = args, form = form)

if __name__ == "__main__":
    app.debug = True
    app.run()
