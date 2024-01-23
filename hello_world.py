class ImmutableList:
    def __init__(self, items):
        self.items = tuple(items)

    def add_item(self, new_item):
        return ImmutableList(self.items + (new_item,))

    def get_items(self):
        return self.items

def transform_list(immutable_list: ImmutableList, transformer_function) -> ImmutableList:
    return ImmutableList(map(transformer_function, immutable_list.get_items()))

original_list = ImmutableList([1, 2, 3])
squared_list = transform_list(original_list, lambda x: x**2)
print("Original List:", original_list.get_items())
print("Squared List:", squared_list.get_items())
