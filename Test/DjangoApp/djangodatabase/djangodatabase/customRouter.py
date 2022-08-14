import random
from django.db import connections
from django.db.utils import OperationalError


class databaseRouter:
    def db_for_read(self, model, **hints):
        db_connection = connections['default']
        try:
            c = db_connection.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True
        if connected:
            return random.choice(['default','backup1'])
        else:
            return random.choice(['backup1'])

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True
    
    def allow_migrate(db, app_label, model_name=None, **hints):
        return True