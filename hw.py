class Judge:
    def __init__(self, answer: str) -> None:
        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        # TODO

    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        # TODO


def read_input(guess_len: int) -> str:
    """
    Function that read player's guess.
    guess_len: length the the player should guess. it would be same as the length of answer
    return: the valid string guessed by player

    You should show the hint message:
        "Enter your guess:\n"
    If the player's guess is invalid, you should print:
        "Invalid, please enter your guess again:\n"
    Note: a valid guess means contain only guess_len non-repetitive integer range from 0~9
    """
    # TODO
    input=("Enter your guess:\n")

def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    # TODO
