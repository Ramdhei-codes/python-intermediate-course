class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password # atributo privado
    
    @property
    def password(self):
        """Docs of this method"""
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password
        print(f'Pass set to {self.__password}')
    



roberto = User('Roberto', '38799')

print(f'{roberto.username}: {roberto._User__password}')

