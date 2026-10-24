def ft_filter(function, iterable):
    for value in iterable:
        if function(value):
            yield value
