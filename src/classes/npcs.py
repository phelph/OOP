class Enemy:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.hp = lvl * 3 + 50
        self.dmg = self.lvl * 5 + 10
        self.gold = lvl * 10
        self.exp = lvl * 5 + 10

    def get_attacked(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            return self.hp, self.gold
        return self.hp, 0
