class ScreenMeta(type):
    def __instancecheck__(self, instance):
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        return (hasattr(subclass, 'navigate') and callable(subclass.navigate)) \
          and (hasattr(subclass, 'goBack') and callable(subclass.goBack)) \
            and (hasattr(subclass, 'start') and callable(subclass.start)) \

class ScreenInterface(metaclass=ScreenMeta):
    pass

