from .extensions import db
# ^ We import the SQLAlchemy() instance created in extensions.py.
#   'db' exposes db.Model, Column, relationship, etc.

# ---------- Pivot (association) table with extra data ----------
class RecipeIngredient(db.Model):
    """
    Association (pivot) between Recipe and Ingredient.
    Uses a COMPOSITE PRIMARY KEY (recipe_id + ingredient_id) so:
    - the pair is unique (no duplicate ingredient in the same recipe)
    - we can attach extra fields (quantity, unit)
    """
    
    __tablename__ = "recipe_ingredient"
    
    # Composite primary key (two FKs also act as PKs)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), primary_key=True)
    
    # Extra data on the relationship
    quantity = db.Column(db.Float, nullable=False, default=0.0)
    unit = db.Column(db.String(32), nullable=True)
    
    # Optional: relationships back to parents (handy for joins/ORM navigation)
    recipe = db.relationship("Recipe", back_populates="recipe_ingredients")
    ingredient = db.relationship("Ingredient", back_populates="ingredient_recipes")
    
    # Note: no 'id' column. The PK is (recipe_id, ingredient_id).
    
class Recipe(db.Model):
    """
    A recipe with a title and description.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
        # 1) Low-level link to the association rows (lets you access quantity/unit)
    recipe_ingredients = db.relationship(
        "RecipeIngredient",
        back_populates="recipe",
        cascade="all, delete-orphan",
        lazy="select",              # load when accessed; common default
    )

    # 2) High-level "secondary" relationship to Ingredients (convenient list)
    ingredients = db.relationship(
        "Ingredient",
        secondary="recipe_ingredient",   # table name of the pivot
        back_populates="recipes",
        lazy="select",
    )

class Ingredient(db.Model):
    """
    A unique ingredient by name.
    """
    
    __tablename__ = "ingredient"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    
    # Mirror of Recipe.recipe_ingredients
    ingredient_recipes = db.relationship(
        "RecipeIngredient",
        back_populates="ingredient",
        cascade="all, delete-orphan",
        lazy="select",
    )

    # Mirror of Recipe.ingredients (the convenient many-to-many)
    recipes = db.relationship(
        "Recipe",
        secondary="recipe_ingredient",
        back_populates="ingredients",
        lazy="select",
    )
    
    
