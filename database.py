from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://jmv0s8zbk3miqywy2uf4:pscale_pw_EG09lvKrpOhi9rqJ1PhgtJr77XdE9qFVw6tc7cSP8N3@eu-central.connect.psdb.cloud/joviancareers?charset=utf8mb4"

                       
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_all_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM comments"))
    return [dict(zip(result.keys(), row)) for row in result.fetchall()]


def load_three_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM comments ORDER BY id DESC LIMIT 3"))
    return [dict(zip(result.keys(), row)) for row in result.fetchall()]


def load_id_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM comments WHERE id = :val"),
                          {"val": id})
    rows = result.fetchall()

    if len(rows) == 0:
      return None

    else:
      row_dict = {}
      for i, col in enumerate(result.keys()):
        row_dict[col] = rows[0][i]
      return row_dict
    

def add_comment_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO comments (title, full_name, text_comment) VALUES (:title, :full_name, :text_comment)")
    conn.execute(query, {
                "title": data["title"],
                "full_name": data["full_name"],
                "text_comment": data["text_comment"]
    })