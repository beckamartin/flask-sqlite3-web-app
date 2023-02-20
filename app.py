from flask import Flask, render_template, jsonify, request
from database import load_all_from_db, load_three_from_db, load_id_from_db, add_comment_to_db



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  if request.form:
      data = request.form
      add_comment_to_db(data)
    
  return render_template("home.html", comments=load_three_from_db())


@app.route("/api/")
def api_all():
  return jsonify(load_all_from_db())


@app.route("/api/<id>")
def api_id(id):
  return jsonify(load_id_from_db(id))


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)