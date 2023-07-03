all_things = {
    'палатка': 5,
    'спальник': 3,
    'посуда': 2,
    'топор': 2,
    'удочка': 1,
    'одежда': 1,
    'еда': 5
}
MAX_WEIGHT = 14
bag = {}
count_weight = 0
for thing, weight in all_things.items():
    if count_weight + weight <= MAX_WEIGHT:
        bag[thing] = weight
        count_weight += weight
print(bag)