# Put your app in here.
from operations import add, sub, mult, div

from flask import Flask, request
app = Flask(__name__)

MATH = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<operation>')
def all_routes(operation):
    oper = MATH[operation]
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = oper(a,b)
    return f'{total}'