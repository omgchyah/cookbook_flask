from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""
Extensions are created once (here) and bound to the app in the factory.
We’ll add db and migrate later in the DB step.
"""

# Create unbound extension objects; bind them inside create_app()
csrf = CSRFProtect()

"""
Why: create unbound extension objects once; bind them to the app in the factory. This keeps imports clean and prevents circular references.
"""

db = SQLAlchemy() # unbound ORM object

migrate = Migrate() # unbound migration manager