from unit import Unit
unit = Unit()
class Ship(Unit):
    def __init__(self, pos_x:int, pos_y:int,height:float,width: float,speed:int,hp:int,ammo:int)->None:
        super().__init__(pos_x,pos_y,height,width,float,speed,hp)
        self.ammo = ammo
    def shoot(self)->None:
        self.ammo -=1
