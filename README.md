# Flask Recipes CRUD

## A small learning project to build a Flask app with a MySQL backend that manages recipes, ingredients, and a pivot table (recipe_ingredient). We’ll add templates, forms, and validation step by step in later milestones

## Project Goals (scope now)

- Set up a clean Flask project layout.
- Configure environment variables with python-dotenv.
- Prepare SQLAlchemy for MySQL and migrations (no models yet in this step).
- Keep everything simple and explicit.

## Tech Stack (current)

- Python 3.10+
- Flask (app + routing)
- Jinja2 (templates)
- SQLAlchemy + PyMySQL (ORM + MySQL driver)
- Flask-Migrate (Alembic migrations)
- Flask-WTF / WTForms (forms + validation; installed now, used later)
- python-dotenv (environment variables)

## Project Structure (initial)

    ```
    your-repo/
    ├─ README.md
    ├─ requirements.txt
    ├─ .env.example          # Template for env vars (do not include secrets)
    ├─ src/
    │  └─ app/
    │     ├─ __init__.py     # app factory (to be filled in later)
    │     ├─ config.py       # config from env (to be filled in later)
    │     ├─ extensions.py   # db, migrate, csrf setup (later)
    │     ├─ models.py       # empty for now
    │     ├─ forms.py        # empty for now
    │     ├─ blueprints/     # core, recipes, ingredients (later)
    │     ├─ templates/      # base.html, pages (later)
    │     └─ static/         # css/js/img (later)
    └─ scripts/
    └─ (optional)         # seed or helpers (later)
    ```

## Requirements

### Create requirements.txt:

- flask
- python-dotenv
- flask-wtf
- wtforms
- email-validator
- flask-sqlalchemy
- pymysql
- flask-migrate

## Optional quick install:

    ```bash
    python -m venv .venv
    ```

    ```bash
    # Windows
    . .venv/Scripts/Activate.ps1
    ```

    ```bash
    # macOS/Linux
    source .venv/bin/activate
    ```

    ```bash
    pip install -U pip
    pip install -r requirements.txt
    ```
