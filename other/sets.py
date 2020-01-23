print("Sets are unordered and store unique values")
l1 = [inner_idx for outer_idx in range(5) for inner_idx in range(10)]
print("Converting to set will drop the duplicates")
s1 = set(l1)
print("set comprehension is also available")
s2 = {i for i in range(20) if i % 2 == 1}
print("Built in features like union and intersection")
print(s1.union(s2), '\n', s1.intersection(s2))

jobs = set()
jobs.add('engineer')
try:
    jobs.add(['teacher', 'chemist'])
except Exception as e:
    print(f"{e}. Cannot add mutable objects to sets")

print(jobs)
