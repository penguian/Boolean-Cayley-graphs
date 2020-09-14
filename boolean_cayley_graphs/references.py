# -*- coding: utf-8 -*-

r"""
Reference generation
====================

The ``references`` module defines
functions that generate and organize the bibliographic references for this project.

AUTHORS:

- Paul Leopardi (2017-05-20): initial version

"""
#*****************************************************************************
#       Copyright (C) 2017 Paul Leopardi paul.leopardi@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from collections import OrderedDict
from string import ascii_uppercase
from sys import stdout


bibitem = OrderedDict()

bibitem["RFC2144"] = ("""C. M. Adams.
*The cast-128 encryption algorithm.*
RFC 2144, RFC Editor, May 1997.
""")

bibitem["Ada1997"] = ("""C. M. Adams.
Constructing symmetric ciphers using the cast design procedure.
In E. Kranakis and P. Van Oorschot, editors, *Selected Areas in
Cryptography*,  71--104, Boston, MA, (1997). Springer US.
""")

bibitem["BC1999"] = ("""A. Bernasconi and B. Codenotti.
"Spectral analysis of Boolean functions as a graph eigenvalue problem".
IEEE Transactions on Computers, 48(3):345--351, (1999).
""")

bibitem["BCV2001"] = ("""A. Bernasconi, B. Codenotti, and J. M. VanderKam.
"A characterization of bent functions in terms of strongly regular graphs".
IEEE Transactions on Computers, 50(9):984--985, (2001).
""")

bibitem["Bos1963"] = ("""R. C. Bose.
"Strongly regular graphs, partial geometries and partially balanced designs".
Pacific J. Math, 13(2):389--419, (1963).
""")

bibitem["BFFWW2006"] = ("""I. Bouyukliev, V. Fack, W. Willems, and J. Winne.
"Projective two-weight codes with small parameters and their corresponding graphs".
Designs, Codes and Cryptography, 41(1):59--78, (2006).
""")

"""
Notes:
7.3 1, p 74. SDP designs. [35,6,16]_2 PTW codes and 2-(64,28,12) SDP designs,
ref [23] is [Ton1996]_.

pp. 74-75 *two* constructions of SRGs, from [Del1972]_ and
from [9] Calderbank and Kantor.
"""

bibitem["Bra2006"] = ("""A. Braeken.
*Cryptographic Properties of Boolean Functions and S-Boxes*.
Phd thesis, Katholieke Universiteit Leuven, Leuven-Heverlee, Belgium,
(2006).
""")

bibitem["BCN1989"] = ("""A. E. Brouwer, A. Cohen, and A. Neumaier.
*Distance-Regular Graphs*.
Ergebnisse der Mathematik und Ihrer Grenzgebiete, 3 Folge / A Series of
Modern Surveys in Mathematics. Springer London, (2011).
""")

bibitem["BV1992"] = ("""A. E. Brouwer and C. A. Van Eijl.
"On the p-rank of the adjacency matrices of strongly regular graphs".
Journal of Algebraic Combinatorics, 1(4):329--346, (1992).
""")

bibitem["CalK1986"] = ("""R. Calderbank and W. M. Kantor.
"The geometry of two-weight codes".
Bulletin of the London Mathematical Society, 18(2):97--122, (1986).
""")

bibitem["Car2010"] = ("""C. Carlet.
Boolean functions for cryptography and error correcting codes.
In *Boolean Models and Methods in Mathematics, Computer Science,
and Engineering*, volume 2,  257--397. Cambridge University Press, (2010).
""")

bibitem["CDPS2010"] = ("""C. Carlet, L. E. Danielsen, M. G. Parker, and P. Solé.
"Self-dual bent functions".
International Journal of Information and Coding Theory,
1(4):384--399, (2010).
""")

bibitem["CTZ2011"] = ("""Y. M. Chee, Y. Tan, and X. D. Zhang.
"Strongly regular graphs constructed from p-ary bent functions".
Journal of Algebraic Combinatorics, 34(2):251--266, (2011).
""")

bibitem["Del1972"] = ("""P. Delsarte.
"Weights of linear codes and strongly regular normed spaces".
Discrete Mathematics, 3(1-3):47--64, (1972).
""")

bibitem["Dil1974"] = ("""J. F. Dillon.
*Elementary Hadamard Difference Sets*.
PhD thesis, University of Maryland College Park, Ann Arbor, USA, (1974).
""")

