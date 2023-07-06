def get_kwargs_dict(**kwargs):
    kwargs_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            kwargs_dict[value] = key
        except TypeError:
            kwargs_dict[str(value)] = key
    return kwargs_dict


print(get_kwargs_dict(a=3, c=11, b=[1, 2]))