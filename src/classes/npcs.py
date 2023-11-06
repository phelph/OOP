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

    def take_dmg(self, dmg) -> tuple[bool, int, int]:
        """
        Calculates the damage dealt to the NPC and returns a boolean indicating
        if the NPC was killed or not, the remaining HP and the gained gold.
        """

        self.hp -= dmg

        if self.hp <= 0:
            killed = True
            return killed, 0, self.gold

        killed = False
        return killed, self.hp, 0
