from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..extensions import db
from ..models import Ingredient
from ..forms import IngredientForm

ingredients_bp = Blueprint("ingredients", __name__)

@ingredients_bp.route("/")
def list_ingredients():
    items = Ingredient.query.order_by(Ingredient.name).all()
    return render_template("ingredients/list.html", items = items)

@ingredients_bp.route("/create", methods=["GET", "POST"])
def create_ingredient():
    form = IngredientForm()
    if form.validate_on_submit():
        db.session.add(Ingredient(name=form.name.data.strip()))
        db.session.commit()
        flash("Ingredient created", "success")
        return redirect(url_for("ingredients.list_ingredients"))
    return render_template("ingredients/create.html", form=form)

@ingredients_bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_ingredient(id):
    item = Ingredient.query.get_or_404(id)
    form = IngredientForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data.strip()
        db.session.commit()
        flash("Ingredient updated", "success")
        return redirect(url_for("ingredients.list_ingredients"))
    return render_template("ingredients/edit.html", form=form, item=item)

@ingredients_bp.route("<int:id>/delete", methods=["POST"])
def delete_ingredient(id):
    item = Ingredient.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash("Ingredient deleted", "info")
    return redirect(url_for("ingredients.list_ingredients"))