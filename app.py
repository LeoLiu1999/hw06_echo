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
    if (request.method == GET):
        args = request.args
        print "request.form:"
        print form
        return render_template("result.html", inputs = form)
    if (request.method == POST):
        form = request.form
        print "request.args:"
        print args
        return render_template("result.html", inputs = args)

if __name__ == "__main__":
    app.debug = True
    app.run()
