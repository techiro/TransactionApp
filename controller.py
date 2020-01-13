import getIncome
import sys
class DB_Controller(object):
    TRANSACTION_MANAGER = "1"
    ACCOUNT_MANAGER = "2"
    END_MENU = "3"
    account_name = ""
    def __init__(self, DB_Model):
        print("hello this is controller_init_")
        self.DB = DB_Model

    def menu(self):
        print("Transaction Appを起動しました")
        print("あなたのアカウント名を教えてください")
        self.DB.account_name = input()
        while True:
            print("取引を確認する    1")
            print("口座を確認する    2")
            print("Transaction Appを終了する　　 3")
            print("あなたがしたいことを1か2で選んでください")
            response = input()

            if response == self.TRANSACTION_MANAGER:
                print("transaction_managerを確認します")
                self.DB.check_transaction()
                self.DB.disconnect_DB()
                

            elif response == self.ACCOUNT_MANAGER:
                print("account_managerを確認します")
                self.DB.check_account()
                self.DB.disconnect_DB()

            elif response == self.END_MENU:
                print("システムを終了します")
                self.DB.disconnectDB()
                sys.exit()

            
            else:
                print("----------もう一度入力を行ってください----------")


if __name__ == "__main__":
    db = getIncome.DB_Model("sample_db.sqlite")
    controller = DB_Controller(db)
    controller.menu()