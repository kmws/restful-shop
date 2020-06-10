import os
import shutil

import flask_migrate
import pytest

from app import init_app, create_root
from tools.config_properties import init_config, get_config
from tools.database import get_db

root_dict = {"email": "root@email.com", "password": "root"}

def delete_all_migrations(current_dir):
    if os.path.exists(current_dir + '/migrations'):
        shutil.rmtree(current_dir + '/migrations')
    if os.path.exists(current_dir + '/api/migrations'):
        shutil.rmtree(current_dir + '/api/migrations')
    if os.path.exists(current_dir + '/api_user/migrations'):
        shutil.rmtree(current_dir + '/api_user/migrations')
    if os.path.exists(current_dir + '/api_admin/migrations'):
        shutil.rmtree(current_dir + '/api_admin/migrations')



@pytest.fixture(scope='session')
def client():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sqlite_file_path = current_dir + '/sqlite.db'
    if os.path.exists(sqlite_file_path):
        os.remove(sqlite_file_path)
    delete_all_migrations(current_dir)

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
    meta = get_db().metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        get_db().session.execute(table.delete())
    get_db().session.commit()
    create_root(root_dict['email'], root_dict['password'])
