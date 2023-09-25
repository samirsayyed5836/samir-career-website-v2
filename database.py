from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_form_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = [] 
    for row in result.all():
     jobs.append(row._mapping)
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs WHERE id = :val").bindparams(val=id))
    
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._mapping


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
            "VALUES (:job_id, :full_name, :email, :linkdin_url, :education, :work_experience, :resume_url)"
        )

        values={'job_id': job_id,
            'full_name':data['full_name'],
            'email':data['email'],
            'linkdin_url':data['linkdin_url'],
            'education':data['education'],
            'work_experience':data['work_experience'],
            'resume_url':data['resume_url']
            } 
        conn.execute (query, values)
        



