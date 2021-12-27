# Computer Introduction Hw7 - python 

### Introduction

In this homework, you need to finish a judge of the game "[Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)" (numeric version).

The game flow shows in below:

1. Enter the secret number (or you can call it answer) of this game. It consists of some non-repetitve numbers; its length is smaller than 10. We assume the answer must be valid.
2. Then, the player start to guess the number. Notice that the player's input might be invalid. The below cases are considered invalid.
   - The guess contains non-digit characters
   - The length of the guess doesn't equal to the length of the answer.
   - The guess contains repetitive characters.
3. Based on the guess and the secret number, the judge would tell the player that his/her guess is "xAxB".
4. Repeat step 2 & 3 until the player gets the correct answer.

### What you need to do

Finish all the funcitons and classed in `hw.py`
The below is the output format:

- When the player start to guess, you print `Enter your guess:\n` to the screen
- If the player's guess is invaild, you should print `Invalid, please enter your guess again:\n` to the screen
- The judge would tell the players: `Your guess is ...; the result is ...A...B\n`
  - E.g. if the player guess 0123, and the answer is 0538, the judge would tell:
    `Your guess is 0123; the result is 1A1B\n`

Other notice:

- You are **NOT** allowed to modify `main.py`
- You are **NOT** allowed to use any packages
- For the submission form, please refer to the homework [slide](https://docs.google.com/presentation/d/1KP3hLg8JemKJfMik8PmadV5bgj4essCBcq9GetbqK7A/edit?usp=sharing)

### How to execute it

- Interactive mode:

```python
python main.py
```

- Test the score:

```bash
bash test.sh
```
