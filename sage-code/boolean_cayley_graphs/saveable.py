r"""
A mixin class with methods that load and save SageObject objects with standardized names.


AUTHORS:

- Paul Leopardi (2016-08-04): initial version
- Paul Leopardi (2017-04-01): saveable.py based on persistent.py

"""

#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.structure.sage_object import load


class Saveable(object):
    r"""
    """


    @classmethod
    def mangled_name(cls, name):
        r"""
        """
        return cls.__name__ + "__" + name


    @classmethod
    def load_mangled(cls, name):
        r"""
        """
        return load(cls.mangled_name(name))


    def save_mangled(self, name):
        r"""
        """
        self.save(self.__class__.mangled_name(name))

