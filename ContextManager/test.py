import json
from DBcm import DBContextManager

with open('../db_config.json', 'r') as config:
    db_config = json.load(config)

with DBContextManager(db_config) as cursor:
    print(cursor)
    if cursor:
        _sql = "select ship_arrived, dock_id from shipsregjournalrecord"
        cursor.execute(_sql)
        result = cursor.fetchall()
        print(result)
    else:
        # print('Error')
        raise ValueError("Курсор не создан")
