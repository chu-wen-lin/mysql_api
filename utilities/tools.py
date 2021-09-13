# TODO: define methods to MySQL

import pymysql
from object.database import get_db
from object.schema import Post as Schema


def select_posts(limit,
                 offset,
                 **kwargs):
    sub_query = None
    for key in kwargs.keys():
        if kwargs[key]:
            if not sub_query:
                if key == 'start_time':
                    sub_query = f" WHERE `post_time` >= '{kwargs[key]}'"
                elif key == 'end_time':
                    sub_query = f" WHERE `post_time` <= '{kwargs[key]}'"
                elif key == 'keywords':
                    sub_query = f" WHERE `content` LIKE '%{kwargs[key]}%'"
                else:
                    sub_query = f" WHERE `{key}` = '{kwargs[key]}'"
            else:
                if key == 'start_time':
                    sub_query += f" AND `post_time` >= '{kwargs[key]}'"
                elif key == 'end_time':
                    sub_query += f" AND `post_time` <= '{kwargs[key]}'"
                elif key == 'keywords':
                    sub_query += f" AND `content` LIKE '%{kwargs[key]}%'"
                else:
                    sub_query += f" AND `{key}` = '{kwargs[key]}'"

    with get_db() as connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            columns = ','.join(Schema.__dict__.get("__fields__").keys())
            if sub_query:
                query = f"SELECT {columns} FROM `ts_page_content` {sub_query} limit {limit} offset {offset}"
            else:
                query = f"SELECT {columns} FROM `ts_page_content` limit {limit} offset {offset}"

            cursor.execute(query)

            result = cursor.fetchone()
            while result:
                yield result
                result = cursor.fetchone()

            connection.commit()
