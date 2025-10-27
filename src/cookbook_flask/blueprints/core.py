from flask import Blueprint, render_template, flash, redirect, url_for

core_bp = Blueprint("core", __name__)

# Why: at least one route so you can see something on /.
@core_bp.route("/")
def home():
    return render_template("home.html", raw="<strong>bold</strong>")

@core_bp.route("/demo-flash")
def demo_flash():
    flash("Saved successfully!", "success")  # message + category
    return redirect(url_for("core.home"))