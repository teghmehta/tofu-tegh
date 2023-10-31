from models.candidate import Candidate

class CandidateController:
  @get('/:id')
  def get(id, db):
    return Candidate.find(db, id)

  @get('/')
  def getAll(db):
    return Candidate.findAll(db)

  @patch('/:id')
  def update(id, db, data):
    return Candidate.find(db, id).update(db, data)

  @post('/')
  def create(db, data):
    return Candidate.create(db, data)