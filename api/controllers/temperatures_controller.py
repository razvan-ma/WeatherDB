from flask import jsonify, request
from models import Temperaturi, Orase
from utils.db_config import db

def create_temperature():
    data = request.get_json()
    temperature = data.get('valoare')
    city_id = data.get('idOras')

    if not all([temperature, city_id]):
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        new_temperature = Temperaturi(idoras=city_id, valoare=temperature)
        db.session.add(new_temperature)
        db.session.commit()
        return jsonify({"id": new_temperature.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
def get_all_temperatures():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    from_date = request.args.get('from')
    until_date = request.args.get('until')
    
    query = db.session.query(Temperaturi).join(Orase, Temperaturi.idoras == Orase.id)
    if lat is not None:
        query = query.filter(Orase.latitudine == lat)
    if lon is not None:
        query = query.filter(Orase.longitudine == lon)
    if from_date is not None:
        query = query.filter(Temperaturi.timestamp >= from_date)
    if until_date is not None:
        query = query.filter(Temperaturi.timestamp <= until_date)
    
    results = query.all()

    return jsonify([{
        "id": temperature.id,
        "valoare": temperature.valoare,
        "timestamp": temperature.timestamp,
    } for temperature in results]), 200

def get_temperature_by_city(id):
    from_date = request.args.get('from')
    until_date = request.args.get('until')

    query = db.session.query(Temperaturi).filter(Temperaturi.idoras == id)

    if from_date is not None:
        query = query.filter(Temperaturi.timestamp >= from_date)
    if until_date is not None:
        query = query.filter(Temperaturi.timestamp <= until_date)

    results = query.all()

    return jsonify([{
        "id": temperature.id,
        "valoare": temperature.valoare,
        "timestamp": temperature.timestamp,
    } for temperature in results]), 200

def get_temperature_by_country(id):
    from_date = request.args.get('from')
    until_date = request.args.get('until')

    query = db.session.query(Temperaturi).join(Orase, Temperaturi.idoras == Orase.id).filter(Orase.idtara == id)

    if from_date is not None:
        query = query.filter(Temperaturi.timestamp >= from_date)
    if until_date is not None:
        query = query.filter(Temperaturi.timestamp <= until_date)

    results = query.all()

    return jsonify([{
        "id": temperature.id,
        "valoare": temperature.valoare,
        "timestamp": temperature.timestamp,
    } for temperature in results]), 200

def modify_temperature(id):
    data = request.get_json()
    new_value = data.get('valoare')

    if new_value is None:
        return jsonify({"error": "Missing required field 'valoare'"}), 400

    try:
        temperature = db.session.query(Temperaturi).filter(Temperaturi.id == id).first()

        if not temperature:
            return jsonify({"error": "Temperature record not found"}), 404

        temperature.valoare = new_value
        db.session.commit()

        return jsonify({
            "id": temperature.id,
            "valoare": temperature.valoare,
            "timestamp": temperature.timestamp
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
def delete_temperature(id):
    try:
        temperature = db.session.query(Temperaturi).filter(Temperaturi.id == id).first()
        if not temperature:
            return jsonify({"error": "Temperature not found"}), 404
        db.session.delete(temperature)
        db.session.commit()
        return jsonify({"message": "Temperature deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    