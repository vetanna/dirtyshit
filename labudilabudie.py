def polindromcheck(word):
    #word = str(input())
    cringe = word [::-1]
    if word == cringe:
        return True
    else:
        return False


print(polindromcheck(str(input())))


