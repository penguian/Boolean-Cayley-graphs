r"""
A mixin class with methods that load and save objects with standardized names.

AUTHORS:

- Paul Leopardi (2016-08-04): initial version
- Paul Leopardi (2017-04-01): saveable.py based on persistent.py

"""
#*****************************************************************************
#       Copyright (C) 2016-2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import os
import os.path

from sage.structure.sage_object import load


class Saveable(object):
    r"""
    A mixin class with methods that load and save objects with standardized names.
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
            The default value of Noe means the current directory.

        EXAMPLES:

        ::
            sage: from boolean_cayley_graphs.saveable import Saveable
            sage: class ListSaveable(list, Saveable):
            ....:     def __init__(self, value):
            ....:         list.__init__(self, value)
            ....:
            sage: print ListSaveable.mangled_name('a')
            ListSaveable__a
            sage: print ListSaveable.mangled_name('a',directory='b')
            b/ListSaveable__a
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

        """
        return cls(load(cls.mangled_name(name, directory)))


    @classmethod
    def remove_mangled(cls, name, directory=None):
        r"""
        Remove a saved object based on its standardized name.

        """
        file_name = cls.mangled_name(name, directory) + ".sobj"
        if os.path.isfile(file_name):
            os.remove(file_name)


    def save_mangled(self, name, directory=None):
        r"""
        Save an object using its standardized name.


        """
        self.save(self.__class__.mangled_name(name, directory))


