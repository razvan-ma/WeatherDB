from flask import Blueprint
from controllers.city_controller import get_all_cities, create_city, modify_city, delete_city, get_city_by_country

city_bp = Blueprint('countries', __name__)

city_bp.route('/', methods=['GET'])(get_all_cities)
city_bp.route('/', methods=['POST'])(create_city)
city_bp.route('/country/<int:id>', methods=['GET'])(get_city_by_country)
city_bp.route('/<int:id>', methods=['PUT'])(modify_city)
city_bp.route('/<int:id>', methods=['DELETE'])(delete_city)