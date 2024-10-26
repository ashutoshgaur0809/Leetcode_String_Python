T  = int(input("Enter Total Number of Test Cases -> "))

for i in range(T):
    N,M = map(int,input("Enter Len of two strings -> "))
    Sa = input("Enter String 1->")
    Sb = input("Enter String 2->")


    Sc = Sa + Sb
    Sc = set(Sc)

    if len(Sc) < 26:
        print("Yes")
    else:
        print("No")

# Enter Total Number of Test Cases -> 3
# Enter String 1->dijkstra
# Enter String 2->blossom   
# Yes
# Enter String 1->fastquicklazypropagation
# Enter String 2->westmajixhoverboard
# N0
# Enter String 1->supercalifragilisticexpialidocious
# Enter String 2->pneumonoultramicroscopicsilicovolcanoconiosis
# Yes
