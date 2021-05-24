class user():
    def __init__(self,id,nickname):
        self.id=id
        self.nickname=nickname

    def updatenick(self,nickname):
        self.nickname=nickname
    
    def getid(self,id):
        return self.id

