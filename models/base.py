from typing import List

class Base:
  className = ""

  @classmethod
  def find(cls, db, id):
    return Base(db.execute("""
      SELECT * FROM {className} WHERE id = ?
    """, id))


  @classmethod
  def findAll(cls, db):
    return List[Base(db.execute("""
      SELECT * FROM {className}
    """))]

  def update(self, db, data):
    db.execute("""
      UPDATE {className} SET {fields} WHERE id = ?
    """.format(
      className = self.className,
      fields = ", ".join(["{} = ?".format(key) for key in data])
    ), *data.values(), self.id)

    for key in data:
      setattr(self, key, data[key])
    return self

  def delete(self, db):
    db.execute("""
      DELETE FROM {className} WHERE id = ?
    """.format(className = self.className), self.id)
    return self

  @classmethod
  def create(cls, db, data):
    db.execute("""
      INSERT INTO {className} DEFAULT VALUES
    """.format(className = cls.className, # .. I did add the data SQL
               ))
    return cls(db.execute("""
      SELECT * FROM {className} ORDER BY id DESC LIMIT 1
    """.format(className = cls.className)))