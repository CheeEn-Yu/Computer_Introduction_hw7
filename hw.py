class Judge:
    def __init__(self, answer: str) -> None:
        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        # TODO
        self.answer = answer

    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        # TODO
        self.num = num
        A = 0
        B = 0
        for i in range(len(self.answer)):
            if self.answer[i] == num[i]:
                A+=1
        for i in range(len(self.answer)-1):
            for j in range(i+1,len(self.answer)):
                if self.answer[i] == self.answer[j]:
                    B+=1
        print("Your guess is %s; the result is %dA%dB" %(num,A,B))

        if self.num == self.answer:
            return 1
        return 0


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
    guess=input("Enter your guess:\n")
    while(len(guess) != guess_len):
        guess = input("Invalid, please enter your guess again:\n")
    for i in range(guess_len-1):
        for j in range(i+1,guess_len):
            while(guess[i] == guess[j]):
                guess = input("Invalid, please enter your guess again:\n")
    for i in range(guess_len):
        while(guess[i]!='1' or guess[i]!='2' or guess[i]!='3'or guess[i]!='4'or guess[i]!='5'or guess[i]!='6'or guess[i]!='7'or guess[i]!='8'or guess[i]!='9'or guess[i]!='0'):
            guess = input("Invalid, please enter your guess again:\n")


    return guess
    

def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    # TODO
    read=input()
    return read