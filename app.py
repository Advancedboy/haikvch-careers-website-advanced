from flask import Flask, render_template, jsonify

from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route('/')
def index():
    jobs_list = load_jobs_from_db()
    return render_template('home.html', jobs=jobs_list)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(load_jobs_from_db())


@app.route('/about')
def about():
    return '<h1>About page</h1>'


@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "<h1>NOT FOUND</h1>", 404
    return render_template('jobpage.html', job=job)


if __name__ == '__main__':
    app.run(debug=True)
