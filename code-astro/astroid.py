from ship import Ship
ship = Ship()
class Astroid():
    def __init__(self, pos_x:int, pos_y:int,height:float,width: float,speed:int)->None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.speed = speed
        self.hitbox = [self.pos_x - self.width / 2, self.pos_y - self.height / 2, self.pos_x + self.width / 2,
                       self.pos_y + width / 2]
        super().__init__(pos_x-width/2,pos_y-height/2,pos_x+width/2,pos_y+width/2)
    def move(self)->None:
        self.pos_y -= self.speed
        self.hitbox[1] = self.pos_y - self.height / 2
        self.hitbox[3] = self.pos_y + self.height / 2
    def getright(self)-> float:
        return self.hitbox[2]
    def getleft(self)-> float:
        return self.hitbox[0]
    def getup(self)-> float:
        return self.hitbox[3]
    def getdown(self)-> float:
        return self.hitbox[1]
    def doiitaship(self,target :Ship)->bool:
        d: bool = self.getright() >= target.getleft()
        c: bool = self.getdown() <= target.getup()
        b: bool = self.getleft() <= target.getright()
        a: bool = self.getup() >= target.getdown()
        e: bool = d and b
        g: bool = c and a
        return e and g



