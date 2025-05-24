# @Time: 2025/5/12 23:27
# @Author: Junyuan Li
# @File: game.py
# @Software : PyCharm
from ship import Ship


class Game:
    def __init__(self):
        self.size = 5
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.players = {
            'Red': {'coins': 10, 'ships': []},
            'Blue': {'coins': 10, 'ships': []}
        }
        self.turn = 'Red'
        self.built_type3 = {'Red': False, 'Blue': False}  # type 3 can be summoned once
        self.action_taken = False

    def place_ship(self, ship_type, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Invalid position.")
            return False

        if self.board[y][x] is not None:
            print("Position already occupied.")
            return False

        if ship_type == 3 and self.built_type3[self.turn]:
            print("Type 3 ship already used.")
            return False

        if self.turn == 'Red' and x != 0:
            print("Red can only summon ships in column 0.")
            return False
        if self.turn == 'Blue' and x != 4:
            print("Blue can only summon ships in column 4.")
            return False

        ship = Ship(ship_type, self.turn, (x, y))
        if self.players[self.turn]['coins'] >= ship.cost:
            self.players[self.turn]['coins'] -= ship.cost
            self.players[self.turn]['ships'].append(ship)
            self.board[y][x] = ship
            if ship_type == 3:
                self.built_type3[self.turn] = True
            print(f"{self.turn} summoned Ship {ship_type} at ({x}, {y})")
            self.action_taken = True
            return True
        else:
            print("Not enough coins.")
            return False

    def move_ship(self, ship, new_x, new_y):
        if ship.team != self.turn:
            print("Not your ship.")
            return False

        if ship.move_range == 0:
            print("This ship cannot move.")
            return False

        dx = abs(ship.position[0] - new_x)
        dy = abs(ship.position[1] - new_y)
        if dx + dy > ship.move_range:
            print("Move out of range.")
            return False

        if not (0 <= new_x < self.size and 0 <= new_y < self.size):
            print("Move out of bounds.")
            return False

        if self.board[new_y][new_x] is not None:
            print("Target position is occupied.")
            return False

        self.board[ship.position[1]][ship.position[0]] = None
        ship.position = (new_x, new_y)
        self.board[new_y][new_x] = ship
        print(f"{ship.team} moved ship to ({new_x}, {new_y})")
        self.action_taken = True
        return True

    def attack(self, attacker, target):
        if attacker.team == target.team:
            print("Cannot attack ally.")
            return False

        if not attacker.can_attack(target):
            print("Target out of range.")
            return False

        target.take_damage(attacker.damage)
        print(f"{attacker.team} attacked {target.team}'s ship at {target.position}, remaining HP: {target.hp}")

        if not target.is_alive():
            self.board[target.position[1]][target.position[0]] = None
            self.players[target.team]['ships'].remove(target)
            self.players[attacker.team]['coins'] += 5
            self.players[target.team]['coins'] += 2
            print(f"{target.team}'s ship destroyed! Coins refunded: +5 to {attacker.team}, +2 to {target.team}")

        self.action_taken = True
        return True

    def end_turn(self):
        if self.action_taken:
            self.turn = 'Blue' if self.turn == 'Red' else 'Red'
            self.action_taken = False
        else:
            print("You must take an action before ending your turn.")

    def check_win_condition(self):
        for team in ['Red', 'Blue']:
            ships = self.players[team]['ships']
            coins = self.players[team]['coins']
            if not ships and coins < 4:
                loser = team
                winner = 'Red' if team == 'Blue' else 'Blue'
                print(f"{loser} cannot continue. {winner} wins!")
                return True
        return False
