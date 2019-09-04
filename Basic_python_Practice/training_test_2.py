import random

number_of_player = input("enter the number of player for this game: ")
number_of_player = int(number_of_player)

if (number_of_player > 1) and (number_of_player <= 4):
    final_point1, final_point2 = 0, 0
    final_point, point2, point1 = 0, 0, 0
    p1, p2, p3, p4, d = 0, 0, 0, 0, 0
    if number_of_player == 2:
        player1_name = input("enter the first player name: ")
        player2_name = input("enter the second player name ")
        player1_name = player1_name.upper()
        player2_name = player2_name.upper()
        # for x in range(1):
        #     point1 = random.randint(1, 7)
        #     point2 = random.randint(1, 7)
        #     # print(point1)
        #     # print(point2)
        #     if point1 > point2:
        #         final_point1 = final_point1 + point1
        #     elif point2 > point1:
        #         final_point2 = final_point2 + point2
        #     else:
        #         final_point1 = final_point1 + point1
        #         final_point2 = final_point2 + point2
        #
        # if final_point1 > final_point2:
        #     final_point = final_point1
        # else:
        #     final_point = final_point2
        # print(point1)
        # print(point2)
        # print(final_point)
        while final_point < 100:
            for x in range(1):
                point1 = random.randint(1, 7)
                point2 = random.randint(1, 7)
                if point1 > point2:
                    final_point1 = final_point1 + point1
                    p1 = p1 + 1
                    print('final_point_1: ', final_point1)
                elif point2 > point1:
                    final_point2 = final_point2 + point2
                    p2 = p2 + 1
                    print('final_point_2: ', final_point2)
                else:
                    final_point1 = final_point1 + point1
                    final_point2 = final_point2 + point2
                    d = d+1
                print(point1)
                print(point2)

            if final_point1 > final_point2:
                final_point = final_point1
            elif final_point2 > final_point1:
                final_point = final_point2
            else:
                final_point = final_point1
            print(final_point)
            print('-------------------------------')

        if p1 > p2:
            print(player1_name,' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print('Both draws: ', d, ' rounds')
            print(player1_name," is the winner. Congratulations!")
        else:
            print(player1_name, ' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print('Both draws: ', d, ' rounds')
            print(player2_name, " is the winner. Congratulations!")
else:
    print("Please play with minimum 2 and maximum 4 players. Thanks.")
