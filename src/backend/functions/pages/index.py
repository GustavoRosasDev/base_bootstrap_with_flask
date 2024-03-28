#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app, site_name, render_template


@app.route("/")
def index():
    return render_template(
        template_name_or_list="index.html",
        page_title='Home page',
        page_name='Home',
        site_name=site_name
    )
