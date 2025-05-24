# @Time: 2025/5/12 23:27
# @Author: Junyuan Li
# @File: main.py
# @Software : PyCharm
from game import Game


def display_board(game):
    print("\nBoard \n(X axis ↓):")
    header = "   " + "  ".join(str(x) for x in range(game.size))
    print(header)
    print("   " + "---" * game.size)
    for y in range(game.size):
        row = f"{y} |"  # Y-axis marker
        for x in range(game.size):
            ship = game.board[y][x]
            if ship:
                symbol = f"R{ship.ship_type}" if ship.team == "Red" else f"B{ship.ship_type}"
            else:
                symbol = "."
            row += f"{symbol:^3}"
        print(row)
    print("↑ Y axis")


'''
                ship_type = int(input("Ship type (1/2/3): "))
                y = int(input("Y position (0-4)[red's x = 0; blue's x = 4]: "))
                if game.turn == 'Red':
                    x = 0
                else:
                    x = 4
                game.place_ship(ship_type, x, y)
'''


def main():
    game = Game()
    print("Victory condition: When one side has no ships and no money to continue summoning ships")
    while True:
        print(f"\n{game.turn}'s Turn (Coins: {game.players[game.turn]['coins']})")
        display_board(game)

        if game.check_win_condition():
            break

        command = input("Enter command (summon/move/attack): ").strip()

        if command == 'summon':
            try:
                while True:
                    ship_type = int(input("Ship type (1/2/3): "))
                    if ship_type not in [1, 2, 3]:
                        print(f"please enter valid number")
                        continue
                    else:
                        break
                y = int(input("Y position (0-4)[red's x = 0; blue's x = 4]: "))
                if game.turn == 'Red':
                    x = 0
                else:
                    x = 4
                game.place_ship(ship_type, x, y)
            except ValueError:
                print("Invalid input.")

        elif command == 'move':
            try:
                x = int(input("Current X: "))
                y = int(input("Current Y: "))
                new_x = int(input("New X: "))
                new_y = int(input("New Y: "))
                ship = game.board[y][x]
                if ship:
                    if ship.team == game.turn:
                        game.move_ship(ship, new_x, new_y)
                    else:
                        print("You can only move your own ship.")
                else:
                    print("No ship at this location.")
            except:
                print("Invalid move input.")

        elif command == 'attack':
            try:
                ax = int(input("Attacker X: "))
                ay = int(input("Attacker Y: "))
                attacker = game.board[ay][ax]
                if attacker:
                    if attacker.team == game.turn:
                        print(
                            f"Attacker Info - HP: {attacker.hp}, Damage: {attacker.damage}"
                            f", Attack Range: {attacker.attack_range}")
                        tx = int(input("Target X: "))
                        ty = int(input("Target Y: "))
                        target = game.board[ty][tx]
                        if target:
                            game.attack(attacker, target)
                        else:
                            print("No target at this location.")
                    else:
                        print("You can only attack with your own ship.")
                else:
                    print("No attacker at this location.")
            except:
                print("Invalid attack input.")
        else:
            print("Unknown command.")
        if game.check_win_condition():
            break
        game.end_turn()


if __name__ == "__main__":
    main()
