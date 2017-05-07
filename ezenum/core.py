"""Core components of the ezenum package."""

import collections.abc
import enum



class StringDenum(collections.abc.Sequence):
    """Easy, ordered enum-like objects from String lists.

    Arguments
    ---------
    members : list
        A list of strings,

    Example
    -------
    >>> colors = StringEnum(['Red', 'Blue', 'Green'])
    >>> colors.Red
    'Red'
    """
    def __init__(self, members):
        self.members = members
        for name in members:
            setattr(self, name, name)
    def __getitem__(self, index):
        return self.members[index]
    def __len__(self):
        return len(self.members)
    def __repr__(self):
        return str(self.members)


def string_enum(name, member_list):
    """Get an orderable enum of strings from the given list."""
    return type(name, enum.Enum, {
        member: member for member in member_list
    })
