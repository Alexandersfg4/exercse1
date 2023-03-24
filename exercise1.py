PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
ROUND = "round"
GAME = "game"
cards_of_the_first_player = (10, 6, 8, 9, 7, 12, 7)
cards_of_the_second_player = (7, 6, 9, 5, 2, 8, 11)


class IncorrectScope(Exception):
    pass


def print_winner(winner_name, scope, winner_score, loser_score):
    main_part = f"{winner_name} wins the {scope}"
    if scope == ROUND:
        main_part += f", with {winner_score} beating {loser_score}"
    elif scope == GAME:
        main_part += f", by {winner_score} wins to {loser_score}"
    else:
        raise IncorrectScope
    print(main_part)


if __name__ == "__main__":
    first_player_wins = 0
    second_player_wins = 0
    round_number = 0
    print(8 * "*" + "Card Blusters" + 8 * "*", end="\n\n")
    for firs_player_score, second_player_score in zip(
        cards_of_the_first_player, cards_of_the_second_player
    ):
        round_number += 1
        print(f"Round number {round_number}: ", end="")
        if firs_player_score > second_player_score:
            print_winner(PLAYER_1, ROUND, firs_player_score, second_player_score)
            first_player_wins += 1
        elif firs_player_score < second_player_score:
            print_winner(PLAYER_2, ROUND, second_player_score, firs_player_score)
            second_player_wins += 1
        else:
            print("This round has ended in a draw")
    print("")
    if first_player_wins > second_player_wins:
        print_winner(PLAYER_1, GAME, first_player_wins, second_player_wins)
    elif first_player_wins < second_player_wins:
        print_winner(PLAYER_2, GAME, second_player_wins, first_player_wins)
    else:
        print("The game has ended in a draw")
