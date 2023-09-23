from flask import Flask, jsonify, render_template

from database import load_jobs_form_db

app = Flask(__name__)




@app.route("/")
def hello_world():
  jobs = load_jobs_form_db()
  return render_template("home.html", jobs=jobs, company_name="Samir")


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_form_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
