from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Minsk, Belarus',
        'salary': '$12,000'
    },
    {
        'id': 2,
        'title': 'Marketer',
        'location': 'Molodechno, Belarus',
        'salary': '$1000'
    },
    {
        'id': 3,
        'title': 'Frontend',
        'location': 'remote',
        'salary': '$10,000'
    },
    {
        'id': 4,
        'title': 'Low-level software engineer',
        'location': 'NYC, United States',
        'salary': '$24,000'
    }
]


@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS, company_name='Haikvch')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)
