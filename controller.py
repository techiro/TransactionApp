import getIncome
import sys
class DB_Controller(object):
    CHECK_TRANSACTION = "1"
    CHECK_ACCOUNT = "2"
    END_MENU = "3"
    def __init__(self, DB_Model):
        print("hello this is controller_init_")
        self.DB_Model = DB_Model

    def menu(self):
        print("Transaction Appを起動しました")

        while True:
            print("帳簿を確認する    1")
            print("口座を確認する    2")
            print("APPを終了する　　 3")
            print("あなたがしたいことを1か2で選んでください")
            response = input()

            if response == self.CHECK_TRANSACTION:
                print("transactionを確認します")
                # self.check_transaction()
                

            elif response == self.CHECK_ACCOUNT:
                print("accountを確認します")
                # self.check_account()

            elif response == self.END_MENU:
                print("システムを終了します")
                sys.exit()
            
            else:
                print("もう一度入力を行ってください")


if __name__ == "__main__":
    db = getIncome.DB_Model("sample_db.sqlite")
    controller = DB_Controller(db)
    controller.menu()