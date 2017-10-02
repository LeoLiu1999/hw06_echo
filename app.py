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
    if (request.method == 'GET'):
        inputs = request.args
        print "request.form:"
    if (request.method == 'POST'):
        inputs = request.form
        print "request.args:"
    print inputs
    
    return render_template("result.html", username = inputs['username'], password = inputs['password'])

if __name__ == "__main__":
    app.debug = True
    app.run()
