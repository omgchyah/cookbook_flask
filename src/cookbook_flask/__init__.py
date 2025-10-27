from flask import Flask
from .config import Config # loads env + settings
from .extensions import csrf, db, migrate # extension objects (unbound)
from .blueprints.core import core_bp  # your first routes
from . import models

"""
Factory (create_app): builds a fresh app on demand (clean for tests/CLI).
app.config.from_object(Config): centralizes settings in one place.
csrf.init_app(app): turns on CSRF site-wide (we’ll need it for forms).
Blueprint: keeps routes modular and organized.
"""

"""
Why: After binding, any model that imports db will use this app’s database connection. migrate hooks into SQLAlchemy to generate/apply schema changes later.
"""

def create_app():
    app = Flask(__name__) # create the Flask app
    app.config.from_object(Config) # apply configuration
    
    # Bind extensions
    csrf.init_app(app) # bind CSRF to this app instance
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Blueprints Routes
    app.register_blueprint(core_bp) # mount routes at "/"
    from .blueprints.ingredients import ingredients_bp # ← import local
    app.register_blueprint(ingredients_bp, url_prefix="/ingredients") # ← registro
    
    
    return app

# Expose an app variable for convenience (CLI can import it)
app = create_app()
    