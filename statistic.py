from decouple import config
import psycopg2

class DB:
    def __connect(self):
         return psycopg2.connect(host=config('host'), user=config('user'), password=config('password'), dbname=config('dbname'))

    def save(self, query):
        conn = self.__connect()
        cur = conn.cursor()
        self.cursor.execute(query)
        conn.commit()
        cur.close()
        return cur

    def get(self, query):
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

class Statistic:
    def get(self):
        db = DB()
        result = db.get("""SELECT * FROM cpu_usage""")
        return result


