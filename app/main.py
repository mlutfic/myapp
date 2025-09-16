from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )

@app.route("/")
def home():
    return "Halo, ini aplikasi Docker + Database!"

@app.route("/friends", methods=["GET"])
def list_friends():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM friends;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/friends", methods=["POST"])
def add_friend():
    name = request.json.get("name")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO friends (name) VALUES (%s) RETURNING id;", (name,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "name": name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

