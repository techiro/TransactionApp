import getIncome
import sys
class DB_Controller(object):
    TRANSACTION_MANAGER = "1"
    ACCOUNT_MANAGER = "2"
    END_MENU = "b"
    account_name = ""
    def __init__(self, DB_Model):
        self.DB = DB_Model

    def menu(self):
        print("Transaction Appを起動しました")
        print("あなたのアカウント名を教えてください")
        self.DB.account_name = input()

        while True:
            print("==========================")
            print("取引マネージャーを起動する{:>10}".format(self.TRANSACTION_MANAGER))
            print("口座マネージャーを起動する{:>10}".format(self.ACCOUNT_MANAGER))
            print("MENUに戻る{:>26}".format(self.END_MENU))
            print("あなたがしたいことを1,2,bで選んでください")
            print("==========================\n")
            response = input()
            
            if response == self.TRANSACTION_MANAGER:
                print("transaction_managerを確認します")
                self.DB.check_transaction()
                

            elif response == self.ACCOUNT_MANAGER:
                print("account_managerを確認します")
                self.DB.check_account()

            elif response == self.END_MENU:
                print("システムを終了します")
                sys.exit()

            
            else:
                print("----------もう一度入力を行ってください----------")


if __name__ == "__main__":
    db = getIncome.DB_Model("sample_db.sqlite")
    controller = DB_Controller(db)
    controller.menu()