# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)


@app.route("/add")
def add_page():
    a = request.args["a"]
    b = request.args["b"]
    val = add(int(a), int(b))
    return str(val)


@app.route("/subtract")
def subtract_page():
    a = request.args["a"]
    b = request.args["b"]
    val = sub(int(a), int(b))
    return str(val)


@app.route("/divide")
def divide_page():
    a = request.args["a"]
    b = request.args["b"]
    val = div(int(a), int(b))
    return str(val)


@app.route("/multiply")
def multiply_page():
    a = request.args["a"]
    b = request.args["b"]
    val = mult(int(a), int(b))
    return str(val)

# FURTHER STUDY - DYNAMIC URL FOR DIFFERENT OPERATORS
# needed a little help with how to reference the dictionary and the url


# key should be str? bc if not a str then its a variable or num
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

# dyanmic part is what you pass into the function has to match exactly the url route - bc...
# for example, url is add, function arg is add, then we call dictionary of add which is add
@app.route("/math/<calcs>")
def calc_page(calcs):
    a = request.args["a"]
    b = request.args["b"]
    res = operators[calcs](int(a), int(b))
    return str(res)
