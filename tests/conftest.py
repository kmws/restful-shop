import os
import shutil

import flask_migrate
import pytest

from app import init_app
from tools.config_properties import init_config
from tools.database import get_db


@pytest.fixture(scope='session')
def client():
    print("HELLO CLIENT")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sqlite_file_path = current_dir + '/sqlite.db'

    if os.path.exists(sqlite_file_path):
        os.remove(sqlite_file_path)
    if os.path.exists(current_dir + '/api/migrations'):
        shutil.rmtree(current_dir + '/api/migrations')

    init_config(test_db_path="sqlite:////" + sqlite_file_path)
    app = init_app()
    open(sqlite_file_path, 'a').close()
    with app.app_context():
        flask_migrate.init()
        flask_migrate.migrate()
        flask_migrate.upgrade()
    yield app.test_client()


@pytest.fixture(autouse=True)
def clean_db():
    print("HELLO DB")
    meta = get_db().metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        get_db().session.execute(table.delete())
    get_db().session.commit()
