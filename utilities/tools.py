# TODO: define methods to MySQL

import pymysql
from object.database import get_db
from object.schema import TypeHintOut as Schema

# from fastapi import Depends
# from sqlalchemy.orm import Session
# from sqlalchemy import and_, desc
# from models import Model


def select_posts(limit: int = 1000,
                 offset: int = 0,
                 **kwargs):

    sub_query = None
    for key in kwargs.keys():  # retrieve parameters excluding limit and offset
        if not sub_query:
            if key == 'start_time':
                sub_query = f" WHERE `post_time` >= '{kwargs[key]}'"
            elif key == 'end_time':
                sub_query = f" WHERE `post_time` <= '{kwargs[key]}'"
            else:
                sub_query = f" WHERE `{key}` = '{kwargs[key]}'"
        else:
            if key == 'start_time':
                sub_query += f" AND `post_time` >= '{kwargs[key]}'"
            elif key == 'end_time':
                sub_query += f" AND `post_time` <= '{kwargs[key]}'"
            else:
                sub_query += f" AND `{key}` = '{kwargs[key]}'"

    with get_db() as connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:

            columns = ','.join(Schema.__dict__.get("__fields__").keys())
            query = f"SELECT {columns} FROM `ts_page_content` {sub_query} ORDER BY `post_time` DESC limit {limit} offset {offset}"
            cursor.execute(query)

            result = cursor.fetchone()
            while result:
                yield result
                result = cursor.fetchone()

            connection.commit()

# class CommonQueryParams:
#     def __init__(self, db: Session, skip: int = 0, limit: int = 10000):
#         self.db = db
#         self.skip = skip
#         self.limit = limit
