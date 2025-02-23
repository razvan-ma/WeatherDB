from flask import jsonify, request
from models import Orase, Tari
from utils.db_config import db

def create_city():
    data = request.get_json()
    name = data.get('nume')
    latitude = data.get('lat')
    longitude = data.get('lon')
    country_id = data.get('idTara')

    if not all([name, latitude, longitude, country_id]):
        return jsonify({"error": "Missing required fields"}), 400

    country = db.session.query(Tari).filter(Tari.id == country_id).first()
    if not country:
        return jsonify({"error": "Country with idTara not found"}), 404

    try:
        new_city = Orase(idtara=country_id, nume_oras=name, latitudine=latitude, longitudine=longitude)
        db.session.add(new_city)
        db.session.commit()
        return jsonify({"id": new_city.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

def get_all_cities():
    cities = db.session.execute("SELECT * FROM Orase").fetchall()
    return jsonify([{
        "id": city.id,
        "idTara": city.idtara,
        "nume": city.nume_oras,
        "lat": city.latitudine,
        "lon": city.longitudine
    } for city in cities]), 200

def get_city_by_country(id):
    cities = db.session.execute("SELECT * FROM Orase WHERE idtara = :id", {"id": id}).fetchall()
    return jsonify([{
        "id": city.id,
        "idTara": city.idtara,
        "nume": city.nume_oras,
        "lat": city.latitudine,
        "lon": city.longitudine
    } for city in cities]), 200

def modify_city(id):
    data = request.get_json()
    name = data.get('nume')
    latitude = data.get('lat')
    longitude = data.get('lon')
    country_id = data.get('idTara')

    if not all([name, latitude, longitude, country_id]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        city = db.session.query(Orase).filter(Orase.id == id).first()
        if not city:
            return jsonify({"error": "City not found"}), 404
        
        city.idtara = country_id
        city.nume_oras = name
        city.latitudine = latitude
        city.longitudine = longitude
        db.session.commit()
        return jsonify({"id": city.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

def delete_city(id):
    try:
        city = db.session.query(Orase).filter(Orase.id == id).first()
        if not city:
            return jsonify({"error": "City not found"}), 404
        db.session.delete(city)
        db.session.commit()
        return jsonify({"message": "City deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400