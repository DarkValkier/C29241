from character import Character
from berserk import Berserk


player1 = Character(name='Victor', health=150, damage=5)
player2 = Berserk(name='Petya', damage=5)

player1.print_stats()
print()
player2.print_stats()

while player1.alive() and player2.alive():
    print()
    damage_p1 = player1.attack(player2)
    damage_p2 = player2.attack(player1)
    print(f'{player1.name} атаковал {player2.name} и нанёс {round(damage_p1, 2)} урона.')
    print(f'{player2.name} атаковал {player1.name} и нанёс {round(damage_p2, 2)} урона.')
    print(f'У {player1.name} осталось {round(player1.health, 2)} здоровья')
    print(f'У {player2.name} осталось {round(player2.health, 2)} здоровья')
    print()

player1.print_stats()
print()
player2.print_stats()