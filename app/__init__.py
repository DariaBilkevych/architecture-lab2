from flask import Flask
from .database import init_db
from .models import db_session

def create_app():
    app = Flask(__name__)
    
    init_db()

    # Import routers
    from .views import book_bp
    app.register_blueprint(book_bp)

    return app
