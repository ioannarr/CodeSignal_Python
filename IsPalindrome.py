def solution(inputString):
    if (len(inputString) == 1):
        return True
    elif (len(inputString) > 1):
        if(inputString == inputString[::-1]):
            return True 
        else:
            return False
    else:
        return False