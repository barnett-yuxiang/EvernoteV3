"""
Modify the global variable inside a function
"""

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

# There is no block scope in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
