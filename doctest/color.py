# user.py
class User:
    def __init__(self, name, favorite_colors):
        self.name = name
        self._favorite_colors = set(favorite_colors)

    @property
    def favorite_colors(self):
        """Return the user's favorite colors.

        Usage examples:
        >>> john = User("John", {"#797EF6", "#4ADEDE", "#1AA7EC"})
        >>> sorted(john.favorite_colors)
        ['#1AA7EC', '#4ADEDE', '#797EF6']
        """
        return self._favorite_colors
    
    """_summary_
    Exploring Some Limitations of doctest
Probably the most significant limitation of doctest compared to other testing frameworks is the lack of features equivalent to fixtures in pytest or the setup and teardown mechanisms in unittest. If you ever need setup and teardown code, then you’ll have to write it in every affected docstring. Alternatively, you can use the unittest API, which provides some setup and teardown options.
    """
