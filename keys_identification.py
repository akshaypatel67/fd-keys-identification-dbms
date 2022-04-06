import itertools


# relation = input("enter attributes in relation: ")
# fd_list = input("Enter functional dependencies: ")
# to_find = input("Enter attribute to find closure of: ")

relation = []
fd_list = []

flag = 1


# to_find = to_find.split(",")

fd_pairs = []
fd_attributes = []
fd_closure = []

presentRight = set()

attributes_set = []
closures_set = []

keyset = []

essential = set()

keys = []

def clearAll():
    global relation, fd_list, flag, fd_pairs, fd_attributes, presentRight, fd_closure, essential, keyset, attributes_set, keys

    relation = []
    fd_list = []

    flag = 1


    # to_find = to_find.split(",")

    fd_pairs = []
    fd_attributes = []
    fd_closure = []

    presentRight = set()

    attributes_set = []
    closures_set = []

    keyset = []

    essential = set()

    keys = []

# method to find closure of attribute set
def findClosure(x):
    to_find = x.copy()
    mark = []

    flag=1

    while flag:
        flag = 0
        for i,pair in enumerate(fd_pairs):
            if(i not in mark):
                pair_set = set(pair[0])
                to_find_set = set(to_find)

                if pair_set.issubset(to_find_set):
                    mark.append(i)
                    to_find.extend(pair[1])
                    flag = 1

    ans=list(set(to_find))
    ans.sort()
    return ans

# method to check if attribute is already a subset of candidate key
def checkKey(temp):
    for x in keyset:
        if set(x).issubset(temp):
            return False
    return True

# method to find candidate keys from given FDs
def findKey():
    fl=0
    for L in range(1, len(attributes_set)+1):
        for subset in itertools.combinations(attributes_set, L):
            temp = []
            temp.extend(essential)
            # print(subset,"sub")
            for x in subset:
                ind = attributes_set.index(x)
                temp.extend(x)
            temp = list(set(temp))
            temp.sort()
            # print(temp)
            tempset = set(temp)
            if findClosure(temp) == relation and checkKey(tempset):
                print(temp)
                keyset.append(temp)
                keys.append(temp)
                fl = 1
                return fl
    return fl


def submit(relation_str, fdList):
    global relation, fd_list, flag, fd_pairs, fd_attributes, presentRight, fd_closure, essential, keyset, attributes_set

    clearAll()

    fd_list = fdList
    relation = relation_str

    # fd_list = fd_list.split(" ")
    relation = relation.split(",")
    relation.sort()

    flag = 1

    # split fd with '->'
    for x in fd_list:
        pair = x.split("->")
        pair[0] = pair[0].split(",")
        pair[1] = pair[1].split(",")

        fd_pairs.append(pair)
        fd_attributes.append(pair[0])
        presentRight.update(pair[1])

    # find essential attributes
    essential = set(relation).difference(presentRight)
    # print(essential)
    essential = list(essential)



    # remove redundant Fds
    for i in range(len(fd_attributes)):
        fd_attributes[i].sort()
        if(fd_attributes[i] not in attributes_set):
            attributes_set.extend(fd_attributes[i])

    print()


    # check if essential attributes form candidate key
    if findClosure(essential) == relation:
        print(essential)
        keyset.append(essential)
        keys.append(essential)

    else:
        flag = 1

        while flag:
            print()
            flag = findKey()

    return keys

# submit(input(), input())