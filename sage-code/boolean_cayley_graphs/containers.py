r"""
Containers, such as lists.

AUTHORS:

- Paul Leopardi (2016-08-21): initial version

"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import glob
import os
import random
import shelve
import string

default_alphabet = string.digits + string.ascii_letters
default_length = 64


def random_name(alphabet=default_alphabet, length=default_length):
   return ''.join(random.choice(alphabet)
                  for i in range(length))


class List(list):
    r"""
    Subclass of list with added methods, such as index_append.
    """
    def index_append(self, item):
        r"""
        Return the index of a given item, appending it if necessary.

        If the inherited list index() method for self yields a ValueError,
        then set result to the length of self, and append item to self.

        INPUT:

        - ``self`` -- the current object.
        - ``item`` -- the item to look up, and append if necessary.

        OUTPUT:

        A non-negative integer indicating the index of ``item`` within ``self``.

        EFFECT:

        The item ``item`` may be appended to ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import List
            sage: L = List([1,2,4])
            sage: I = L.index_append(2)
            sage: I
            1
            sage: L
            [1, 2, 4]
            sage: I = L.index_append(3)
            sage: I
            3
            sage: L
            [1, 2, 4, 3]
        """
        try:
            result = self.index(item)
        except ValueError:
            result = len(self)
            self.append(item)
        return result


class BijectiveList(object):
    r"""
    Replacement for the list class with only a few methods,
    such as __getitem__(), index(), and index_append().

    List lookup for __getitem__ uses a list named _item.
    Index lookup for index() and index_append() uses a dict named _index.
    This class is used for 1-1 relationships where index lookup via dict makes sense.

    .. WARNING::

        Initialization from a non-empty list can easily break
        the 1-1 relationship between index and item in a BijectiveList.
    """
    def __init__(self, other_list=None, file_prefix=None):
        r"""
        .. WARNING::

            Initialization from a non-empty list can easily break
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
        Return the index of a given item.

        Use a dict lookup using _index instead of calling index() on the list.
        If the dict lookup yields a KeyError then raise a ValueError.
        """
        try:
            result = self._index[item]
        except KeyError:
            raise ValueError("{} is not in list".format(item))
        return result


    def index_append(self, item):
        r"""
        Return the index of a given item, appending it if necessary.

        Use a dict lookup using _index instead of calling index() on the list.
        If the dict lookup yields a KeyError then set result to the length of self,
        append item to self, and add result to _index.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,4])
            sage: BI = BL.index_append(2)
            sage: BI
            1
            sage: BL.get_list()
            [1, 2, 4]
            sage: BI = BL.index_append(3)
            sage: BI
            3
            sage: BL.get_list()
            [1, 2, 4, 3]
            sage: BL.get_dict()
            {1: 0, 2: 1, 3: 3, 4: 2}

        """
        try:
            result = self._index[item]
        except KeyError:
            result = len(self._item)
            self._item.append(item)
            self._index[item] = result
        return result


    def sync(self):
        pass


    def close_dict(self):
        pass


    def remove_dict(self):
        try:
            del self._index
        except AttributeError:
            pass


    def __del__(self):
        self.remove_dict()


class ShelveBijectiveList(BijectiveList):
    r"""
    Replacement for the list class with only a few methods,
    such as __getitem__() index(), and index_append().

    List lookup for __getitem__ uses a list named _item.
    Index lookup for index() and index_append() uses a shelve named _index.
    This class is used for 1-1 relationships where index lookup via dict makes sense.

    .. NOTE::

        This class uses shelve to work around memory restrictions.

    .. WARNING::

    Initialization from a non-empty list works only for lists of strings.

    .. WARNING::

        Initialization from a non-empty list can easily break
        the 1-1 relationship between index and item in a ShelveBijectiveList.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
        sage: SBL = ShelveBijectiveList(["1","2","4"])
        sage: SBL.get_list()
        ['1', '2', '4']
        sage: SBI = SBL.index_append("3")
        sage: SBI
        3
        sage: SBL.get_list()
        ['1', '2', '4', '3']
        sage: SBL.get_dict()
        {'1': 0, '3': 3, '2': 1, '4': 2}

    """
    def __init__(self, other_list=None):
        r"""
        """
        self.file_prefix = random_name()
        # Work around http://bugs.python.org/issue18039 not fixed in 2.7*
        self.remove_dict()
        self._index = shelve.open(self.file_prefix + ".index", flag='n')
        if other_list == None:
            self._item = []
        else:
            self._item = other_list
            for index in range(len(other_list)):
                item = other_list[index]
                self._index[item] = index


    def sync(self):
        self._index.sync()


    def close_dict(self):
        self._index.close()


    def remove_dict(self):
        for fn in glob.glob(self.file_prefix + ".index*"):
            os.remove(fn)


    def __del__(self):
        self.remove_dict()

