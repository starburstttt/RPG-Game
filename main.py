from pip._internal.resolution.resolvelib import factory

from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 10, "dmg": 140},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]


player = Person(460, 65,60, 34, magic)
enemy = Person(1200, 65, 40, 25 , magic)

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "An enemy ATTACKS!" + bcolors.ENDC)
while running:
        print("============================================")
        player.choose_action()
        choice = input("Choose an action: ")
        index = int(choice) - 1

        if index == 0:
                dmg = player.generate_damage()
                enemy.take_dmg(dmg)
                print("You attacked for:", dmg, "points of damage. Enemy's HP:", enemy.get_hp())
        elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose a magic: ")) - 1
                magic_dmg = player.generate_spell_damage(magic_choice)
                magic = player.generate_spell_damage(magic_choice)
                spell = player.get_spell_name(magic_choice)
                cost = player.get_spell_mp_cost(magic_choice)

                current_mp = player.get_mp()

                if cost > current_mp:
                        print(bcolors.FAIL + "\nNot enough Magic Power\n" + bcolors.ENDC)
                        continue

                player.reduce_mp(cost)
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)



        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_dmg(enemy_dmg)
        print("Enemy attacks for:", enemy_dmg, "points of damage. Player's HP:", player.get_hp())

        print("=================================")
        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

        if enemy.get_hp() == 0:
                print(bcolors.OKGREEN + "You won!" + bcolors.ENDC)
                running = False
        elif player.get_hp() == 0:
                print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
                running = False
