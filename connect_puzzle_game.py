import connect_ai as cai
import connect_at as cat
import connect_puzzle as cp
import BvB as bvb
import time

SEARCH_DEPTH = 5
connect = cp.Connect()
connect2 = cp.Connect()
connect3 = bvb.Connect()

print("-----------------------------------")
print("          CONNECT 4 GAME           ")
print("-----------------------------------")

while True:

    print("\nWYBIERZ TRYB GRY:")
    print("0.WYJDZ Z GRY")
    print("1.GRACZ VS BOT")
    print("2.BOT VS BOT")
    wybor = int(input("Wybor: "))
    print("\n\n\n")
    if wybor == 0:
        exit(0)
    elif wybor == 1:

        print("\n\n------------------------ALGORYTM MINIMAX BEZ ALFA I BETA----------------------------")

        while connect.has_winner() == 0:
            start = time.time()
            connect.print_turn()
            connect.play_move(cai.choose_move(connect, SEARCH_DEPTH))
            connect.print_board()
            end = time.time()
            print("\nTIME:")
            print(end - start)
            print("\n")
            print(connect.has_winner())

            connect.print_turn()
            human_move_result = False

            while human_move_result is False:
                print('Make your move: ')
                human_move = int(input())
                human_move_result = connect.play_move(human_move)
            connect.print_board()
            print(connect.has_winner())

        print("\n\n------------------------ALGORYTM MINIMAX Z ALFA I BETA----------------------------")

        while connect2.has_winner() == 0:
            start = time.time()
            connect2.print_turn()
            connect2.play_move(cat.choose_move(connect2, SEARCH_DEPTH))
            connect2.print_board()
            end = time.time()
            print("\nTIME:")
            print(end - start)
            print("\n")
            print(connect2.has_winner())

            connect2.print_turn()
            human_move_result = False
            while human_move_result is False:
                print('Make your move: ')
                human_move = int(input())
                human_move_result = connect2.play_move(human_move)
            connect2.print_board()
            print(connect2.has_winner())

    elif wybor == 2:
        while connect3.has_winner() == 0:
            print('\nBOT --- ALGORYTM BEZ ALFA I BETA\n')
            start = time.time()
            connect3.print_turn()
            connect3.play_move(cai.choose_move(connect3, SEARCH_DEPTH))
            connect3.print_board()
            end = time.time()
            print("\nTIME:")
            print(end - start)
            print("\n")
            print(connect3.has_winner())

            connect3.print_turn()

            print('\nBOT --- ALGORYTM Z ALFA I BETA\n')
            start = time.time()
            connect3.print_turn()
            connect3.play_move(cat.choose_move(connect3, SEARCH_DEPTH))
            connect3.print_board()
            end = time.time()
            print("\nTIME:")
            print(end - start)
            print("\n")
            print(connect3.has_winner())

            connect3.print_board()
            print(connect3.has_winner())

