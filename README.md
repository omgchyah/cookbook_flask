# Flask Recipes CRUD

## A small learning project to build a Flask app with a MySQL backend that manages recipes, ingredients, and a pivot table (recipe_ingredient). We’ll add templates, forms, and validation step by step in later milestones

## Project Goals (scope now)

- Set up a clean Flask project layout.
- Configure environment variables with python-dotenv.
- Prepare SQLAlchemy for MySQL and migrations (no models yet in this step).
- Keep everything simple and explicit.

## 🧰 Tech Stack

### Core

| Package    | Install name           | What it’s for                                              | Why we use it                                               |
| ---------- | ---------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| **Flask**  | `Flask`                | Micro web framework (routing, request/response, templates) | Lightweight and explicit—perfect for learning and CRUD apps |
| **Jinja2** | *(bundled with Flask)* | HTML templating (blocks, inheritance, loops, filters)      | Clean, powerful templating out of the box                   |

### Database & ORM

| Package              | Install name                   | What it’s for                    | Why we use it                                             |
| -------------------- | ------------------------------ | -------------------------------- | --------------------------------------------------------- |
| **Flask-SQLAlchemy** | `Flask-SQLAlchemy`             | SQLAlchemy integration for Flask | Nice defaults, simpler app config                         |
| **SQLAlchemy**       | *(pulled by Flask-SQLAlchemy)* | ORM & DB toolkit                 | The standard for Python ORMs                              |
| **PyMySQL**          | `PyMySQL`                      | MySQL/MariaDB driver             | Pure-Python driver; easy to set up on Windows/macOS/Linux |

### Migrations

| Package           | Install name                | What it’s for                    | Why we use it                                |
| ----------------- | --------------------------- | -------------------------------- | -------------------------------------------- |
| **Flask-Migrate** | `Flask-Migrate`             | Alembic migrations via Flask CLI | Version your schema, evolve safely over time |
| **Alembic**       | *(pulled by Flask-Migrate)* | DB migration engine              | Rock-solid migration layer for SQLAlchemy    |

### Forms & Validation

| Package             | Install name      | What it’s for                         | Why we use it                                        |
| ------------------- | ----------------- | ------------------------------------- | ---------------------------------------------------- |
| **Flask-WTF**       | `Flask-WTF`       | WTForms integration + CSRF protection | Secure forms with simple `validate_on_submit()` flow |
| **WTForms**         | `WTForms`         | Declarative form fields & validators  | Clean form definitions and reusable validators       |
| **email-validator** | `email-validator` | Email field validation                | Required by WTForms’ `Email()` validator             |

### Configuration

| Package           | Install name    | What it’s for                   | Why we use it                               |
| ----------------- | --------------- | ------------------------------- | ------------------------------------------- |
| **python-dotenv** | `python-dotenv` | Load secrets/config from `.env` | Keep credentials out of code and out of Git |

## Project Structure (initial)

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

## Optional quick install

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
