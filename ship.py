# @Time: 2025/5/12 23:26
# @Author: Junyuan Li
# @File: ship.py
# @Software : PyCharm
class Ship:
    def __init__(self, ship_type, team, position):
        self.ship_type = ship_type
        self.team = team  # 'Red' or 'Blue'
        self.position = position  # (x, y)

        if ship_type == 1:
            self.hp = 2
            self.move_range = 2
            self.damage = 1
            self.attack_range = 1
            self.cost = 4
        elif ship_type == 2:
            self.hp = 4
            self.move_range = 1
            self.damage = 2
            self.attack_range = 2
            self.cost = 5
        elif ship_type == 3:
            self.hp = 6
            self.move_range = 0
            self.damage = 1
            self.attack_range = 25  # Full map range
            self.cost = 6

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def can_attack(self, target):
        dx = abs(self.position[0] - target.position[0])
        dy = abs(self.position[1] - target.position[1])
        return max(dx, dy) <= self.attack_range

