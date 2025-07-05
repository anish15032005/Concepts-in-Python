#anagram = when two strings can be written using the exact same letters
#example = "public relations" is an anagram of "crap built on lies."

def anagram(s1,s2):
    #Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    #     #Return boolean for sorted match.
#     return sorted(s1) == sorted(s2)

# print(anagram('sanjay ','sinha'))
    
    #check if the same number of letters
    if len(s1) != len(s2):
        return False
    #count frequency of each letter
    count = {}
    for letter in s1:#for ever letter in first string letter: 'o'
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
        #do reverse for second string
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
            
    for k in count:
        if count[k] != 0:
            return False
        
    return True
x = anagram('Clint Eastwood','old WEST action') 
print(x)

            
    
    

    
    
    
    
    
    
    
    
    
    
    
    

    