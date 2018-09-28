r"""
"""
#*****************************************************************************
#       Copyright (C) 2016 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

import sys

from sage.all_cmdline import *

from boolean_cayley_graphs.bent_function_cayley_graph_classification import BentFunctionCayleyGraphClassification
from boolean_cayley_graphs.bent_function import BentFunction

r"""
"""
# Check that the correct number arguments exist.
if len(sys.argv) < 3:
    print "Usage: save_psf_from_parts seq_nbr fnbr [dir]"
    sys.exit(1)

# Convert the arguments to int.
seq_nbr  = int(sys.argv[1]) # Number of the partial spread function sequence
fnbr     = int(sys.argv[2]) # Function number within partial spread function sequence
d_load = None
if len(sys.argv) > 3:
    d_load = sys.argv[3]         # Directory to load parts from
d_save = None
if len(sys.argv) > 4:
    d_save = sys.argv[3]         # Directory to save to

# Construct the classification from the existing parts.
c_name = "psf"+str(seq_nbr)+"_"+str(fnbr)
c = BentFunctionCayleyGraphClassification.from_parts(c_name, directory=d_load)

# Save the classification.
c.save_mangled(c_name, directory=d_save)

# Check the saved classification
c_check = BentFunctionCayleyGraphClassification.load_mangled(c_name)
c_check.report()
if (c.algebraic_normal_form == c_check.algebraic_normal_form and
    c.cayley_graph_class_list == c_check.cayley_graph_class_list and
    c.bent_cayley_graph_index_matrix == c_check.bent_cayley_graph_index_matrix and
    c.dual_cayley_graph_index_matrix == c_check.dual_cayley_graph_index_matrix and
    c.weight_class_matrix == c_check.weight_class_matrix):
    print "Check succeeded."
else:
    print "Check failed."
    sys.exit(1)

quit

