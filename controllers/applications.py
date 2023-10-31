from models.applications import Applications
from models.tracking import Tracking

class ApplicationsController:
  @get('/:id')
  def get(id, db):
    return Applications.find(db, id)

  @get('/')
  def getAll(db, filter):
    #  validation on filter
    if 'listingId' in filter:
      return Applications.findAllByListingId(db, filter['listingId'])

    return Applications.findAll(db)

  @patch('/:id')
  def update(id, db, data):
    # validation (prevent status being passed in because we have a dedicated route for that below)

    return Applications.find(db, id).update(db, data)

  @patch('/:id/status')
  def updateStatus(id, db, status):
    application = Applications.find(db, id)
    previousStatus = application.status
    application.update(db, {
      "status": status
    })
    Tracking.create(db, {
      "previousStatus": previousStatus,
      "status": status,
      "application_id": application.id
    })

    return application


  @post('/')
  def create(db, data):
    #
    # {
    #   resume,
    #   listing_id,
    #   candidate_id
    # }

    return Applications.create(db, data)