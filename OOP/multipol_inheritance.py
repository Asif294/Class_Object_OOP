class Family:
    def __init__(self,addres):
        self.address=addres
class sports:
    def __init__(self,game):
        self.game=game
class school:
    def __init__(self,level,id):
        self.level=level
        self.id=id

class student(Family,sports,school):
    def __init__(self, addres,game,level,id):
        school.__init__(self, id,level)
        sports.__init__(self ,game)
        super().__init__(addres)
        
    
        