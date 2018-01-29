︠62a40188-3970-4cce-97b0-5c9b45dabef7si︠
%typeset_mode True
︡098c2ad3-6c21-4088-b053-9569dc64d023︡{"done":true}︡
︠803356c6-a2c0-4b86-bfdc-5b279e4319f1i︠
%md
# Cayley graphs of binary bent functions of dimension 2.
︡e56b0877-1c07-458f-ab66-44210031914b︡{"done":true,"md":"# Cayley graphs of binary bent functions of dimension 2."}
︠0dbcadda-44a8-46a8-8f9c-2608ba1b054bs︠
load("boolean_dimension_cayley_graph_classifications.sage")
︡414e1bc7-2b46-4439-8a0e-39e15a73ee20︡{"done":true}︡
︠6a9760de-9316-46d4-9c91-d4579ef24a78i︠
%md
Save all of the classifications for dimension 2, based on `"bent_function_extended_affine_representative_polynomials.sage"`.
Set `c` to be the list of these classifications, starting from 1. `c[0]` is `None`.
︡51e5bb0d-b308-4798-b41e-5a701b499c13︡{"done":true,"md":"Save all of the classifications for dimension 2, based on `\"bent_function_extended_affine_representative_polynomials.sage\"`.\nSet `c` to be the list of these classifications, starting from 1. `c[0]` is `None`."}
︠98ed0bfd-b764-4224-b2a7-df6cf05aaf4es︠
c = save_boolean_dimension_cayley_graph_classifications(2)
︡67c92539-1da0-438d-aa1a-91b1e6bde4b9︡{"done":true}︡
︠a4d0250c-e19a-4860-a47f-1c36364dbcf6s︠
len(c)-1
︡347805e4-6228-46c0-9046-898b2745396f︡{"html":"<div align='center'>$\\displaystyle 1$</div>"}︡{"done":true}︡
︠75fc02cd-adb1-4c8d-8d4a-a290214c8007i︠
%md
Show the type of the classification `c2[1]`.
︡c9e1a861-7ddf-49e7-bbae-cc2c53aeb02a︡{"done":true,"md":"Show the type of the classification `c2[1]`."}
︠33c057ae-710b-4455-9ba2-ff4140abb4f9s︠
type(c[1])
︡f422e3aa-50e2-41a5-9595-7c373600b5b7︡{"stdout":"<class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>\n"}︡{"done":true}︡
︠5cd5963d-65a2-45a9-a22f-73018a4809a0i︠
%md
Show the internal structure of the classification `c[1]`.
︡dc7e80a4-651b-4665-9cbd-0a88943c51ae︡{"done":true,"md":"Show the internal structure of the classification `c[1]`."}
︠d43c18cf-8d63-4a25-91bd-151823a7f265s︠
c[1].__dict__
︡2ad4c31d-1d40-4562-a4d3-2c4d754656f7︡{"stdout":"{'_default_filename': 'BentFunctionCayleyGraphClassification__p2_1.sobj', 'dual_cayley_graph_index_matrix': [0 0 0 1]\n[0 1 0 0]\n[0 0 1 0]\n[1 0 0 0], 'weight_class_matrix': [0 0 0 1]\n[0 1 0 0]\n[0 0 1 0]\n[1 0 0 0], 'bent_cayley_graph_index_matrix': [0 0 0 1]\n[0 1 0 0]\n[0 0 1 0]\n[1 0 0 0], 'algebraic_normal_form': x0*x1, 'cayley_graph_class_list': ['CK', 'C~']}\n"}︡{"done":true}︡
︠a7424806-05a8-478d-b87b-12d5924eeed2i︠
%md
Produce a report on the classification `c[1]`.
︡fe91be4f-ebc2-43f1-9a18-439e2d33ddad︡{"done":true,"md":"Produce a report on the classification `c[1]`."}
︠e6a76c34-5584-4a15-8191-f2477eb134f4s︠
c[1].report()
︡8f453853-71be-4e93-937b-bf2107e02992︡{"stdout":"Algebraic normal form of Boolean function: x0*x1\nFunction is bent.\n\nWeight class matrix:\n[0 0 0 1]\n[0 1 0 0]\n[0 0 1 0]\n[1 0 0 0]\n\nSDP design incidence structure t-design parameters: (True, (1, 4, 1, 1))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n[0 0 0 1]\n[0 1 0 0]\n[0 0 1 0]\n[1 0 0 0]\n\nThere are 2 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1\nClique polynomial: 2*t^2 + 4*t + 1\nStrongly regular parameters: (4, 1, 0, 0)\nRank: 4 Order:"}︡{"stdout":" "}︡{"stdout":"8\n\nLinear code from representative:\n[1, 1] linear code over GF(2)\nGenerator matrix:\n[1]\nLinear code is projective.\nWeight distribution: {0: 1, 1: 1}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1 + x0 + x1\nClique polynomial: t^4 + 4*t^3 + 6*t^2 + 4*t + 1\nStrongly regular parameters: False\nRank: 4 Order: 24\n\nLinear code from representative:\n[3, 2] linear code over GF(2)\nGenerator matrix:\n[1 0 1]\n[0 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 2: 3}\n"}︡{"done":true}︡
︠2035fa5c-dc40-4344-bcb7-b582201c5765s︠
c[1].algebraic_normal_form
︡9c5d12f1-cda5-488f-9210-a8018572d7d6︡{"html":"<div align='center'>$\\displaystyle x_{0} x_{1}$</div>"}︡{"done":true}︡
︠5f7ba64c-9491-4365-9520-87064981f913s︠
matrix_plot(c[1].weight_class_matrix,cmap='gist_stern')
︡dbc6910c-c7ea-4f5b-b4b6-2e05a8021356︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/23310/tmp_nDHHSQ.svg","show":true,"text":null,"uuid":"a83c0fa5-ab62-436e-af4c-249c93202a84"},"once":false}︡{"done":true}︡
︠28af0dcb-9270-463d-a316-557954d57a64s︠
matrix_plot(c[1].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡16ec9960-c3a3-4d9d-8f01-6918e66a4d68︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/23310/tmp_0_TkTx.svg","show":true,"text":null,"uuid":"08650b40-8b6e-43a6-8afc-5fe3bd5f8274"},"once":false}︡{"done":true}︡
︠2eebe003-b521-4e7b-b036-680c0ac0fca1s︠
matrix_plot(c[1].dual_cayley_graph_index_matrix,cmap='gist_stern')
︡9b7a5f2f-eb35-44b3-a033-c887293d0bba︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/23310/tmp_jsRxjP.svg","show":true,"text":null,"uuid":"961e127f-c713-4e18-902f-2b4193d4e624"},"once":false}︡{"done":true}︡
︠3fe4270f-c4f8-4df3-a1e2-1cdecded6afes︠
︡626133a4-9119-4068-b00f-b712ae54e9cd︡{"done":true}︡
︠245c7b8a-d0b7-4a6c-b249-41e070720f09s︠

︡1aa26535-7ea7-402c-aa6a-b12240b63439︡{"done":true}︡









