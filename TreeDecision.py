# Exemplo de arvore de decisao
from __future__ import division
from collections import Counter, defaultdict
from functools import partial
import math, random


# revisado
def entropy(class_probabilities):
    return sum(-p * math.log(p, 2) for p in class_probabilities if p)


# revisado
def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]


# revisado
def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)


# revisado
def partition_entropy(subsets):
    total_count = sum(len(subsets) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)


#revisado
# Criando grupos
def group_by(items, key_fn):
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups


#revisado
def partition_by(inputs, attribute):
    return group_by(inputs, lambda x: x[0][attribute])


#revisado
def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs, attribute)
    return partition_entropy(partitions.values())


#revisado
def classify(tree, input):
    if tree in [True, False]:
        return tree
    attribute, subtree_dict = tree
    subtree_key = input.get(attribute)
    if subtree_key not in subtree_dict:
        subtree_key = None
    subtree = subtree_dict[subtree_key]
    return classify(subtree, input)


#revisado
def build_tree_id3(inputs, split_candidates=None):
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues
    if num_trues == 0:
        return False
    if num_falses == 0:
        return True
    if not split_candidates:
        return num_trues >= num_falses
    best_atribute = min(split_candidates, key=partial(partition_entropy_by, inputs))
    partitions = partition_by(inputs, best_atribute)
    new_candidates = [a for a in split_candidates if a != best_atribute]
    subtrees = {attribute: build_tree_id3(subset, new_candidates) for attribute, subset in partitions.iteritems()}
    subtrees[None] = num_trues > num_falses
    return best_atribute, subtrees


#revisado
def forest_classify(trees, input):
    votes = [classify(tree, input) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]


print("ARVORE DE DECISAO PYTHON\n")
if __name__ == '__main__':
    inputs = [
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)
    ]

for key in ['level', 'lang', 'tweets', 'phd']:
    print key, partition_entropy_by(inputs, key)
senior_inputs = [(input, label) for input, label in inputs if input["level"] == "Senior"]
print '\n'
for key in ['lang', 'tweets', 'phd']:
    print key, partition_entropy_by(senior_inputs, key)

print

print "building the tree"
tree = build_tree_id3(inputs)
print tree
print "Junior / Java / tweets / no phd", classify(tree, {"level": "Junior", "lang": "Java",
                                                         "tweets": "yes", "phd": "no"})

print "Junior / Java / tweets / phd", classify(tree, {"level": "Junior", "lang": "Java",
                                                      "tweets": "yes", "phd": "yes"})
print "Intern", classify(tree, { "level" : "Intern" } )
print "Senior", classify(tree, { "level" : "Senior" } )
raw_input()