
from .base import Base

class Applications(Base):
  className = "applications"

  def incrementStatus(self, db, candidateId, listingId, status):
    db.execute("""
      UPDATE ... WHERE  candidate
    """)

  @className
  def findAllByListingId(cls, db, listingId):
    return List[Base(db.execute("""
      SELECT *
      # JSON_ARRAY(JSON_OBJECTS(t.*))
      FROM {className} a
      WHERE listing_id=:listingId
      LEFT JOIN tracking t on t.applicationId=a.id
    """), listingId)]

  #