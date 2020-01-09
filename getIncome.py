# sqlite3 標準モジュールをインポート
import sqlite3
import pandas
import constants


class DB_Model(object):

    TRANSACTIONS_TABLE = """
        CREATE TABLE IF NOT EXISTS "transactions" (
        "id"	INTEGER NOT NULL,
        "name"	TEXT NOT NULL UNIQUE,
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
    CHECK_TRANSACTION = "1"
    CHECK_PROFIT = "2"
    BACK_MENU = "3"

    COLUMN_NAME = """
'id'  |   'date'   |   'customer'   |  'deadline'   |  'money'
            """
    column = []

    def __init__(self, db_path):
        #DBとAPPをつなげる。

        self.db_path = db_path
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()

    def db_init(self):

        print("テーブルを確認なければ生成します。")

        self.cursor.execute(self.TRANSACTIONS_TABLE)
        self.cursor.execute(self.ACCOUNT_TABLE)

    def check_transaction(self):
        print("This is check_transaction")
        while True:
            print("取引一覧を確認　　  　1")
            print("利益を確認    　　　　2")
            print("MENUに戻る　　 　　　 3")
            print("あなたがしたいことを1,2,3で選んでください")
            response = input()

            if response == self.CHECK_TRANSACTION:
                print("取引一覧を表示します")
                print('{0}様の取引履歴'.format(self.account_name))
                print(self.COLUMN_NAME)
                self.cursor.execute("SELECT id,date,customer,deadline,money FROM transactions WHERE name=?",('{0}'.format(self.account_name),))
                print(self.cursor.fetchall())

            elif response == self.CHECK_PROFIT:
                print("見込み利益を表示します")
                print('{0}様の見込み利益'.format(self.account_name))
                self.cursor.execute("SELECT")
                
            elif response == self.BACK_MENU:
                print("メニューに戻ります")
                break
            
            else:
                print("もう一度入力を行ってください")


    def check_account(self):
        print("This is check_account")

        if response == self.CHECK_ACCOUNT:
                print("accountを確認します")
                self.cursor.execute("SELECT * FROM account ORDER BY id")

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
    db.account_name = "tanaka"
    db.check_transaction()
