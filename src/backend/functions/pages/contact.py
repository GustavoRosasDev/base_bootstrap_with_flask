#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app, site_name, render_template


@app.route("/contact")
def contact():
    return render_template(
        template_name_or_list="contact.html",
        page_title='Contact page',
        page_name='Contact',
        site_name=site_name
    )
