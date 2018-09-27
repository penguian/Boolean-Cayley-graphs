r"""
The ``saveable`` module defines the ``Savable`` class:
a mixin class with methods that load and save Sage objects with standardized names.

AUTHORS:

- Paul Leopardi (2016-08-04): initial version
- Paul Leopardi (2017-04-01): saveable.py based on persistent.py

"""
#*****************************************************************************
#       Copyright (C) 2016-2018 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import os
import os.path

from sage.misc.persist import load, save


class Saveable(object):
    r"""
    A mixin class with methods that load and save objects with standardized names.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.saveable import Saveable
        sage: class ListSaveable(list, Saveable):
        ....:     def __init__(self, value):
        ....:         list.__init__(self, value)
        ....:
        sage: a = ListSaveable([1])
        sage: a[0]
        1
    """


    @classmethod
    def mangled_name(cls, name, directory=None):
        r"""
        Convert a name for an object into a standardized name.

        INPUT:

        - ``cls`` -- The current class.
        - ``name`` -- The name for the object.
        - ``directory`` -- (Optional, default=None)
            The directory name to be used for the file name of the object.
            The default value of None means the current directory.

        OUTPUT:

        A string containing the directory path and the standardized name.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.saveable import Saveable
            sage: class ListSaveable(list, Saveable):
            ....:     def __init__(self, value):
            ....:         list.__init__(self, value)
            ....:
            sage: ListSaveable.mangled_name('a')
            'ListSaveable__a'
            sage: ListSaveable.mangled_name('a', directory='b')
            'b/ListSaveable__a'
        """
        standardized_name = cls.__name__ + "__" + name
        if directory == None:
            return standardized_name
        else:
            return os.path.join(directory, standardized_name)


    @classmethod
    def load_mangled(cls, name, directory=None):
        r"""
        Load an object based on its standardized name.

        INPUT:

        - ``cls`` -- the class object.
        - ``name`` -- string: the file name suffix (without ".obj")
          part of the standardized name.
        - ``directory`` -- string, optional. The directory where the object
          was saved. Default is None, meaning the current directory.

        OUTPUT:

        The object that was saved in the file referred to by the
        standardized name and the directory.

        EXAMPLES:

        ::

            sage: import os
            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved as BFI
            sage: a = BFI([0,1,0,0])
            sage: d = tmp_dir()
            sage: a.save_mangled("a", directory=d)
            sage: b = BFI.load_mangled("a", directory=d)
            sage: a == b
            True
            sage: BFI.remove_mangled("a", directory=d)
            sage: os.rmdir(d)
        """
        return cls(load(cls.mangled_name(name, directory=directory)))


    @classmethod
    def remove_mangled(cls, name, directory=None):
        r"""
        Remove a saved object based on its standardized name.

        INPUT:

        - ``cls`` -- the class object.
        - ``name`` -- string: the file name suffix (without ".obj")
          part of the standardized name.
        - ``directory`` -- string, optional. The directory where the object
          was saved. Default is None, meaning the current directory.

        OUTPUT:

        None.

        EFFECT:

        The file containing the saved object is deleted.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved as BFI
            sage: a = BFI([0,1,0,0])
            sage: d = tmp_dir()
            sage: a.save_mangled("a", directory=d)
            sage: file_name = BFI.mangled_name("a.sobj", directory=d)
            sage: os.path.isfile(file_name)
            True
            sage: BFI.remove_mangled("a", directory=d)
            sage: os.path.isfile(file_name)
            False
            sage: os.rmdir(d)
        """
        file_name = cls.mangled_name(name + ".sobj", directory=directory)
        if os.path.isfile(file_name):
            os.remove(file_name)


    def save_mangled(self, name, directory=None):
        r"""
        Save an object using its standardized name.

        INPUT:

        - ``self`` -- the current object.
        - ``name`` -- string: the file name suffix (without ".obj")
          part of the standardized name.
        - ``directory`` -- string, optional. The directory where the object
          is to be saved. Default is None, meaning the current directory.

        OUTPUT:

        None.

        EFFECT:

        A file is created and the object ``self`` is saved into the file.

        EXAMPLES:

        ::

            sage: from boolean_cayley_graphs.boolean_function_improved import BooleanFunctionImproved as BFI
            sage: a = BFI([0,1,0,0])
            sage: d = tmp_dir()
            sage: a.save_mangled("a", directory=d)
            sage: file_name = BFI.mangled_name("a.sobj", directory=d)
            sage: os.path.isfile(file_name)
            True
            sage: BFI.remove_mangled("a", directory=d)
            sage: os.rmdir(d)
        """
        save(self, self.__class__.mangled_name(
            name,
            directory=directory))
