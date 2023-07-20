from secondday.app.dice import rolldice

def guess_number(number):
    result = rolldice()
    if result == number:
        return "You Won the match"
    else:
        return "You Lost the match"