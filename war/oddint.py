def find_it(seq):
    for x in seq:
        if seq.count(x) %2 != 0:
            return x
