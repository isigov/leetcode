def strongPasswordChecker(s):
    """
    :type s: str
    :rtype: int
    """
    minimumChange = 0
    freeSpace = 0
    adding = 0
    whiteSpace = 0
    strSize = len(s)
    print("==============================")
    print("s=" + str(s))
    print("strlen=" + str(strSize))
    if strSize < 6:
        adding = 6 - strSize 
    if strSize > 20:
        whiteSpace = strSize - 20
    
    i = 0
    upper = False
    lower = False
    digit = False
    
    stateCharacter = ''
    state = 0
    maxRepeating = 1
    repeating = []
    repeated = False
    while i < strSize:
        if s[i].isupper():
            upper = True
        if s[i].isdigit():
            digit = True
        if s[i].islower():
            lower = True
        if s[i] == stateCharacter:
            state += 1
            maxRepeating += 1
            if state == 2:
                freeSpace += 1
                state = 0
                repeated = True
        else:
            if repeated == True and maxRepeating >= 3:
                repeating.append(maxRepeating)
            stateCharacter = s[i]
            state = 0
            repeated = False
            maxRepeating = 1
        i += 1
    if repeated == True and maxRepeating >= 3:
        repeating.append(maxRepeating)

    if not upper:
        minimumChange += 1
    if not digit:
        minimumChange += 1
    if not lower:
        minimumChange += 1

    print("repeating=" + str(repeating))
    print("minimumChange=" + str(minimumChange))
    print("whiteSpace=" + str(whiteSpace))

    if whiteSpace > 0 and minimumChange == 0 and freeSpace == 0:
        return whiteSpace

    if adding >= minimumChange and adding >= freeSpace:
        return adding

    if freeSpace > 0 and whiteSpace > 0:
        reg = 0
        loop = 0
        threeCount = 0
        fourCount = 0
        oldWhiteSpace = whiteSpace
        repeatCount = len(repeating)
        remainder = whiteSpace % repeatCount
        each = 0
        if whiteSpace - remainder > 0:
            each = (whiteSpace - remainder) / repeatCount
        else:
            each = 1
            repeating = sorted(repeating, reverse=True)
            print("repeating=" + str(repeating))
        for rep in repeating:
            if loop == repeatCount - 1 and whiteSpace > 0:
                reg += (((((rep - each - remainder) - ((rep - each - remainder) % 3)) / 3)))
                if rep - each - remainder == 3:
                    threeCount += 1
                if rep - each - remainder == 4:
                    fourCount += 1
            else:
                if whiteSpace == 0:
                    each = 0
                reg += (((((rep - each) - ((rep - each) % 3)) / 3)))
                if rep - each == 3:
                    threeCount += 1
                if rep - each == 4:
                    fourCount += 1
                if remainder == oldWhiteSpace and each == 1:
                    whiteSpace -= 1
            print("reg=" + str(reg))
            loop += 1
        if oldWhiteSpace + reg > minimumChange and reg > 0:
            if threeCount > 0 and fourCount > 0:
                counter = 0
                if threeCount > fourCount:
                    counter = threeCount - abs(threeCount - fourCount)
                elif fourCount > threeCount:
                    counter = fourCount - abs(threeCount - fourCount)
                elif fourCount == threeCount:
                    counter = fourCount
                return reg + oldWhiteSpace - counter
            elif 4 in repeating and 3 in repeating:
                return reg + oldWhiteSpace - 1
            return reg + oldWhiteSpace
        return oldWhiteSpace + minimumChange

    if whiteSpace == freeSpace and minimumChange > 0:
        return minimumChange + freeSpace

    if freeSpace >= minimumChange and whiteSpace == 0:
        reg = 0
        for rep in repeating:
            reg += ((((rep - (rep % 3)) / 3)))
        return reg + adding

print(strongPasswordChecker("aaa111") == 2)
print(strongPasswordChecker("1234aaaaa567890123456B") == 3)
print(strongPasswordChecker("1010101010aaaB10101010") == 2)
print(strongPasswordChecker("abc123") == 1)
print(strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa") == 7)
print(strongPasswordChecker("ABABABABABABABABABAB1") == 2)
print(strongPasswordChecker("") == 6)
print(strongPasswordChecker("...") == 3)
print(strongPasswordChecker("1111111111") == 3)
print(strongPasswordChecker("aaa") == 3)
print(strongPasswordChecker("aaaa") == 2)
print(strongPasswordChecker("aaaaa") == 2)
print(strongPasswordChecker("aaaaaa") == 2)
print(strongPasswordChecker("aaaaaaa") == 2)
print(strongPasswordChecker("aaaaaaaa") == 2)
print(strongPasswordChecker("aaaaaaaaa") == 3) # 9
print(strongPasswordChecker("aaaaaaaaaa") == 3) # 10
print(strongPasswordChecker("aaaaaaaaaaa") == 3) # 11 #-1
print(strongPasswordChecker("aaaaaaaaaaaa") == 4) # 12 #-0
print(strongPasswordChecker("aaaaaaaaaaaaa") == 4) # 13 #-1
print(strongPasswordChecker("aaaaaaaaaaaaaa") == 4) # 14 #-1
print(strongPasswordChecker("aaaaaaaaaaaaaaa") == 5) # 15 #-1
print(strongPasswordChecker("aaaaaaaaaaaaaaaa") == 5) #-1
print(strongPasswordChecker("aaaaaaaaaaaaaaaaa") == 5) #-2
print(strongPasswordChecker("aaaaaaaaaaaaaaaaaa") == 6) #-1
print(strongPasswordChecker("aaaaaaaaaaaaaaaaaaa") == 6) #-2
print(strongPasswordChecker("aaaaaaaaaaaaaaaaaaaa") == 6) #-2
print(strongPasswordChecker("ppppppppppppppppppp") == 6)
print(strongPasswordChecker("abAbababababababaaa") == 1)
print(strongPasswordChecker("abAbabababababababaaa") == 2)
print(strongPasswordChecker("QQQQQ") == 2)
print(strongPasswordChecker("aaAA11") == 0)
print(strongPasswordChecker("hoAISJDBVWD09232UHJEPODKNLADU1") == 10)
print(strongPasswordChecker("abababababababababaaa") == 3)
print(strongPasswordChecker("ababababababababababaaa") == 5)
print(strongPasswordChecker("ababababababababaaaaa") == 3)
print(strongPasswordChecker("1234567890123456Baaaaa") == 3)
print(strongPasswordChecker("..................!!!") == 7)
print(strongPasswordChecker("AAAAAABBBBBB123456789a") == 4)
print(strongPasswordChecker("aaaaabbbb1234567890ABA") == 3)
print(strongPasswordChecker("aaaaaabbbbbcccc5BAbcdd") == 5)
print(strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC") == 13)
print(strongPasswordChecker("aaaabbaaabbaaa123456A") == 3)
print(strongPasswordChecker("aaaabaaaaaa123456789F") == 3)