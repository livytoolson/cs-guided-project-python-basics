"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):

    """
    def find_length(string):
        return len(string)
    
    lst.sort(key=find_len)
    return lst
    """

    """
    lst.sort(key=len)
    sort takes a list and sorts that list in place
    sort mutates the list
    """

    """
    lst.sort(key=lambda string: len(string))
    return lst
    """

    return sorted(lst, key=len)
    # sorted creates a new list and returns it 
    # does not manipulate the original list

print(sort_by_length(["a", "ccc", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["may", "april", "september", "august"]))
print(sort_by_length([]))