bibitem["DS1987"] = ("""J. F. Dillon and J. R. Schatz.
"Block designs with the symmetric difference property".
In Proceedings of the NSA Mathematical Sciences Meetings,
159--164. US Govt. Printing Office Washington, DC, (1987).
""")

bibitem["Din2015"] = ("""C. Ding.
"Linear codes from some 2-designs".
IEEE Transactions on information theory, 61(6):3265--3275, (2015).
""")

bibitem["DD2015"] = ("""K. Ding and C. Ding.
"A class of two-weight and three-weight codes and their applications
in secret sharing".
IEEE Transactions on Information Theory, 61(11):5835--5842, (2015).
""")

bibitem["FSSW2013"] = ("""T. Feulner, L. Sok, P. Solé, and A. Wassermann.
"Towards the classification of self-dual bent functions in eight variables".
Designs, Codes and Cryptography, 68(1):395--406, (2013).
""")

bibitem["HL1994"] = ("""C. Hoede and X. Li.
"Clique polynomials and independent set polynomials of graphs".
Discrete Mathematics, 125(1):219 -- 228, (1994).
""")

bibitem["HY2004"] = ("""T. Huang and K.-H. You.
"Strongly regular graphs associated with bent functions".
In *7th International Symposium on Parallel Architectures,
Algorithms and Networks, 2004. Proceedings*,  380--383, May 2004.
""")

bibitem["JGTMMBJP2013"] = ("""D. Joyner, O. Geil, C. Thomsen, C. Munuera, I. Márquez-Corbella,
E. Martínez-Moro, M. Bras-Amorós, R. Jurrius, and R. Pellikaan.
"Sage: A basic overview for coding theory and cryptography."
In *Algebraic Geometry Modeling in Information Theory*, volume 8
of *Series on Coding Theory and Cryptology*,  1--45. World Scientific
Publishing Company, (2013).
""")

bibitem["JK2007"] = ("""T. Junttila and P. Kaski.
"Engineering an efficient canonical labeling tool for large and sparse graphs".
In D. Applegate, G. S. Brodal, D. Panario, and R. Sedgewick, editors,
*Proceedings of the Ninth Workshop on Algorithm Engineering and
Experiments and the Fourth Workshop on Analytic Algorithms and
Combinatorics*,  135--149, New Orleans, LA, (2007). Society for Industrial
and Applied Mathematics.
""")

bibitem["JK2011"] = ("""T. Junttila and P. Kaski.
"Conflict propagation and component recursion for canonical labeling".
In *Theory and Practice of Algorithms in (Computer) Systems*,
151--162. Springer, (2011).
""")

bibitem["Kan1975"] = ("""W. M. Kantor.
"Symplectic groups, symmetric designs, and line ovals".
*Journal of Algebra*, 33(1):43--58, (1975).
""")

bibitem["Kan1983"] = ("""W. M. Kantor.
"Exponential numbers of two-weight codes, difference sets and
symmetric designs".
Discrete Mathematics, 46(1):95--98, (1983).
""")

bibitem["Lan2010"] = ("""P. Langevin.
"Classification of partial spread functions in eight variables", (2010).
http://langevin.univ-tln.fr/project/spread/psp.html
Last accessed 9 May 2017.
""")

bibitem["LH2011"] = ("""P. Langevin and X.-D. Hou.
"Counting partial spread functions in eight variables".
IEEE Transactions on Information Theory, 57(4):2263--2269, (2011).
""")

bibitem["LL2011"] = ("""P. Langevin and G. Leander.
"Counting all bent functions in dimension eight 99270589265934370305785861242880."
*Designs, Codes and Cryptography*, 59(1-3):193--205, (2011).
""")

bibitem["LLM2008"] = ("""P. Langevin, G. Leander, and G. McGuire.
Kasami bent functions are not equivalent to their duals.
In G. Mullen, D. Panario, and I. Shparlinski, editors, *Finite
Fields and Applications: Eighth International Conference on Finite Fields and
Applications, July 9-13, 2007, Melbourne, Australia*, Contemporary
mathematics,  187--198. American Mathematical Society, (2008).
""")

bibitem["Leo2016GitHub"] = ("""P. Leopardi.
*Boolean-cayley-graphs*, (2016).
https://github.com/penguian/Boolean-Cayley-graphs
GitHub repository. Last accessed 9 May 2017.
""")

