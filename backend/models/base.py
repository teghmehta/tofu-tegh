from flask import jsonify
class Base:
  className = ""

  def __init__(self, data):
    for key in data:
      setattr(self, key, data[key])


  @classmethod
  def find(cls, db, id):
    cursor = db.cursor()
    cursor.execute(f"""
      SELECT * FROM {cls.className} WHERE id = {id}
    """.format(className = cls.className, id = id))
    return Base(cursor.fetchone())


  @classmethod
  def findAll(cls, db):
    cursor = db.cursor()
    cursor.execute(f"""
      SELECT * FROM {cls.className}
    """)
    return [cls(row) for row in cursor.fetchall()]


  def update(self, db, data, className):
    sets = [
        f"{key} = '{value}'" for key, value in data.items()
      ]
    db.cursor().execute(f"""
      UPDATE {className} SET {
        ", ".join(sets)
      } WHERE id = {self.id}
    """)
    db.commit()

    for key in data:
      setattr(self, key, data[key])
    return self

  def delete(self, db, className):
    cursor = db.cursor()
    cursor.execute("""
      DELETE FROM {className} WHERE id = ?
    """.format(className = className), self.id)

    db.commit()
    return self

  @classmethod
  def create(cls, db, data):
    cursor = db.cursor()
    fields = ", ".join([key for key in data])
    values = ", ".join([f"'{value}'" for value in data.values()])
    cursor.execute(f"""
      INSERT INTO {cls.className} ({fields}) VALUES ({values})
    """)
    db.commit()

    lastRowId = cursor.lastrowid
    return cls.find(db, lastRowId)

  def to_dict(self):
    return jsonify(self.__dict__)
