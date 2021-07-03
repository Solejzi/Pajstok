def a(*args, **kwargs):
    print(*args)

    print(args)
    print(kwargs)


a('x','c', xd=1, xd2=2 )