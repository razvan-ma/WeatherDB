import flask 
from utils.db_config import db

from routes.country_routes import country_bp
from routes.city_routes import city_bp
from routes.temperatures_routes import temperature_bp
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/weatherdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(country_bp, name="country", url_prefix='/api/countries')
app.register_blueprint(city_bp, name="city", url_prefix='/api/cities')
app.register_blueprint(temperature_bp, name="temperature", url_prefix='/api/temperatures')
# Print all routes
with app.app_context():
    for rule in app.url_map.iter_rules():
        print(f"Endpoint: {rule.endpoint}, Route: {rule}, Methods: {rule.methods}")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
