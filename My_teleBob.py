class Alex():
    def __init__(self,a,b,c,d,e):
       self.name = a
       self.clothes = b
       self.health = c
       self.weapon = d
       self.impact = e

    def print_info(self):
        print('ваше имя:',self.name )
        print('вашa одежда:', self.clothes)
        print('ваше здоровье:', self.health)
        print('ваше оружее:', self.weapon)
        print('ваша сила удара:', self.impact)

me = Alex('alex','cap',100,'gun',200)
me.print_info()