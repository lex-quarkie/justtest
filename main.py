#!/usr/bin/env python3
import connexion
import logging

from app.orm import init_db

logging.basicConfig(level=logging.INFO)
db_session = init_db('sqlite:///app.db')
app = connexion.FlaskApp(__name__)
app.app.config['JSON_SORT_KEYS'] = False
app.add_api('openapi/my_api.yaml')

application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
