class NPC_Creator:
    def create_npc(self, friendly: bool, type: str, lvl: int):
        if not friendly:
            return Enemy("Demon", lvl)


class Enemy:
    def __init__(self, enemy_type: str, lvl: int):
        self.enemy_type = enemy_type
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
