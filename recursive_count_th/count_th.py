'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #if under two characters it cannot contain 'th' so return 0
    if len(word) < 2:
        return 0
    # a slice to see if between letters 0-2 has 'th' then add to count
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    # go to the next word
    else: 
        return count_th(word[1:])