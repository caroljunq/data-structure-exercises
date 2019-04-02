import random
hashtable = {_: [] for _ in range(10)}

def insert_el(val):
    key = hash(val)
    index = key % len(hashtable)
    hashtable[index].append(val)
    print(hashtable)

insert_el("mariana")
insert_el("carolina")
