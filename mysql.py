#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql


class New(object):
    def __init__(self, host="localhost", port=3306, user="root", passwd="passwd", dbname="user"):
        try:
            self.connect = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset="utf8mb4", read_timeout=3, write_timeout=3, connect_timeout=3, cursorclass=pymysql.cursors.DictCursor)
            self.connect.ping(reconnect=True)
        except pymysql.MySQLError as error:
            print(error)
            exit(0)

    def select(self, sql):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except pymysql.MySQLError as error:
            print(error)
            return {}
        finally:
            cursor.close()

    def insert(self, sql):
        cursor = self.connect.cursor()
        try:
            self.connect.begin()
            cursor.execute(sql)
            self.connect.commit()
        except pymysql.MySQLError as error:
            self.connect.rollback()
            print(error)
        finally:
            cursor.close()

    def update(self, sql):
        cursor = self.connect.cursor()
        try:
            self.connect.begin()
            cursor.execute(sql)
            self.connect.commit()
        except pymysql.MySQLError as error:
            self.connect.rollback()
            print(error)
        finally:
            cursor.close()

    def delete(self, sql):
        cursor = self.connect.cursor()
        try:
            self.connect.begin()
            cursor.execute(sql)
            self.connect.commit()
        except pymysql.MySQLError as error:
            self.connect.rollback()
            print(error)
        finally:
            cursor.close()
