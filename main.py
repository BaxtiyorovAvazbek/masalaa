# 1-masala
family = {
    "father":"Darth Vader",
    "sister":"Leia",
    "brother in law":"Han",
    "droid":"R2D2"
}
name = input("Name: ")
def relation_to_luke(name):
    for x in family:
        if family[x] == name:
            return f"Luke, I am your {x}."
        elif family[x] == name:
            return f"Luke, I am your {x}."
        elif family[x] == name:
            return f"Luke, I am your {x}."


print(relation_to_luke(name))
# 2-masala
def get_budgets(lst):
    result = 0
    for x in lst:
        y = x.get("budget")
        result += y

    return result


print(get_budgets([
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]))
# 3-masala
def get_student_names(lst):
    sort_name = []
    for x in lst:
        sort_name.append(lst[x])
    sort_name.sort()
    return sort_name


print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))
# 4-masala
def maximum_score(lst2):
    result2 = 0
    for x in lst2:
        y = x.get("score")
        result2 += y
    return result2


print(maximum_score([
    {"tile": "N", "score": 1},
    {"tile": "K", "score": 5},
    {"tile": "Z", "score": 10},
    {"tile": "X", "score": 8},
    {"tile": "D", "score": 2},
    {"tile": "A", "score": 1},
    {"tile": "E", "score": 1}
]))
# 5-masala
# 6-masala
def mapping(map):
    lugat = {}
    for x in map:
        lugat[x] = x.upper()
        print(lugat)
    return lugat


print(mapping(["p", "s"]))
# 7-masala
def count(count_all):
    harflar = 0
    sonlar = 0
    for x in count_all:
        if x.isalpha():
            harflar += 1
        elif x.isdigit():
            sonlar += 1
    return {'LETTERS': harflar, 'DIGITS': sonlar}


count_all = ("Hello World")
natija = count(count_all)
print(natija)
# 8-masala
def calc(calc_diff):
    value = calc_diff.values()
    n = sum(value)
    print(n - naxt)


naxt = int(input("Son: "))
calc_diff = {"baseball bat": 20}
calc(calc_diff)
# 9-masala
# 10-masala