bibitem["Leo2016SMC"] = ("""P. Leopardi.
*Boolean-cayley-graphs*, (2016).
http://tinyurl.com/Boolean-Cayley-graphs
SageMathCloud public folder. Last accessed 9 May 2017.
""")

bibitem["Leo2017Hurwitz"] = ("""P. Leopardi.
"Twin bent functions, strongly regular Cayley graphs, and Hurwitz-Radon theory".
Submitted October 2016 to Journal of Algebra Combinatorics Discrete
Structures and Applications, accepted April 2017.
Preprint: arXiv:1504.02827 [math.CO].
""")

bibitem["Leo2017"] = ("""P. Leopardi.
"Classifying bent functions by their Cayley graphs".
2017, 2018.
Preprint: arXiv:1705.04507 [math.CO].
""")

bibitem["MP2013"] = ("""B. D. McKay and A. Piperno.
*Nauty and Traces user's guide (Version 2.5)*.
Computer Science Department, Australian National University,
Canberra, Australia, (2013).
""")

bibitem["MP2014"] = ("""B. D. McKay and A. Piperno.
"Practical graph isomorphism, II".
*Journal of Symbolic Computation*, 60:94--112, (2014).
""")

bibitem["MS1990"] = ("""W. Meier and O. Staffelbach.
"Nonlinearity criteria for cryptographic functions".
In J.-J. Quisquater and J. Vandewalle, editors, *Advances in
Cryptology --- EUROCRYPT '89: Workshop on the Theory and Application of
Cryptographic Techniques*, volume 434 of *Lecture Notes in Computer
Science*,  549--562, Berlin, Heidelberg, (1990). Springer.
""")

bibitem["Neu2006"] = ("""T. Neumann.
*Bent functions*.
PhD thesis, University of Kaiserslautern, (2006).
""")

bibitem["Rot1976"] = ("""O. S. Rothaus.
"On 'bent' functions".
Journal of Combinatorial Theory, Series A, 20(3):300--305, (1976).
""")

bibitem["Roy2008"] = ("""G. F. Royle.
"A normal non-cayley-invariant graph for the elementary abelian group of order 64".
*Journal of the Australian Mathematical Society*, 85(03):347--351, (2008).
""")

bibitem["SageMathCloud"] = ("""SageMath, Inc.
*SageMathCloud Online Computational Mathematics*, (2016).
https://cloud.sagemath.com
""")

bibitem["Sei1979"] = ("""J. J. Seidel.
"Strongly regular graphs".
In *Surveys in combinatorics (Proc. Seventh British
Combinatorial Conf., Cambridge, 1979)*, volume 38 of *London
Mathematical Society Lecture Note Series*, 157--180, Cambridge-New York,
(1979). Cambridge Univ. Press.
""")

bibitem["Sta2007"] = ("""P. Stanica.
"Graph eigenvalues and Walsh spectrum of Boolean functions".
Integers: Electronic Journal Of Combinatorial Number Theory,
7(2):A32, (2007).
""")

bibitem["Sti2007"] = ("""D. R. Stinson.
*Combinatorial designs: constructions and analysis*.
Springer Science \\& Business Media, (2007).
""")

bibitem["SageMath7517"] = ("""The Sage Developers.
*SageMath, the Sage Mathematics Software System (Version 7.5)*, (2017).
http://www.sagemath.org
""")

bibitem["Tok2015"] = ("""N. Tokareva.
*Bent functions: results and applications to cryptography*.
Academic Press, (2015).
""")

bibitem["Ton1996"] = ("""V. D. Tonchev.
"The uniformly packed binary [27, 21, 3] and [35, 29, 3] codes".
Discrete Mathematics, 149(1-3):283--288, (1996).
""")

bibitem["Ton2007"] = ("""V. D. Tonchev.
"Codes". In C. Colbourne and J. Dinitz, editors, *Handbook of
combinatorial designs*, chapter VII.1,  677--701. CRC press, second edition,
(2007).
""")


