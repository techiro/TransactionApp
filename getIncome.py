# sqlite3 標準モジュールをインポート
import sqlite3
import pandas
import constants
import logging
import datetime

class DB_Model(object):

    TRANSACTIONS_TABLE = """
        CREATE TABLE IF NOT EXISTS "transactions" (
        "id"	INTEGER NOT NULL,
        "name"	TEXT NOT NULL,
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
        "bank_name"　TEXT,
        "money"	INTEGER
        );
        """
    CHECK_TRANSACTION = "1"
    CHECK_ACCOUNT = "1"
    CHECK_PROFIT = "2"
    DEPOSIT_ACCOUNT = "2"
    ADD_TRANSACTION = "3"
    BACK_MENU = "b"

    TRANSACTION_COLUMN_NAME = "|   '請求先'   |  '締め切り'   |  '金額'"
    ACCOUNT_COLUM_NAME = "| '銀行名' | '金額'"
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
            print("==========================")
            print("取引を確認{:>10}".format(self.CHECK_TRANSACTION))
            print("利益を確認{:>10}".format(self.CHECK_PROFIT))
            print("取引を追加{:>10}".format(self.ADD_TRANSACTION))
            print("MENUに戻る{:>10}".format(self.BACK_MENU))
            print("あなたがしたいことを1,2,3,bで選んでください")
            print("==========================\n")
            response = input()

            if response == self.CHECK_TRANSACTION:
                print("取引一覧を表示します")
                print('{0}様の取引履歴'.format(self.account_name))
                print(self.TRANSACTION_COLUMN_NAME)
                b=self.cursor.execute("SELECT customer,deadline,money FROM transactions WHERE name=?",('{0}'.format(self.account_name),))
                # 中身を全て取得するfetchall()を使って、printする。
                self.print_fech_data(b)

            elif response == self.CHECK_PROFIT:
                print("見込み利益を表示します")
                print('{0}様の見込み利益\n'.format(self.account_name))

                result = self.cursor.execute("SELECT TOTAL(money) FROM transactions WHERE name=?",('{0}'.format(self.account_name),))
                money = int(self.return_list_data(result))
                print('{0} 万円'.format(money))

            elif response == self.ADD_TRANSACTION:
                print("取引を追加します")
                add_id = int(db.table_counted_row("transactions"))
                add_date = str(datetime.datetime.now())
                print("誰に請求しますか？")
                add_distination = input()
                print("締め切りを入力してください")
                add_deadline = input()
                print("金額を入力してください")
                add_money = input()
                # UPDATE_STRING = "INSERT INTO transactions VALUES(" + add_id + 
                insert_transaction = 'INSERT INTO transactions (id, name, date, customer, deadline, money) values (?,?,?,?,?,?)'
                add_data = (
                            add_id,
                            self.account_name,
                            add_date,                            
                            add_distination,
                            add_deadline,
                            add_money
                            )
                self.cursor.execute(insert_transaction, add_data)

                print("""宛先:{distination:>20}様へ\n締め切り：{deadline:>20}\n金額：{money:>20}万円\nを請求します。よろしければ  y  キャンセルする場合は  n  を入力してください""".format(distination=add_distination,deadline=add_deadline,money=add_money))
                
                while True:
                    apply = input()
                    if apply == "y":
                        self.db.commit()
                        print("登録が完了しました。")
                        break
                    elif apply == "n":
                        print("メニューに戻ります")
                        break
                    else:
                        print("よろしければ  y  キャンセルする場合は  n  を入力してください")
                        
            elif response == self.BACK_MENU:
                print("メニューに戻ります")
                break
            
            else:
                print("もう一度入力を行ってください")
            

    def check_account(self):
        print("This is check_account")

        while True:
            print("==========================")
            print("口座を確認{:>10}".format(self.CHECK_ACCOUNT))
            print("口座に入金{:>10}".format(self.DEPOSIT_ACCOUNT))
            print("MENUに戻る{:>10}".format(self.BACK_MENU))
            print("あなたがしたいことを1,2,bで選んでください")
            print("==========================\n")
            response = input()
            if response == self.CHECK_ACCOUNT:
                print("accountを確認します")
                #アカウント名を使用してそのデータのみを表示させる。
                # result = self.cursor.execute("SELECT * FROM account ORDER BY id")
                # self.print_fech_data(result)
                b=self.cursor.execute("SELECT bank_name,money FROM account WHERE name=?",('{0}'.format(self.account_name),))
                # 中身を全て取得するfetchall()を使って、printする。
                print(self.ACCOUNT_COLUM_NAME)
                self.print_fech_data(b)


            elif response == self.DEPOSIT_ACCOUNT:
                print("口座に入金します。〇〇様の口座にいくら入金されますか？")
                print("入金する口座名を入力してください")
                add_account = input()
                # print("いくら入金しますか？")
                # add_money = input()

                current_money = self.cursor.execute("SELECT money FROM account WHERE name=? AND bank_name=?",('{0}'.format(self.account_name),'{0}'.format(add_account)))

                remain_money = self.return_list_data(current_money)
                print("{0} 万円口座にあります。".format(remain_money))
                
                print("いくら入金しますか？")
                add_money = int(input())
                total_money = int(remain_money) + add_money
                self.cursor.execute('UPDATE account SET money=? WHERE name=? and bank_name=?',(total_money,'{0}'.format(self.account_name),'{0}'.format(add_account)))
                
                print("""口座名:{distination:>20}銀行へ\n金額：{money:>20}万円\nを入金します。よろしければ  y  キャンセルする場合は  n  を入力してください""".format(distination=add_account,money=add_money))
                
                while True:
                    apply = input()
                    if apply == "y":
                        self.db.commit()
                        print("登録が完了しました。")
                        break
                    elif apply == "n":
                        print("メニューに戻ります")
                        break
                    else:
                        print("よろしければ  y  キャンセルする場合は  n  を入力してください")
                # self.cursor.execute(insert_transaction, add_data)

                # print("""宛先:{distination:>20}様へ\n締め切り：{deadline:>20}\n金額：{money:>20}万円\nを請求します。よろしければ  y  キャンセルする場合は  n  を入力してください""".format(distination=add_distination,deadline=add_deadline,money=add_money))
                


            elif response == self.BACK_MENU:
                    print("メニューに戻ります")
                    break
            else:
                print("もう一度入力を行ってください")

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
    def print_fech_data(self, fechdata):
        for t_row in fechdata:
            l_row = list(t_row)
            print(l_row)


    def table_counted_row(self, table_N):
        result_t = self.cursor.execute('SELECT count(*) FROM ' + '{0}'.format(table_N))
        
        return self.return_list_data(result_t)

    def return_list_data(self,result_tuple, number=0):
        #第二引数は入力がなければ0がはいる。
        try:
            for row_t in result_tuple:
                count_l = list(row_t)
            return count_l[number]
        except :
            print("errorが発生しました。")



    def disconnect_DB(self):
        self.db.close()


if __name__ == "__main__":    

    db = DB_Model("sample_db.sqlite")
    db.db_init()
    db.account_name = "tanaka"
    # db.check_transaction()
    db.check_account()
    # b = db.table_counted_row("transactions")
    # print(type(b))
    
