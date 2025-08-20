from rock_pap_sci import decide_winner

""" Testing get_user_choice() """


# def test_get_user_choice_rock():
#     assert (get_user_choice() == "Rock")


# def test_get_user_choice_paper():
#     assert (get_user_choice() == "Paper")


# def test_get_user_choice_scissors():
#     assert (get_user_choice() == "Scissors")


""" Testing decide_winner() """


def test_decide_winner_rock():
    assert (decide_winner("Rock", "Scissors") == "You win!")


def test_decide_winner_paper():
    assert (decide_winner("Paper", "Rock") == "You win!")


def test_decide_winner_scissors():
    assert (decide_winner("Scissors", "Paper") == "You win!")
