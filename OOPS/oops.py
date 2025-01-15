class account():
    def __init__(self, acc, pwd):
        self.acc = acc
        self.__pwd = pwd
    
    def __printpwd(self, pwd):
        print("The passwrod is: ", pwd)
    
a = account(1234, "abcd")
print(a.__pwd)