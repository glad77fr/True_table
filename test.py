import itertools
import numpy as np

def or_true_table(nb_item):
    full_combinaison = list(itertools.product([0, 1], repeat=nb_item))
    full_combinaison = np.array(full_combinaison)
    sum_combinaison = full_combinaison.sum(axis=1)
    true_position = tuple(np.where(sum_combinaison != 0))
    return full_combinaison[true_position]

def and_true_table(nb_item):
    full_combinaison = list(itertools.product([0, 1], repeat=nb_item))
    full_combinaison = np.array(full_combinaison)
    sum_combinaison = full_combinaison.sum(axis=1)
    true_position = tuple(np.where(sum_combinaison == nb_item))
    return full_combinaison[true_position]

def xor_true_table(nb_item):
    full_combinaison = list(itertools.product([0, 1], repeat=nb_item))
    full_combinaison = np.array(full_combinaison)
    sum_combinaison = full_combinaison.sum(axis=1)
    true_position = tuple(np.where(sum_combinaison == 1))
    return full_combinaison[true_position]

test = xor_true_table(5)
print(test)