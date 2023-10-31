from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_cors import CORS
from models.listings import Listings
from models.candidate import Candidate
from models.applications import Applications
from models.tracking import Tracking
from models.base import Base
db = MySQL(cursorclass=DictCursor)

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = '34839md3!Key.!'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'tofu_service'

db.init_app(app)
# Listings Routes
@app.route('/listings/<id>', methods=['GET'])
def get_listing(id):
    try:
        listing = Listings.find(db.get_db(), id)
        if not listing:
            return jsonify({"message": "Listing not found"}), 404
        return listing.to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/listings', methods=['GET'])
def get_all_listings():
    try:
        listings = Listings.findAll(db.get_db())
        return jsonify([j.__dict__ for j in listings]), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/listings/<id>', methods=['PATCH'])
def update_listing(id):
    try:
        data = request.get_json()
        listing = Listings.find(db.get_db(), id)
        if not listing:
            return jsonify({"message": "Listing not found"}), 404
        return listing.update(db.get_db(), data, "listings").to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/listings', methods=['POST'])
def create_listing():
    try:
        data = request.get_json()
        return Listings.create(db.get_db(), data).to_dict(), 201
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

# Candidate Routes
@app.route('/candidates/<id>', methods=['GET'])
def get_candidate(id):
    try:
        candidate = Candidate.find(db.get_db(), id)
        if not candidate:
            return jsonify({"message": "Candidate not found"}), 404
        return candidate.to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/candidates', methods=['GET'])
def get_all_candidates():
    try:
        candidates = Candidate.findAll(db.get_db())
        return jsonify([j.__dict__ for j in candidates]), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/candidates/<id>', methods=['PATCH'])
def update_candidate(id):
    data = request.get_json()
    candidate = Candidate.find(db.get_db(), id)
    if not candidate:
        return jsonify({"message": "Candidate not found"}), 404
    return candidate.update(db.get_db(), data, "candidates").to_dict(), 200

@app.route('/candidates', methods=['POST'])
def create_candidate():
    try:
        data = request.get_json()
        return Candidate.create(db.get_db(), data).to_dict(), 201
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

# Applications Routes
@app.route('/applications/<id>', methods=['GET'])
def get_application(id):
    try:
        application = Applications.find(db.get_db(), id)
        if not application:
            return jsonify({"message": "Application not found"}), 404
        return application.to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications/listings/<id>', methods=['GET'])
def get_all_applications_by_listings(id):
    try:
        return jsonify([j.__dict__ for j in Applications.findAllByListingId(db.get_db(),id)]), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications/history/<id>', methods=['GET'])
def get_all_application_history(id):
    try:
        return jsonify([j.__dict__ for j in Tracking.findAllByAppId(db.get_db(),id)]), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications', methods=['GET'])
def get_all_applications():
    try:
        return jsonify([j.__dict__ for j in Applications.findAll(db.get_db())]), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications/<id>', methods=['PATCH'])
def update_application(id):
    try:
        data = request.get_json()
        application = Applications.find(db.get_db(), id)
        if not application:
            return jsonify({"message": "Application not found"}), 404
        return application.update(db.get_db(), data, "applications").to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications/<id>/status', methods=['PATCH'])
def update_application_status(id):
    try:
        status = request.get_json().get('status')
        application = Applications.find(db.get_db(), id)
        previous_status = application.status
        application.update(db.get_db(), {"status": status}, "applications")
        Tracking.create(db.get_db(), {
            "previous_status": previous_status,
            "status": status,
            "application_id": application.id
        })
        return application.to_dict(), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

@app.route('/applications', methods=['POST'])
def create_application():
    try:
        data = request.get_json()
        return Applications.create(db.get_db(), data).to_dict(), 201
    except Exception as e:
        print(e)
        return jsonify({"message": f"Internal Server Error {repr(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
