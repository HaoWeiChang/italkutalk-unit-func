from pymongo.mongo_client import MongoClient


class Mongodb:
    def __init__(self, host: str, db: str, port: int = 27017) -> MongoClient:
        """Create an Mongodb instance.
        :Parameters:
          - `host`: 輸入MongoDB Host(ex:localhost 、db-dev.italkutalk).
          - `port`: 輸入MongoDB Port(ex:27017)
          - `db`: 輸入Client的DB
        """
        self.__client = MongoClient("mongodb://"+host, port)
        self.__db = self.__client.get_database(db)
        pass

    def get_col(self, col_name: str):
        return self.__db.get_collection(col_name)

    def get_info(self) -> None:
        print(self.__client.server_info())
