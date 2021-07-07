class smartdict(dict):
    def __init__(self):
        pass

    def add_attribute(self, key, value):
        self.__setattr__(key, value)
        self.__setitem__(key, value)


def convert(obj: list) -> smartdict:
    """
    Converts list to dict. Format is expected as a list of lists with either another list as a key and/or value. If both parameters is a list, the values for each key will be asigned the list from the value index.

    Allowed formats:

    ```
    ["key", "value"]
    ["key", ["value1", "value2"]]
    [["key1", "key2"], "value"]
    [["key1", "key2"], ["value1", "value2"]]

    # dict.key -> value
    # dict["key"] -> value
    ```
    """
    if not isinstance(obj, list):
        return None

    sm = smartdict()
    for elem in obj:
        if not isinstance(elem, list):
            return None
        
        key, value = elem
        if isinstance(key, list):
            for e in key:
                sm.add_attribute(e, value)
        
        else:
            sm.add_attribute(key, value)
    

    return sm
