# sqlite3 標準モジュールをインポート
import sqlite3
import pandas
import constants


class DB_Model(object):
    TRANSACTIONS_TABLE = """
        CREATE TABLE IF NOT EXISTS "transactions" (
        "id"	INTEGER NOT NULL,
        "date"	TEXT,
        "customer"	TEXT,
        "deadline"	TEXT,
        "money"	INTEGER,
        PRIMARY KEY("id")
        );
        """
    ACCOUNT_TABLE = """
        CREATE TABLE IF NOT EXISTS "account" (
        "id"	INTEGER,
        "name"	TEXT,
        "money"	INTEGER
        );
        """

    def __init__(self, db_path):
        #DBとAPPをつなげる。

        self.db_path = db_path
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()


    def db_init(self):
        
        print("テーブルを確認なければ生成します。")
    
        self.cursor.execute(self.TRANSACTIONS_TABLE)
        self.cursor.execute(self.ACCOUNT_TABLE)



    def insert_transactions_csv(self, csv_path):

        transactions = pandas.read_csv(csv_path)
        try:
            for i in range(len(transactions)):
                set_data = []
                # pandas で格納されている型は numpy.int64であり、
                # そのままsqlite3に格納すると
                if type(person) == numpy.int64: 
                    person = int(person)
                set_data.append(person)
                self.cursor.execute("INSERT INTO PERSONS values( ?, ?, ?, ?, ?)", set_data)
                print("transactions データベースを更新")
                response = self.cursor.execute("SELECT * FROM transactions;")
        except sqlite3.ProgrammingError:
            print("形式の異なるcsvです。間違ったcsvを挿入してないか確認してください")




if __name__ == "__main__":    

    db = DB_Model("sample_db.sqlite")
    db.db_init()