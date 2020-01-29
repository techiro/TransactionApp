import getIncome
import sys
class DB_Controller(object):
    TRANSACTION_MANAGER = "1"
    ACCOUNT_MANAGER = "2"
    END_MENU = "f"
    account_name = ""
    input_password = ""
    def __init__(self, DB_Model):
        self.DB = DB_Model

    def menu(self):
        print("Transaction Appを起動しました")
        while True:
            
            print("あなたのアカウント名を教えてください")
            
            self.DB.account_name = input()
            print ("パスワードを入力してください")
            self.DB.input_password = input()
            auth = self.DB.auth()
            if auth == True:
                while True:
                    print("==========================")
                    print("取引マネージャーを起動する{:>10}".format(self.TRANSACTION_MANAGER))
                    print("口座マネージャーを起動する{:>10}".format(self.ACCOUNT_MANAGER))
                    print("終了する。{:>26}".format(self.END_MENU))
                    print("あなたがしたいことを1,2,fで選んでください")
                    print("==========================\n")
                    response = input()
                    
                    if response == self.TRANSACTION_MANAGER:
                        print("取引マネージャーを確認します")
                        self.DB.check_transaction()
                        

                    elif response == self.ACCOUNT_MANAGER:
                        print("口座マネージャーを確認します")
                        self.DB.check_account()

                    elif response == self.END_MENU:
                        print("システムを終了します")
                        sys.exit()

                    
                    else:
                        print("----------もう一度入力を行ってください----------")
            else:
                print("パスワードもしくはアカウント名が間違っています。もう一度入力してください。")
                print("==========================\n")



if __name__ == "__main__":
    db = getIncome.DB_Model("sample_db.sqlite")
    controller = DB_Controller(db)
    controller.menu()