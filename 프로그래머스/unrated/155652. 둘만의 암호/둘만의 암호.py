def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in skip :
        alphabet = alphabet.replace(i,'')

    for one in s :
        result += alphabet[(alphabet.find(one) + index) % len(alphabet)]

    return result