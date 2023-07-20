from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id))
        row = result.all()
        if len(row) == 0:
            return None
        else:
            return row[0]._mapping


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO applications (job_id, full_name, email, linked_url, education, work_experience, "
                          "resume_url) VALUES (:job_id, :full_name, :email, :linked_url, :education, :experience, "
                          ":resume_url)").bindparams(job_id=job_id, full_name=data['full_name'], email=data['email'],
                                                     linked_url=data['linked_url'], education=data['education'],
                                                     experience=data['work_experience'], resume_url=data['resume_url']))
