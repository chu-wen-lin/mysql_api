# TODO: connect MySQL
import os
import pymysql


def get_db():

    return pymysql.connect(host=os.getenv("db_host"),
                           user=os.getenv("user"),
                           password=os.getenv("password"),
                           database='forum_data')
