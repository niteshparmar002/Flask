from flask import render_template, request, redirect, url_for, flash
from config import *
from tasks import add

ROWS_PER_PAGE = 10

@app.route('/add')
def index():
    result = celery_redis.send_task('tasks.add', args=[])
    return f'Task ID: {result.id}'

# Routes
@app.route('/')
def Index():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '', type=str)
    if search_query:
        all_data = User.query.filter(User.name.ilike(f"%{search_query}%")).order_by(User.id.desc()).paginate(page=page, per_page=ROWS_PER_PAGE)
    else:
        all_data = User.query.order_by(User.id.desc()).paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template("index.html", employees = all_data)

@app.route('/insert', methods = ['POST'])
def Insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        my_data = User(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash("Employee Inserted Successfully.")
        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def Update():
    if request.method == 'POST':
        my_data = User.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        db.session.commit()
        flash("Employee Updated Successfully.")
        return redirect(url_for('Index'))
    if request.method == 'GET':
        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def Delete(id):
    my_data = User.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully.")
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(debug=True)



## celery implement  1 lac enteries
