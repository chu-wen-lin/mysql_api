# TODO: connect MySQL
import os
import pymysql


def get_db():

    return pymysql.connect(host=os.getenv("db_host"),
                           user=os.getenv("db_user"),
                           password=os.getenv("db_password"),
                           database='forum_data')
