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

import glob
import os
import shelve


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


class ShelveBijectiveList(BijectiveList):
    r"""
    Replacement for list class with only a few methods, such as __getitem__()
    index(), and index_append().
    List lookup for __getitem__ uses a list named _item.
    Index lookup for index() and index_append() uses a dict named _index.
    This class is used for 1-1 relationships where index lookup via dict makes sense.
    *** NOTE ***
    This class uses shelve for persistence.
    """
    def __init__(self, other_list=None, file_prefix="/tmp/ShelveBijectiveList"):
        """
        *** Warning *** Initialization from a non-empty list can easily break
                        the 1-1 relationship between index and item in a BijectiveList.
        """
        self.file_prefix = file_prefix
        # Work around http://bugs.python.org/issue18039 not fixed in 2.7*
        self.remove()
        self._item = shelve.open(file_prefix+".item", flag='n')
        self._index = shelve.open(file_prefix+".index", flag='n')
        if other_list != None:
            for index in range(len(other_list)):
                item = other_list[index]
                self._item[str(index)] = item
                self._index[item] = index


    def __getitem__(self, index):
        r"""
        List lookup by index.
        """
        return self._item[str(index)]


    def index_append(self, item):
        r"""
        Use a lookup using _index instead of calling index() on the list.
        If the lookup yields a KeyError then set index to the length of self,
        append item to self, and add index to _index.
        """
        try:
            index = self._index[item]
        except KeyError:
            index = len(self._item)
            self._item[str(index)] = item
            self._index[item] = index
        return index


    def sync(self):
        self._item.sync()
        self._index.sync()


    def close_list(self):
        self._item.close()


    def close_dict(self):
        self._index.close()


    def close(self):
        self.close_list()
        self.close_dict()


    def remove_list(self):
        for fn in glob.glob(self.file_prefix+".item*"):
            os.remove(fn)


    def remove_dict(self):
        for fn in glob.glob(self.file_prefix+".index*"):
            os.remove(fn)


    def remove(self):
        self.remove_list()
        self.remove_dict()

