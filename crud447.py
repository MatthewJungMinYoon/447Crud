import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

def get_stud(stud_id):
	conn = get_db_connection()
	stud = conn.execute('SELECT * FROM studs WHERE id = ?',
						(stud_id,)).fetchone()
	
	conn.close()
	if stud is None:
		abort(404)
	return stud

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
	conn = get_db_connection()
	studs = conn.execute('SELECT * FROM studs').fetchall()
	conn.close()
	return render_template('index.html', studs=studs)

@app.route('/<int:stud_id>')
def stud(stud_id):
	stud = get_stud(stud_id)
	return render_template('stud.html', stud=stud)

@app.route('/create', methods=('GET', 'POST'))
def create():  
	if request.method == 'POST':
		name = request.form['name']
		studID = request.form['id']
		marks = request.form['marks']

		if not name:
			flash('Name is required')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO studs (name, id, marks) VALUES (?, ?, ?)',
						(name, studID, marks))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))

	return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
	stud = get_stud(id)

	if request.method == 'POST':
		name = request.form['name']
		studID = request.form['id']
		marks = request.form['marks']

		if not name:
			flash('Name is required')
		else:
			conn = get_db_connection()
			conn.execute('UPDATE studs SET name = ?, id = ?, marks = ?',
						(name, studID, marks))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))
	return render_template('edit.html', stud=stud)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    stud = get_stud(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was deleted!'.format(stud['name']))
    return redirect(url_for('index'))