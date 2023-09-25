from flask import Flask, jsonify, render_template, request

from database import load_job_from_db, load_jobs_form_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_form_db()
  return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_form_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    
    if job is None:
        return jsonify({"error": "Job not found"}), 404  # Return a 404 response for not found
    
    # Convert the "RowMapping" object to a dictionary
    job_dict = dict(job)
    
    return render_template("jobpage.html" , job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data= request.form
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  
  return render_template("application_submitted.html", application=data, job=job)
  
  


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
