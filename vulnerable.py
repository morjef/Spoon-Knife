## just an example of some vulnerable code to generate a code scanning alert
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    conn = sqlite3.connect(':memory:')
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.execute(query)  # Vulnerable to SQL injection
    return {"user": cursor.fetchone()}

if __name__ == '__main__':
    app.run(port=3000)
