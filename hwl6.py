# 1
def yes_or_no (some_int):
    watched = set()
    for i in some_int:
        if i not in watched:
            watched.add(i)
            print('No')
        else:
            print('Yes')
    return
yes_or_no([1, 2, 2, 3, 4, 5, 4, 3, 2, 1, 7])

# 2
def count_char(str_val):
    dict_1 = {}
    for i in str_val:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    return dict_1
print(count_char('python is the faster-growing major programming language'))

#3
def bread(func):
    def wrapper():
        print('</------------\\>')
        func()
        print('<\\____________/')
    return wrapper

def tomato():
    print('  **помидоры**')

def salad():
    print('-----салат-----')

def cheese():
    print('^^^^^^сыр^^^^^^^')

def onion():
    print('  -----лук-----')

def beef():
    print(' ###говядина###')

def chicken():
    print(' ||||курица||||')

@bread
def hamburger():
    onion()
    tomato()
    beef()
@bread
def chickenburger():
    cheese()
    salad()
    chicken()

hamburger()
chickenburger()




