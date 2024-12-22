def my_gen():
    n = 1
    print('primeiro print , n e igual a {}'.format(n))

    yield n
    n+=1

    print('segundo print , n e igual a {}'.format(n))
    yield

    n+=1
    print('terceiro e ultimo print , n e igual a {}'.format(n))
    yield n

test = my_gen()
for value in test:
    print(value)
