import psycopg2
from flask import Flask
app = Flask("__main__")

a= "postgresql://jupyter:ykyb34wrytkwqr13@postgresql-do-do-user-1538085-0.db.ondigitalocean.com:25061/jupyter-pool-2?sslmode=require"

def query():
    conn = psycopg2.connect(a)
    cur_data=conn.cursor()

    sql = """
    select * from "user_transaction" limit 100
                """

    cur_data.execute(sql)
    conn.commit()   
    return  list(cur_data)

@app.route('/')
def hello():
    return query()

@app.route('/an')
def helloAn():
    return "Hello An!"

if __name__ == '__main__':
    app.run(debug=True)