def resetable(cls):
    cls._resetable_cache_ = cls.__dict__.copy()
    return cls

def reset(cls):
    cache = cls._resetable_cache_ # raises AttributeError on class without decorator
    for key in [key for key in cls.__dict__ if key not in cache]:
        delattr(cls, key)
    for key, value in cache.items():  # reset the items to original values
        try:
            setattr(cls, key, value)
        except AttributeError:
            pass



@resetable   # use resetable on a class that you want to do this with
class Foo(object):
    pass

Foo.x = 1
print (Foo.x)
reset(Foo)
o = Foo() 
print (o.x) # raises AttributeError as expected