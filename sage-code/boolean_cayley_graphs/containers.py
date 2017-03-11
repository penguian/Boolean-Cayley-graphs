r"""
Containers, such as lists.

Paul Leopardi.
"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


class List(list):
    r"""
    Subclass of list with added methods, such as index_append.
    """
    def index_append(self, item):
        """
        If the inherited list index() method for self yields a ValueError,
         then set result to the length of self, and append item to self.
        """
        try:
            result = self.index(item)
        except ValueError:
            result = len(self)
            self.append(item)
        return result


class BijectiveList(object):
    r"""
    Replacement for list class with only a few methods, such as __getitem__()
    index(), and index_append().
    List lookup for __getitem__ uses a list named _item.
    Index lookup for index() and index_append() uses a dict named _index.
    This class is used for 1-1 relationships where index lookup via dict makes sense.
    """
    def __init__(self, other_list=None):
        """
        *** Warning *** Initialization from a non-empty list can easily break
                        the 1-1 relationship between index and item in a BijectiveList.
        """
        if other_list == None:
            self._item = []
            self._index = {}
        else:
            self._item = other_list
            self._index = dict((other_list[index],index)
                               for index in range(len(other_list)))


    def __getitem__(self, index):
        r"""
        List lookup by index.
        """
        return self._item[index]


    def __len__(self):
        r"""
        Get the length of the list.
        """
        return len(self._item)


    def get_dict(self):
        r"""
        Get the dict part of the BijectiveList.
        """
        return self._index


    def get_list(self):
        r"""
        Get the list part of the BijectiveList.
        """
        return self._item


    def index(self,item):
        r"""
        Replacement for list index() method.
        Use a dict lookup using _index instead of calling index() on the list.
        If the dict lookup yields a KeyError then raise a ValueError.
        """
        try:
            result = self._index[item]
        except KeyError:
            raise ValueError("{} is not in list".format(item))
        return result


    def index_append(self,item):
        r"""
        Use a dict lookup using _index instead of calling index() on the list.
        If the dict lookup yields a KeyError then set result to the length of self,
        append item to self, and add result to _index.
        """
        try:
            result = self._index[item]
        except KeyError:
            result = len(self._item)
            self._item.append(item)
            self._index[item] = result
        return result


