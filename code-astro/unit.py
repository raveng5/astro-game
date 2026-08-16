class Unit:
    def __init__(self, pos_x:int, pos_y:int,height:float,width: float,speed:int,hp:int)->None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.speed = speed
        self.hp = hp
    def gethitbox(self)-> list[float]:
        hitbox = [self.pos_x - self.width / 2, self.pos_y - self.height / 2, self.pos_x + self.width / 2, self.pos_y + self.width / 2]
        return hitbox

    def goup(self)-> None:
        self.pos_y += self.speed

    def godown(self)->None:
        self.pos_y -= self.speed

    def goleft(self)->None:
        self.pos_x -=self.speed

    def goright(self)->None:
        self.pos_x += self.speed

    def getleft(self)->float:
        ls = self.gethitbox()
        if ls[0]>ls[2]:
            return ls[2]
        return ls[0]

    def getright(self)->float:
        ls = self.gethitbox()
        if ls[0]>ls[2]:
            return ls[0]
        return ls[2]

    def gethigh(self)->float:
        ls = self.gethitbox()
        if ls[1]>ls[3]:
            return ls[1]
        return ls[3]

    def getlow(self)->float:
        ls = self.gethitbox()
        if ls[1]>ls[3]:
            return ls[3]
        return ls[1]
    def dotheyhit(self, op:Unit)->bool:
        d: bool = self.getright() >= op.getleft()
        c: bool = self.getlow() <= op.gethigh()
        b: bool = self.getleft() <= op.getright()
        a: bool = self.gethigh() >= op.getlow()
        e: bool = d and b
        g: bool = c and a
        return e and g
