from flask import Flask, render_template, make_response, request
from flask.json import jsonify
from model.db_module import Database

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("hello.html", value="home")

@app.route('/api', methods=["GET"])
def hello_world():
    return make_response(jsonify({"id":"1","name":"dongwon"}),200)

@app.route('/home')
def home():
    return "hello home","200"

@app.route('/admin', methods=["POST"])
def admin_update():
    body = request.get_json()
    id = body.get("admin_id")
    name = body.get("admin_name")
    db_class = Database()
    query = f"insert into admin(admin_id, admin_name) values ({id},'{name}')"
    db_class.execute(query)
    db_class.commit()

    return "clear", 200

@app.route('/admin/<id>', methods=["GET"])
def read_admin(id):

    db_class = Database()
    query = f"select * from admin where admin_id={id}"
    print(query)
    row= db_class.executeAll(query)
    print(row)
    return make_response(jsonify(row),200)

