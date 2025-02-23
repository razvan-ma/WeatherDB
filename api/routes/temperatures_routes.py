from flask import Blueprint
from controllers.temperatures_controller import create_temperature, get_all_temperatures, get_temperature_by_city, get_temperature_by_country, modify_temperature, delete_temperature

temperature_bp = Blueprint('temperatures', __name__)

temperature_bp.route('/', methods=['GET'])(get_all_temperatures)
temperature_bp.route('/', methods=['POST'])(create_temperature)
temperature_bp.route('/cities/<int:id>', methods=['GET'])(get_temperature_by_city)
temperature_bp.route('/countries/<int:id>', methods=['GET'])(get_temperature_by_country)
temperature_bp.route('/<int:id>', methods=['PUT'])(modify_temperature)
temperature_bp.route('/<int:id>', methods=['DELETE'])(delete_temperature)