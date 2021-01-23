class Phone:
    companyName = "Apple"
    modelName = "iPhone"
    userName = ""

    def __init__(self, user):
        super().__init__()
        self.userName = user

    def userMobile(self):
        print("iOS")
        print(self.userName)

sayan = Phone("Sayan")    
sayan.userMobile()    