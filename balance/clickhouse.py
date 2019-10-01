from clickhouse_driver import Client

class ClickhouseDbService:

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

    def query_simple_time(self):
        query = self.client.execute('SELECT now(), version()')
        return "ROW: {0}: {1}".format(type(query), query)