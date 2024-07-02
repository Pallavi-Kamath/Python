def anagram(str1,str2):
    if(sorted(str1) == sorted(str2)):
        print('anagram')
    else:
        print('not anagram')

anagram("listen", "silent")