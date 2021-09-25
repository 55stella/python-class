#soln
num_subscriptin =input()
first_newspaper =input()
num_subscription2 =input()
second_newspaper = input()


split_set1 = set(first_newspaper.split())
split_set2= set(second_newspaper.split())
final = split_set1.intersection(split_set2)
print(final)


