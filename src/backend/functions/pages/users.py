#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app, site_name, render_template


@app.route("/users/<user_name>")
def users(user_name):
    return render_template(
        template_name_or_list="users.html",
        page_title='User page',
        page_name='User',
        user_name=user_name,
        site_name=site_name
    )
