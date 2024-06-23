def main():
   score = get_vaild_score()
   menu=("(G)et a valid score (must be 0-100 inclusive)"+"\n"
         +"(P)rint result"+"\n"+"(S)how stars"+"\n"+"(Q)uit")
   print(menu)
   result=score_result(score)
   stars=show_stars(score)
   choice = input("Choose:").upper()
   while choice != "Q":
       if choice=="G":
           print(score)
       elif choice=="P":
           print(result)
       else:
           print(stars)
       print(menu)
       choice = input("Choose:").upper()
   print("Farewell")
def get_vaild_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def score_result(score):
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    else:
        return "Excellent"

def score_result(score):
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    else:
        return "Excellent"

def show_stars(score):
    return '*' * score

main()