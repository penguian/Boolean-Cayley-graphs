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
import shelve

from sage.misc.temporary_file import tmp_filename

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
            sage: L.index_append(2)
            1
            sage: L
            [1, 2, 4]
            sage: L.index_append(3)
            3
            sage: L
            [1, 2, 4, 3]
            sage: del L
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

    EXAMPLES:

    Initialize from a list.

    ::

        sage: from boolean_cayley_graphs.containers import BijectiveList
        sage: BL = BijectiveList(["1","2","3"])
        sage: BL.get_list()
        ['1', '2', '3']
        sage: BL.get_dict()
        {'1': 0, '2': 1, '3': 2}
        sage: del BL
    """
    def __init__(self, other_list=None):
        r"""
        Constructor.

        EXAMPLES:

        Default initialization.

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList()
            sage: BL.get_list()
            []
            sage: BL.get_dict()
            {}
            sage: del BL

        TESTS:

        Initialize from a list.

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList(["1","2","6"])
            sage: BL.get_list()
            ['1', '2', '6']
            sage: BL.get_dict()
            {'1': 0, '2': 1, '6': 2}
            sage: del BL
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

        INPUT:

        - ``self`` -- the current object.
        - ``index`` -- the index to look up.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,3])
            sage: BL[2]
            3
            sage: del BL
        """
        return self._item[index]


    def __len__(self):
        r"""
        Get the length of the list.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,3])
            sage: len(BL)
            3
            sage: del BL
        """
        return len(self._item)


    def get_dict(self):
        r"""
        Get the dict part of the BijectiveList.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,5])
            sage: BL.get_dict()
            {1: 0, 2: 1, 5: 2}
            sage: del BL
        """
        return self._index


    def get_list(self):
        r"""
        Get the list part of the BijectiveList.

        INPUT:

        - ``self`` -- the current object.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,5])
            sage: BL.get_list()
            [1, 2, 5]
            sage: del BL

        """
        return self._item


    def index(self,item):
        r"""
        Return the index of a given item.

        Use a dict lookup using _index instead of calling index() on the list.
        If the dict lookup yields a KeyError then raise a ValueError.

        INPUT:

        - ``self`` -- the current object.
        - ``item`` -- the item to look up.

        OUTPUT:

        A non-negative integer indicating the index of ``item`` within ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,4])
            sage: BL.index(2)
            1
            sage: BL.get_list()
            [1, 2, 4]
            sage: BL.get_dict()
            {1: 0, 2: 1, 4: 2}
            sage: del BL

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,4])
            sage: try:
            ....:     BL.index(3)
            ....: except ValueError as e:
            ....:     print("ValueError: {0}".format(e.args[0]))
            ....: finally:
            ....:     del BL
            ValueError: 3 is not in list
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

        INPUT:

        - ``self`` -- the current object.
        - ``item`` -- the item to look up, and append if necessary.

        OUTPUT:

        A non-negative integer indicating the index of ``item`` within ``self``.

        EFFECT:

        The item ``item`` may be appended to ``self``.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList([1,2,4])
            sage: BL.index_append(2)
            1
            sage: BL.get_list()
            [1, 2, 4]
            sage: BL.index_append(3)
            3
            sage: BL.get_list()
            [1, 2, 4, 3]
            sage: BL.get_dict()
            {1: 0, 2: 1, 3: 3, 4: 2}
            sage: del BL
        """
        try:
            result = self._index[item]
        except KeyError:
            result = len(self._item)
            self._item.append(item)
            self._index[item] = result
        return result


    def sync(self):
        r"""
        Dummy method to match the interface of ShelveBijectiveList.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList(["1","2","6"])
            sage: BL.sync()
            sage: del BL
        """
        pass


    def close_dict(self):
        r"""
        Dummy method to match the interface of ShelveBijectiveList.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList(["1","2","6"])
            sage: BL.close_dict()
            sage: BL.remove_dict()
        """
        pass


    def remove_dict(self):
        r"""
        Remove the dictionary.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList(["1","2","6"])
            sage: BL.close_dict()
            sage: BL.remove_dict()
            sage: try:
            ....:     BL._index
            ....: except AttributeError:
            ....:     pass
        """
        try:
            del self._index
        except AttributeError:
            pass


    def __del__(self):
        r"""
        Clean up by closing and removing the dictionary,
        before deleting the current object.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import BijectiveList
            sage: BL = BijectiveList(["1","2","6"])
            sage: del BL
            sage: try:
            ....:     BL
            ....: except NameError:
            ....:     pass
        """
        self.close_dict()
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

    Initialize from a list.

    ::

        sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
        sage: SBL = ShelveBijectiveList(["1","2","4"])
        sage: SBL.get_list()
        ['1', '2', '4']
        sage: SBL.get_dict()
        {'1': 0, '2': 1, '4': 2}
        sage: del SBL
    """
    def __init__(self, other_list=None):
        r"""
        Constructor.

        EXAMPLES:

        Default initialization.

        ::

            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList()
            sage: SBL.get_list()
            []
            sage: SBL.get_dict()
            {}
            sage: del SBL

        TESTS:

        Initialize from a list.

        ::

            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList(["1","2","6"])
            sage: SBL.get_list()
            ['1', '2', '6']
            sage: SBL.get_dict()
            {'1': 0, '2': 1, '6': 2}
            sage: del SBL
        """
        self.shelve_file_name = tmp_filename(ext=".index")
        # Work around http://bugs.python.org/issue18039 not fixed in 2.7*
        self.remove_dict()
        self._index = shelve.open(self.shelve_file_name, flag='n')
        if other_list == None:
            self._item = []
        else:
            self._item = other_list
            for index in range(len(other_list)):
                item = other_list[index]
                self._index[item] = index


    def sync(self):
        r"""
        Synchronize the persistent dictionary on disk, if feasible.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList(["1","2","6"])
            sage: SBL.sync()
            sage: del SBL
         """
        self._index.sync()


    def close_dict(self):
        r"""
        Synchronize and close the persistent dictionary on disk.

        TESTS:

        ::

            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList(["1","2","6"])
            sage: SBL.close_dict()
            sage: SBL.remove_dict()
        """
        self._index.close()


    def remove_dict(self):
        r"""
        Remove the files used for the persistent dictionary on disk.

        .. WARNING::

            Use close_dict() first.

        TESTS:

        ::

            sage: import glob
            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList(["1","2","6"])
            sage: SBL.close_dict()
            sage: SBL.remove_dict()
            sage: glob.glob(SBL.shelve_file_name + "*")
            []
        """
        for file_name in glob.glob(self.shelve_file_name + "*"):
            if os.path.isfile(file_name):
                os.remove(file_name)


    def __del__(self):
        r"""
        Clean up by closing the persistent dictionary on disk, and
        removing the files used for it, before deleting the current object.

        TESTS:

        ::

            sage: import glob
            sage: from boolean_cayley_graphs.containers import ShelveBijectiveList
            sage: SBL = ShelveBijectiveList(["1","2","6"])
            sage: shelve_file_name = SBL.shelve_file_name
            sage: del SBL
            sage: glob.glob(shelve_file_name + "*")
            []
            sage: try:
            ....:     SBL
            ....: except NameError:
            ....:     pass
        """
        self.close_dict()
        self.remove_dict()

