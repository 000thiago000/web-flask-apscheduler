from app import app, db, jobs, routes
from app.models import Task


jobs.scheduler.start()


functions = []
for job in jobs.scheduler.get_jobs():
    functions.append(str(job.func).split(' ')[1])
functions = sorted(set(functions))

for function in functions:
    exists = Task.query.filter_by(func='__main__:' + function).first()
    if not exists:
        task = Task(name=function, func='__main__:' + function)
        db.session.add(task)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
