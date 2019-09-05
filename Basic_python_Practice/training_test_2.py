import random

number_of_player = input("enter the number of player for this game: ")
number_of_player = int(number_of_player)

if (number_of_player > 1) and (number_of_player <= 4):
    final_point1, final_point2, final_point3, winner1, winner2, winner3 = 0, 0, 0, 0, 0, 0
    final_point, point2, point1, point3, point4 = 0, 0, 0, 0, 0
    p1, p2, p3, p4, d = 0, 0, 0, 0, 0
    if number_of_player == 2:
        player1_name = input("enter the first player name: ")
        player2_name = input("enter the second player name ")
        player1_name = player1_name.upper()
        player2_name = player2_name.upper()

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
                    d = d + 1
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
            print(player1_name, ' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print('Both draws: ', d, ' rounds')
            print(player1_name, " is the winner. Congratulations!")
        else:
            print(player1_name, ' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print('Both draws: ', d, ' rounds')
            print(player2_name, " is the winner. Congratulations!")

    # for 3 players

    elif number_of_player == 3:
        player1_name = input("enter the first player name: ")
        player2_name = input("enter the second player name ")
        player3_name = input("enter the third player name ")
        player1_name = player1_name.upper()
        player2_name = player2_name.upper()
        player3_name = player3_name.upper()

        while final_point < 100:
            for x in range(1):
                point1 = random.randint(1, 7)
                point2 = random.randint(1, 7)
                point3 = random.randint(1, 7)
                if point1 > point2 and point1 > point3:
                    final_point1 = final_point1 + point1
                    p1 = p1 + 1
                    print('final_point_1: ', final_point1)
                elif point2 > point1 and point2 > point3:
                    final_point2 = final_point2 + point2
                    p2 = p2 + 1
                    print('final_point_2: ', final_point2)
                elif point3 > point1 and point3 > point2:
                    final_point3 = final_point3 + point3
                    p3 = p3 + 1
                    print('final_point_3: ', final_point3)
                elif point1 == point2 and point1 > point3:
                    final_point1 = final_point1 + point1
                    final_point2 = final_point2 + point2
                    p1 = p1 + 1
                    p2 = p2 + 1
                    print('final_point_1: ', final_point1)
                    print('final_point_2: ', final_point2)
                elif point1 > point2 and point1 == point3:
                    final_point1 = final_point1 + point1
                    final_point3 = final_point3 + point3
                    p1 = p1 + 1
                    p3 = p3 + 1
                    print('final_point_1: ', final_point1)
                    print('final_point_3: ', final_point3)
                elif point2 == point3 and point2 > point1:
                    final_point3 = final_point3 + point3
                    final_point2 = final_point2 + point2
                    p3 = p3 + 1
                    p2 = p2 + 1
                    print('final_point_1: ', final_point1)
                    print('final_point_2: ', final_point2)
                else:
                    final_point1 = final_point1 + point1
                    final_point2 = final_point2 + point2
                    final_point3 = final_point3 + point3
                    d = d + 1
                print(point1)
                print(point2)
                print(point3)

            if final_point1 > final_point2 and final_point1 > final_point3:
                final_point = final_point1
                winner1 = winner1 + 1
            elif final_point2 > final_point1 and final_point2 > final_point3:
                final_point = final_point2
                winner2 = winner2 + 1
            elif final_point3 > final_point1 and final_point3 > final_point2:
                final_point = final_point3
                winner3 = winner3 + 1
            else:
                final_point = final_point
            print('final point ', final_point)
            print('-------------------------------')

        if winner1 > winner2 and winner1 > winner3:
            print(player1_name, ' plays: ', p1, ' rounds')
            print(player2_name, ' plays: ', p2, ' rounds')
            print(player3_name, ' plays: ', p3, ' rounds')
            print('All draws: ', d, ' rounds')
            print(player1_name, " is the winner. Congratulations!")
        elif winner2 > winner1 and winner2 > winner3:
            print(player1_name, ' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print(player3_name, ' wins: ', p3, ' rounds')
            print('All draws: ', d, ' rounds')
            print(player2_name, " is the winner. Congratulations!")
        else:
            print(player1_name, ' wins: ', p1, ' rounds')
            print(player2_name, ' wins: ', p2, ' rounds')
            print(player3_name, ' wins: ', p3, ' rounds')
            print('All draws: ', d, ' rounds')
            print(player3_name, " is the winner. Congratulations!")
else:
    print("Please play with minimum 2 and maximum 4 players. Thanks.")
