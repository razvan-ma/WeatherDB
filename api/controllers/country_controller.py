from flask import jsonify, request
from models import Tari
from utils.db_config import db

def get_all_countries():
    countries = db.session.execute("SELECT * FROM Tari").fetchall()
    return jsonify([{
        "id": country.id,
        "nume": country.nume_tara,
        "lat": country.latitudine,
        "lon": country.longitudine
    } for country in countries]), 200

def create_country():
    data = request.get_json()
    name = data.get('nume')
    latitude = data.get('lat')
    longitude = data.get('lon')

    if not all([name, latitude, longitude]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Create a new Tari instance
        new_country = Tari(nume_tara=name, latitudine=latitude, longitudine=longitude)
        db.session.add(new_country)
        db.session.commit()
        return jsonify({"id": new_country.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of an error
        return jsonify({"error": str(e)}), 409

def modify_country(id):
    data = request.get_json()
    name = data.get('nume')
    latitude = data.get('lat')
    longitude = data.get('lon')
    if not all([name, latitude, longitude]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        new_country = Tari(nume_tara=name, latitudine=latitude, longitudine=longitude)
        db.session.add(new_country)
        db.session.commit()
        return jsonify({"id": new_country.id}), 200
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of an error
        return jsonify({"error": str(e)}), 404

def delete_country(id):
    try:
        country = db.session.query(Tari).filter(Tari.id == id).first()
        if country is None:
            return jsonify({"error": "Country not found"}), 404
        db.session.delete(country)
        db.session.commit()
        return jsonify({"message": "Country deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400