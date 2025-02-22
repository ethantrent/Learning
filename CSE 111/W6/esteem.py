"""The Rosenberg self-esteem scale is a self-esteem measure developed by the sociologist Morris Rosenberg in 1965. 
It is still used in social-science research today. To complete the measure, a person completes a survey that contains
the following ten statements.

I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all."""


def main():

    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten"
    "statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the statements by responding with one of these four letters:")

    print("\nD means you strongly disagree with the statement."
    "d means you disagree with the statement."
    "a means you agree with the statement."
    "A means you strongly agree with the statement.")

    score = 0
    score += ask_positive_question("1. I feel that I am a person of worth, at least on an equal plane with others.")
    score += ask_positive_question("2. I feel that I have a number of good qualities.")
    score += ask_negative_question("3. All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question("4. I am able to do things as well as most other people.")
    score += ask_negative_question("5. I feel I do not have much to be proud of.")
    score += ask_positive_question("6. I take a positive attitude toward myself.")
    score += ask_positive_question("7. On the whole, I am satisfied with myself.")
    score += ask_negative_question("8. I wish I could have more respect for myself.")
    score += ask_negative_question("9. I certainly feel useless at times.")
    score += ask_negative_question("10. At times I think I am no good at all.")

    print(f"\nYour score is {score}.")


def ask_positive_question(statement):
    """This function will count the number of positive responses to the questions."""
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == "D":
        score += 0
    elif answer == "d":
        score += 1
    elif answer == "a":
        score += 2
    elif answer == "A":
        score += 3
    else:
        print("Invalid input. Please enter D, d, a, or A.")
    return score


def ask_negative_question(statement):
    """This function will count the number of negative responses to the questions."""
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == "D":
        score += 3
    elif answer == "d":
        score += 2
    elif answer == "a":
        score += 1
    elif answer == "A":
        score += 0
    else:
        print("Invalid input. Please enter D, d, a, or A.")
    return score

if __name__ == "__main__":
    main()





