class HandyDict:
    """Stolen from Flask"""
    def __getattr__(self, name: str):
        return self.__dict__[name]

    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def __delattr__(self, name: str) -> None:
        del self.__dict__[name]

    def __contains__(self, item: str) -> bool:
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self) -> str:
        return '<' + ', '.join('%s: {%s}' % item for item in vars(self).items()) + '>'