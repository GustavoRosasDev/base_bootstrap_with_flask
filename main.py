#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.backend.manager import app
# noinspection PyUnresolvedReferences
from src.backend.function_manager import *


if __name__ == "__main__":
    app.run(debug=True)

    # To deploy: Use Render (free).
    # Live: https://base-flask.onrender.com/
