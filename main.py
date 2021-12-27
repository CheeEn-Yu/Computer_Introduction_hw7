from hw import read_input, enter_answer, Judge


if __name__ == "__main__":
    answer = enter_answer()
    print(f"The length of answer is {len(answer)}")
    judge = Judge(answer=answer)

    while True:
        guess_num = read_input(len(answer))

        if judge.guess(guess_num):
            break

    print("Finish!!!")

