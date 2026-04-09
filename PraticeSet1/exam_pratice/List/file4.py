# remove duplicates from a list of tuples

tp = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('a', 'b')]
new_tp = list(set(tp))

print("Original list of tuples:", tp)
print("List of tuples after removing duplicates:", new_tp)