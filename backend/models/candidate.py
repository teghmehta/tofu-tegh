
from .base import Base
from .applications import Applications

class Candidate(Base):
  className = "candidates"


  @classmethod
  def find(cls, db, id):
    can = super().find(db, id)
    can.applications = [app.__dict__ for app in Applications.findAllByCandId(db, id)]
    return can
