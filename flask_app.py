import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# In production, use a secure secret key from environment variables
app.secret_key = os.urandom(24)

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect(url_for('stego_dashboard'))



@app.route('/stego')
def stego_dashboard():
    return render_template('stego.html', name='User')

if __name__ == '__main__':
    # Make sure DB exists
    import db_setup
    db_setup.init_db()
    
    app.run(debug=True, port=5000)
