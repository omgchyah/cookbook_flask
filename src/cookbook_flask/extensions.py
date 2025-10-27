from flask_wtf import CSRFProtect

"""
Extensions are created once (here) and bound to the app in the factory.
We’ll add db and migrate later in the DB step.
"""

# Create unbound extension objects; bind them inside create_app()
csrf = CSRFProtect()