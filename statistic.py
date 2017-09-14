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
        result = self.prepare_data(result)

        return result

    def prepare_data(self, tup):
        result = []
        for data in tup:
            data = list(data)
            data[2] = [float(x) if x.replace(".","").isdigit() else x for x in data[2]]
            data[3] = self.parse_date(data[3])
            result.append(data)
            #for pos,value in enumerate(data[2]):
            #    data[2][pos] = float(value) if value.replace(".","").isdigit() else value
        return result

    def parse_date(self, date):
        date = "{}/{}/{} {}:{}:{}".format(
                date.month,
                date.day,
                date.year,
                date.hour,
                date.minute,
                date.second,
                )
        return date
