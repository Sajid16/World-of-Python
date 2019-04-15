class Enemy:
    life = 3
    kill = 0

    def attack(self):
        self.life = self.life + 1
        print('Successfully killed one gamer.\nYou have {0} life left'.format(self.life))

    def kill(self, name):
        self.life = self.life - 1
        print('You are killed by ' + name + ' gamer\nYou have {0} life left'.format(self.life))


class Gamer:
    life = 3
    kill = 0

    def attack(self):
        self.life = self.life + 1
        print('Successfully killed one enemy.\nYou have {0} life left'.format(self.life))

    def kill(self, name):
        self.life = self.life - 1
        print('You are killed by ' + name + ' enemy\nYou have {0} life left'.format(self.life))


while True:
    Enemy1 = Enemy()
    Gamer1 = Gamer()

    enemy_name = input('Enter enemy name:\n')
    gamer_name = input('Enter gamer name:\n')
    choice = int(input('1.want to attack as an enemy\n2.want to kill as an enemy\n3.want to attack as a gamer\n4.want to kill as a gamer\n'))

    if choice == 1:
        Enemy1.attack()
    elif choice == 2:
        Enemy1.kill(gamer_name)
    elif choice == 3:
        Gamer1.attack()
    else:
        Gamer1.kill(enemy_name)