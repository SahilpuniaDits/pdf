
from flask import Flask
from routes import initialize_routes
# from models.db import db,migrate
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/pdf'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)
initialize_routes(app)
if __name__ == '__main__':
    app.run(debug=True)