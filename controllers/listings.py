from models.listings import Listings

class ListingsController:
  @get('/:id')
  def get(id, db):
    return Listings.find(db, id)

  @get('/')
  def getAll(db):
    return Listings.findAll(db)

  @patch('/:id')
  def update(id, db, data):
    return Listings.find(db, id).update(db, data)

  @post('/')
  def create(db, data):
    return Listings.create(db, data)