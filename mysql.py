#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql


class New(object):
    def __init__(self, host, port, user, passwd, dbname):
        try:
            self.connect = pymysql.connect(**{"host": host, "port": port, "user": user, "password": passwd, "db": dbname, "charset": "utf8mb4", "read_timeout": 3, "write_timeout": 3, "connect_timeout": 3, "cursorclass": pymysql.cursors.DictCursor,})
            self.connect.ping(reconnect=True)
        except pymysql.MySQLError as error:
            print("connect mysql error: %s" % (error))
            exit(0)

    def select(self, sql):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except pymysql.MySQLError as error:
            print("sql: %s\nerr: %s" % (sql, error))
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
            print("sql: %s\nerr: %s" % (sql, error))
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
            print("sql: %s\nerr: %s" % (sql, error))
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
            print("sql: %s\nerr: %s" % (sql, error))
        finally:
            cursor.close()
