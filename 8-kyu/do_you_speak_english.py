# Premade functions are for noobs
#===================================

# I is not working, let's change the logic a little

# def sp_eng(sentence):

#     if len(sentence) == 0: return False

#     x = ['e', 'n', 'g', 'l', 'i', 's', 'h'][::-1]
#     st = 0

#     for c in sentence:
#         if len(x) != 0 and c.lower() == x[len(x) - 1]: 
#             st = 1
#             x.pop()
#         elif st and len(x) > 0:
#             return False
                
#     return not len(x)

# Not working as well

# def sp_eng(sentence):
#     if len(sentence) == 0:
#         return False

#     word = 'english'
#     idx = 0

#     for char in sentence.lower():
#         if char == word[idx]:
#             idx += 1
#             if idx == len(word):
#                 return True
#         elif char in word[idx:]:
#             return False
#     return False

# == Nevermind, i gave up ==
def sp_eng(sentence):
    return "english" in sentence.lower()