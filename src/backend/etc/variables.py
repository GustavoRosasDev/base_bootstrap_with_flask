#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import Flask

app = Flask(
    __name__,
    template_folder='../../frontend/templates'
)

# Global context variables
app.config['SITE_NAME'] = 'My Website'
site_name = app.config['SITE_NAME']