def cite(citation):
    r"""
    Look up and retrieve reference details from the `bibitem` dictionary.

    INPUT:

    - ``citation`` -- string: A citation, generally but not always
      in the form "AbcYYYY", where "Abc" is the first 3 characters of
      the author's surname, and "YYYY" is the 4 digit year.

    OUTPUT:

    The reference details as a string.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.references import cite
        sage: print(cite("Leo2017"))
        P. Leopardi.
        "Classifying bent functions by their Cayley graphs".
        2017, 2018.
        Preprint: arXiv:1705.04507 [math.CO].
    """
    return bibitem[citation]


def sage_reference(citation):
    r"""
    Retrieve reference details from the `bibitem` dictionary in a format
    similar to the way that Sage formats it own references.

    INPUT:

    - ``citation`` -- string: A citation, generally but not always
      in the form "AbcYYYY", where "Abc" is the first 3 characters of
      the author's surname, and "YYYY" is the 4 digit year.

    OUTPUT:

    The reference details as a Sage-formatted string.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.references import sage_reference
        sage: print(sage_reference("Leo2017"))
        .. [Leo2017] \P. Leopardi.
                    "Classifying bent functions by their Cayley graphs".
                    2017, 2018.
                    Preprint: arXiv:1705.04507 [math.CO].
    """
    bibitem_lines = bibitem[citation].splitlines()
    sage_bibitem_lines = (
        [bibitem_lines[0]] +
        ["            " + line for line in bibitem_lines[1:]])
    return (
        ".. [" + citation + "] \\" + '\n'.join(sage_bibitem_lines))


def print_sage_references():
    r"""
    Retrieve all reference details from the `bibitem` dictionary and print them
    in a format similar to the way that Sage formats it own references.

    INPUT:

    None.

    OUTPUT:

    All reference details in `bibitem` as a Sage-formatted string.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.references import print_sage_references
        sage: print_sage_references()
        .. [RFC2144] \C. M. Adams.
                    *The cast-128 encryption algorithm.*
                    RFC 2144, RFC Editor, May 1997.
        ...
        .. [Ton2007] \V. D. Tonchev.
                    "Codes". In C. Colbourne and J. Dinitz, editors, *Handbook of
                    combinatorial designs*, chapter VII.1,  677--701. CRC press, second edition,
                    (2007).
    """
    for citation in bibitem.keys():
        print(sage_reference(citation))
        print()


def print_sage_references_index_rst(file=stdout):
    r"""
    Retrieve all reference details from the `bibitem` dictionary and print them
    in the format expected by Sphinx for the file `index.rst`.

    INPUT:

    - ``file`` -- file, optional. The file to which the reference details are
      to be printed. Default is stdout.

    OUTPUT:

    All reference details in `bibitem` as a Sage-formatted string.

    EXAMPLES:

    ::

        sage: from boolean_cayley_graphs.references import print_sage_references_index_rst
        sage: print_sage_references_index_rst()
        References
        ==========
        <BLANKLINE>
        References, sorted alphabetically by first author.
        <BLANKLINE>
        :ref:`A <ref-A>`
        ...
        :ref:`T <ref-T>`
        <BLANKLINE>
        .. _ref-A:
        <BLANKLINE>
        **A**
        <BLANKLINE>
        .. [Ada1997] \C. M. Adams.
                    Constructing symmetric ciphers using the cast design procedure.
                    In E. Kranakis and P. Van Oorschot, editors, *Selected Areas in
                    Cryptography*,  71--104, Boston, MA, (1997). Springer US.
        ...
        .. [Ton2007] \V. D. Tonchev.
                    "Codes". In C. Colbourne and J. Dinitz, editors, *Handbook of
                    combinatorial designs*, chapter VII.1,  677--701. CRC press, second edition,
                    (2007).
    """
    print("References", file=file)
    print("==========", file=file)
    print("", file=file)
    print("References, sorted alphabetically by first author.", file=file)
    print("", file=file)
    citations_starting_with = dict()
    for letter in ascii_uppercase:
        citations_starting_with[letter] = [
            cite for cite in bibitem.keys() if cite[0] == letter]
        if len(citations_starting_with[letter]) > 0:
            print(":ref:`"+letter+" <ref-"+letter+">`", file=file)
    print("", file=file)
    for letter in ascii_uppercase:
        if len(citations_starting_with[letter]) > 0:
            print(".. _ref-"+letter+":", file=file)
            print("", file=file)
            print("**"+letter+"**", file=file)
            print("", file=file)
            for citation in citations_starting_with[letter]:
                print(sage_reference(citation), file=file)
                print("", file=file)
