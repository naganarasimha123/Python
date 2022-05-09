class BasePasswordManager:
    old_passwords = []
    
    def get_password(self):
        if(len(self.old_passwords)):
            return self.old_passwords[-1]
        else:
            return "Password yet to set"
    
    def is_correct(self, typed_password):
        if(not len(self.old_passwords)):
            return "Password yet to set"
        if(self.old_passwords[-1] == typed_password):
            return True
        return False


class PasswordManager(BasePasswordManager):

    def get_level(self, new_password = None):
        if(new_password):
            to_check = new_password
        else:
            to_check = BasePasswordManager.old_passwords[-1]
        if(to_check.isalpha() or to_check.isnumeric()):
            level = 0
        elif(to_check.isalnum()):
            level = 1
        else:
            level = 2
        return level

    def set_password(self, new_password):
        if(not len(BasePasswordManager.old_passwords)):
            BasePasswordManager.old_passwords.append(new_password)
            print("New password is set")
            return
        else:
            curr_level = self.get_level()
        new_level = self.get_level(new_password)
        if(new_level > curr_level and len(new_password)>=6):
            BasePasswordManager.old_passwords.append(new_password)
            print("New password is set")
        else:
            print("Security level of new password is lower than current password")

pwd_manager = PasswordManager()
base_pwd_manager = BasePasswordManager()

#print(base_pwd_manager.is_correct("12345"))
#print(base_pwd_manager.get_password())

pwd_manager.set_password("12345")
#print(base_pwd_manager.get_password())
#print(pwd_manager.get_level())
pwd_manager.set_password("12345a")
#pwd_manager.set_password("12345$a")

        

    
    
        
        
             
    
    
