"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    result= score_result(score)
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        print(result)
    random_score=random.random()
    print(score_result(random_score))

def score_result(score):
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
