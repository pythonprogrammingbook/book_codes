import random
random_integers = [random.randint(1, 100) for i in range(100)]
random_integers_without_duplication = list(set(random_integers))
random_integers_without_duplication.sort()
print(random_integers_without_duplication)