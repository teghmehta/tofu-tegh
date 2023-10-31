
from .base import Base

class Applications(Base):
  className = "applications"

  @classmethod
  def findAllByListingId(cls, db, listingId):
    cursor = db.cursor()
    cursor.execute("""
      SELECT * FROM {className} WHERE listing_id = {listingId}
    """.format(className = cls.className, listingId = listingId))

    return [Base(row) for row in cursor.fetchall()]

  @classmethod
  def findAllByCandId(cls, db, candId):
    cursor = db.cursor()
    cursor.execute("""
      SELECT * FROM {className} WHERE candidate_id = {candId}
    """.format(className = cls.className, candId = candId))

    return [Base(row) for row in cursor.fetchall()]
