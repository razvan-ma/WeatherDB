from flask import Blueprint
from controllers.country_controller import get_all_countries, create_country, modify_country, delete_country

country_bp = Blueprint('countries', __name__)

country_bp.route('/', methods=['GET'])(get_all_countries)
country_bp.route('/', methods=['POST'])(create_country)
country_bp.route('/<int:id>', methods=['PUT'])(modify_country)
country_bp.route('/<int:id>', methods=['DELETE'])(delete_country)