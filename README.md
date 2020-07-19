# Boolean-Cayley-graphs

Investigations of Boolean functions, their Cayley graphs, and associated structures.

The project enables the experimental mathematics that underpins recent and ongoing investigation into the classification of bent functions by their Cayley graphs.

This project originally began with the idea of refactoring the [bent-functions-duals-Cayley-graphs-public.sagews](https://cloud.sagemath.com/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/files/public/bent-functions-duals-Cayley-graphs-public.sagews)
worksheet, because it is too long, poorly structured, and takes so long to run that CoCalc cannot run it successfully.
It has since evolved into a Python package `boolean_cayley_graphs`, and associated scripts, Sage code, Jupyter notebooks and code that allows the results
of paper [4] below to be fully reproduced.

## Project URLs

[CoCalc](https://cocalc.com/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/files/Boolean-Cayley-graphs/?session=default): public folder of worksheets, source code and data files.

[GitHub](https://github.com/penguian/Boolean-Cayley-graphs): Git repository of source code, data and papers.

[PyPI](https://pypi.org/project/boolean-cayley-graphs): Installable Python package.

[SourceForge](https://boolean-cayley-graphs.sourceforge.io/): Documentation of Python modules in HTML format.

[NeCTAR](http://vm-130-56-248-117.nci.org.au/bfcg/): Virtual laboratory prototype .

## Installation

```
$ sage -pip install boolean_cayley_graphs --user
```

## Usage

See [SourceForge](https://boolean-cayley-graphs.sourceforge.io/): Documentation of Python modules in HTML format.

## References

1. Paul Leopardi, ["Constructions for Hadamard matrices, Clifford algebras, and their relation to amicability - anti-amicability graphs"](http://ajc.maths.uq.edu.au/pdf/58/ajc_v58_p214.pdf),
Australasian Journal of Combinatorics, Volume 58(2) (2014), pp. 214–248.

   Describes how the pattern of commuting and anticommuting pairs of basis elements of a real Clifford algebra, and their representation theory, can be used in the construction of Hadamard matrices.

2. Paul Leopardi, "Twin bent functions and Clifford algebras", in C. Colbourn (ed.) Algebraic Design Theory and Hadamard Matrices (ADTHM 2014), Springer, 2015, pp. 189-199.

   Preprint:  [arXiv:1501.05477 [math.CO]](http://arxiv.org/abs/1501.05477).

   Examines a pair of bent functions on and their relationship to a necessary condition for the existence of an automorphism of an edge-coloured graph, whose colours are defined by the properties of a canonical basis for the real representation of a real Clifford algebra.

3. Paul Leopardi, "Twin bent functions, strongly regular Cayley graphs, and Hurwitz-Radon theory", 2015.

   Preprint: [arXiv:1504.02827 [math.CO]](http://arxiv.org/abs/1504.02827).

   Uses a theorem of Radon to prove that the corresponding graphs in the two sequences of strongly regular graphs considered in [1] and [2] are not isomorphic, except in the first 3 cases.

4. Paul Leopardi, "Classifying bent functions by their Cayley graphs", v6, December 2018.

   Preprint: [arXiv:1705.04507 [math.CO]](http://arxiv.org/abs/1705.04507).

   Explores the connections between bent functions and their Cayley graphs, as well as projective two-weight linear codes, and symmetric designs with the symmetric difference property, through various equivalence classes. Includes exhaustive classifications of bent functions up to 8 dimensions and degree 3, with selected examples of degree 4

