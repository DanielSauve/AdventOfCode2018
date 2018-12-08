import sys


def sum_metadata(tree):
    tree = list(map(lambda x: int(x), tree))
    metadata_sum = 0
    children_count = tree[0]
    metadata_count = tree[1]
    next_child = 2
    for i in range(children_count):
        meta, next_count = child_metadata(tree[next_child:])
        metadata_sum += meta
        next_child += next_count
    for i in range(metadata_count):
        metadata_sum += tree[next_child + i]
    return metadata_sum


def child_metadata(tree):
    metadata_sum = 0
    children_count = tree[0]
    metadata_count = tree[1]
    next_child = 2
    if children_count == 0:
        for i in range(metadata_count):
            metadata_sum += tree[2 + i]
        return metadata_sum, 2 + metadata_count
    for _ in range(children_count):
        meta, next_count = child_metadata(tree[next_child:])
        metadata_sum += meta
        next_child += next_count
    for i in range(metadata_count):
        metadata_sum += tree[next_child + i]
    return metadata_sum, next_child + metadata_count


if __name__ == "__main__":
    problemInput = open("./day8.txt").read()
    sys.setrecursionlimit(10000)
    print(sum_metadata(problemInput.split()))
