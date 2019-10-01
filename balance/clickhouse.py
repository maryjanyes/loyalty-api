import sys

from clickhouse_driver import Client

class ClickDbService:

    def __init__(self):
        self.client = Client(
            'localhost',
            user='admin',
            password='0000',
            secure=True,
            verify=False,
            database='balance_holding',
            compression=True
        )

    def seeders(self):
        self.client.execute('CREATE DATABASE balance_holding')
        self.client.execute('CREATE TABLE balance_holding.balance (' +
           'timestamp Date DEFAULT now(),' +
           'balance_sum Int64' +
        ') ENGINE = Memory')
        self.tx_seeders()

    def tx_seeders(self):
        self.client.execute('INSERT INTO balance_holding.balance (balance_sum) VALUES (100)')
        self.client.execute('INSERT INTO balance_holding.balance (balance_sum) VALUES (200)')

    def insert_tx_sum_by_timestamp(self, sum):
        self.client.execute('INSERT INTO balance_holding.balance (balance_sum) VALUES (' + sum + ')')
        return True

    def query_simple_time(self):
        query = self.client.execute('SELECT now(), version()')
        return "ROW: {0}: {1}".format(type(query), query)

click_house_db = ClickDbService()

if __name__ == "__main__":

    if len(sys.argv) > 1:
        is_seeder = sys.argv[1]
        if is_seeder:
            click_house_db.seeders()
