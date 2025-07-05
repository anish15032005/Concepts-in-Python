# def reverse(s):
#     s = s.split()
#     s.reverse()
#     return s
    
# print(reverse("Sanjay is a soldier"))

def reverse(s):
    return " $ ".join(reversed(s.split()))

print(reverse("Sanjay is a Soldier"))


def reverse2(s):
    return " * ".join(s.split()[::-1])

print(reverse2("This is the best"))

def reverse3(s):
    length = len(s)
    spaces = ['  ']
    words = []
    i = 0
    
    while i < length:
        if s[i] not in spaces:
            word_start = i
            
            while i < length and s[i] not in spaces:
                i += 1 
            words.append(s[word_start:i])
        i += 1
        
    return "".join(reversed(s))
print(reverse3("dolphins are smarter than dogs"))


def reverse4(s):
    return s.split()[::-1]

print(reverse4("i am groot"))

#simple code like reverse3
def simple_rev3(s):
    words = s.split()
    rev_ord = reversed(words)
    rev_each = [word[::-1] for word in rev_ord]
    return " ".join(rev_each)
             
print(simple_rev3(".dogs are friends but horses are brothers"))