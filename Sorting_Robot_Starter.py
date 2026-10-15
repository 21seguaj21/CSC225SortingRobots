"""CSC 225 — Sorting Robot Lottery, simplified edition.

Complete TimeSheet, choose_algorithms, and only your two randomly assigned sorts.
Each sorting function returns (sorted_original_list, number_of_value_comparisons).
Run: python3 Sorting_Robot_Starter.py
"""
import random


class TimeSheet:
    def __init__(self, algorithm):
        self.name = algorithm
        self.count = []
        self.comparisons = self.count

    def add_run(self, count):
        self.count.append(count)

    def average(self):
        return sum(self.count) / len(self.count) if self.count else None

    def median(self):
        if not self.count:
            return None
        ordered = sorted(self.count)
        middle = len(ordered) // 2
        if len(ordered) % 2:
            return ordered[middle]
        return (ordered[middle - 1] + ordered[middle]) / 2

    def standard_deviation(self):
        if not self.count:
            return None
        mean = self.average()
        variance = sum((value - mean) ** 2 for value in self.count) / len(self.count)
        return variance ** 0.5

    def minimum(self):
        return min(self.count) if self.count else None

    def maximum(self):
        return max(self.count) if self.count else None


def bubble_sort(values):
    n = len(values) - 1
    for i in range(n):
        for j in range(n - i):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]




def selection_sort(values):
    # TODO if assigned
    myList = list(values)
    comparisons = 0
    if len(myList) == 0:
        return None
    else:
        n = len(myList)-1
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if myList[j] < myList[min_index]:
                    min_index = j
                    comparisons += 1
            if min_index != i:
                myList[i],myList[min_index] = myList[min_index],myList[i]
    return myList, comparisons 



def merge_sort(values):
    pass

def quick_sort(values):
    comparisons = 0

    def sort(items):
        nonlocal comparisons
        if len(items) <= 1:
            return items

        pivot = items[len(items) // 2]
        lower, equal, higher = [], [], []
        for item in items:
            comparisons += 1
            if item < pivot:
                lower.append(item)
            else:
                comparisons += 1
                if item > pivot:
                    higher.append(item)
                else:
                    equal.append(item)

        return sort(lower) + equal + sort(higher)

    return sort(list(values)), comparisons


def heap_sort(values):
    data = list(values)
    comparisons = 0

    def sift_down(root, end):
        nonlocal comparisons
        while 2 * root + 1 < end:
            child = 2 * root + 1
            right = child + 1
            if right < end:
                comparisons += 1
                if data[right] > data[child]:
                    child = right
            comparisons += 1
            if data[root] >= data[child]:
                return
            data[root], data[child] = data[child], data[root]
            root = child

    for root in range(len(data) // 2 - 1, -1, -1):
        sift_down(root, len(data))
    for end in range(len(data) - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end)

    return data, comparisons

    
ALGORITHMS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
}


def choose_algorithms(seed):
    """Use random.Random(seed).sample(...) for two DISTINCT names."""
    return random.Random(seed).sample(list(ALGORITHMS), 2)


NUMBER_OF_RUNS = 50
LIST_SIZE = 100


def make_test_lists(seed):
    """Create reproducible random lists; both methods receive identical inputs."""
    rng = random.Random(seed + 1000)
    return [[rng.randint(0, 999) for _ in range(LIST_SIZE)]
            for _ in range(NUMBER_OF_RUNS)]


def run_lab(seed):
    selected = choose_algorithms(seed)
    sheets = {name: TimeSheet(name) for name in selected}
    print(f"Seed: {seed} | Algorithms: {', '.join(selected)}")
    print(f"{'Run':>4} {'Method':12} {'Comparisons':>12}")
    for run_number, original in enumerate(make_test_lists(seed), start=1):
        for name in selected:
            values = original.copy()
            _, count = ALGORITHMS[name](values)
            sheets[name].add_run(count)
            print(f"{run_number:4d} {name:12} {count:12d}")
    print("\nCOMPARISON SUMMARIES")
    for name in selected:
        sheet = sheets[name]
        print(f"{name}: counts={sheet.comparisons}, average={sheet.average()}, "
              f"median={sheet.median()}, std_dev={sheet.standard_deviation()}, "
              f"min={sheet.minimum()}, max={sheet.maximum()}")


if __name__ == "__main__":
    seed = int(input("Enter your integer seed: "))
    run_lab(seed)
