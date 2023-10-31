
from .base import Base

class Tracking(Base):
  className = "tracking"

  @classmethod
  def findAllByAppId(cls, db, application_id):
    cursor = db.cursor()
    cursor.execute("""
      SELECT * FROM {className} WHERE application_id = {application_id}
    """.format(className = cls.className, application_id = application_id))
    return [Base(row) for row in cursor.fetchall()]
