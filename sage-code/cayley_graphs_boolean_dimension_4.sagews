︠62a40188-3970-4cce-97b0-5c9b45dabef7si︠
%typeset_mode True
︡347189a2-e12f-48a5-81cd-42d33342b57f︡{"done":true}︡
︠2de0af70-22b0-4f02-9da2-11b4e9d87e1b︠
%md
# Cayley graphs of binary bent functions of dimension 4.
︡42ea9d0b-47fb-4460-8b4c-5af91845ad4f︡{"done":true,"md":"# Cayley graphs of binary bent functions of dimension 4."}
︠0dbcadda-44a8-46a8-8f9c-2608ba1b054bs︠
load("boolean_dimension_cayley_graph_classifications.sage")
︡5cbfe9bf-6e36-4432-8f3f-82ab2c504baf︡{"done":true}︡
︠6a9760de-9316-46d4-9c91-d4579ef24a78i︠
%md
Save all of the classifications for dimension 4, based on `"bent_function_extended_affine_representative_polynomials.sage"`.
Set `c` to be the list of these classifications, starting from 1. `c[0]` is `None`.
︡51e5bb0d-b308-4798-b41e-5a701b499c13︡{"done":true,"md":"Save all of the classifications for dimension 4, based on `\"bent_function_extended_affine_representative_polynomials.sage\"`.\nSet `c` to be the list of these classifications, starting from 1. `c[0]` is `None`."}
︠98ed0bfd-b764-4224-b2a7-df6cf05aaf4es︠
c = save_boolean_dimension_cayley_graph_classifications(4)
︡e68618cc-b31e-4c19-96a2-add5a3419908︡{"done":true}︡
︠a4d0250c-e19a-4860-a47f-1c36364dbcf6s︠
len(c)-1
︡25498e1a-f268-42ca-ba2b-2bb77f6773cc︡{"html":"<div align='center'>$\\displaystyle 1$</div>"}︡{"done":true}︡
︠75fc02cd-adb1-4c8d-8d4a-a290214c8007i︠
%md
Show the type of the classification `c[1]`.
︡c9e1a861-7ddf-49e7-bbae-cc2c53aeb02a︡{"done":true,"md":"Show the type of the classification `c[1]`."}
︠33c057ae-710b-4455-9ba2-ff4140abb4f9s︠
type(c[1])
︡d2a9abdf-e972-4ed8-a1ed-5127878844a7︡{"stdout":"<class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>\n"}︡{"done":true}︡
︠5cd5963d-65a2-45a9-a22f-73018a4809a0i︠
%md
Show the internal structure of the classification `c[1]`.
︡dc7e80a4-651b-4665-9cbd-0a88943c51ae︡{"done":true,"md":"Show the internal structure of the classification `c[1]`."}
︠d43c18cf-8d63-4a25-91bd-151823a7f265s︠
c[1].__dict__
︡69a18bf7-a877-482d-bdbc-5cd98a267dbd︡{"stdout":"{'_default_filename': 'BentFunctionCayleyGraphClassification__p4_1.sobj', 'dual_cayley_graph_index_matrix': [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]\n[0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]\n[0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]\n[1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]\n[0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]\n[0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]\n[0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]\n[1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]\n[0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]\n[0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]\n[0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]\n[1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]\n[1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]\n[1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]\n[1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]\n[0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0], 'weight_class_matrix': [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]\n[0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]\n[0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]\n[1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]\n[0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]\n[0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]\n[0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]\n[1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]\n[0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]\n[0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]\n[0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]\n[1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]\n[1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]\n[1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]\n[1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]\n[0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0], 'bent_cayley_graph_index_matrix': [0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]\n[0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]\n[0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]\n[1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]\n[0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]\n[0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]\n[0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]\n[1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]\n[0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]\n[0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]\n[0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]\n[1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]\n[1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]\n[1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]\n[1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]\n[0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0], 'algebraic_normal_form': x0*x1 + x2*x3, 'cayley_graph_class_list': ['OJCiWodO{BrGhHodppF_P', 'OJ\\\\{|]vm}]YtufxZ\\\\J^`n']}\n"}︡{"done":true}︡
︠a7424806-05a8-478d-b87b-12d5924eeed2i︠
%md
Produce a report on the classification `c[1]`.
︡fe91be4f-ebc2-43f1-9a18-439e2d33ddad︡{"done":true,"md":"Produce a report on the classification `c[1]`."}
︠e6a76c34-5584-4a15-8191-f2477eb134f4s︠
c[1].report()
︡89133a91-b5c7-477b-8170-f963399d0c2c︡{"stdout":"Algebraic normal form of Boolean function: x0*x1 + x2*x3\nFunction is bent.\n\nWeight class matrix:\n[0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]\n[0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]\n[0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]\n[1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]\n[0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]\n[0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]\n[0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]\n[1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]\n[0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]\n[0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]\n[0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]\n[1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]\n[1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]\n[1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]\n[1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]\n[0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]\n\nSDP design incidence structure t-design parameters: (True, (2, 16, 6, 2))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n[0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0]\n[0 1 0 0 0 1 0 0 0 1 0 0 1 0 1 1]\n[0 0 1 0 0 0 1 0 0 0 1 0 1 1 0 1]\n[1 0 0 0 1 0 0 0 1 0 0 0 0 1 1 1]\n[0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1]\n[0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0]\n[0 0 1 0 1 1 0 1 0 0 1 0 0 0 1 0]\n[1 0 0 0 0 1 1 1 1 0 0 0 1 0 0 0]\n[0 0 0 1 0 0 0 1 1 1 1 0 0 0 0 1]\n[0 1 0 0 0 1 0 0 1 0 1 1 0 1 0 0]\n[0 0 1 0 0 0 1 0 1 1 0 1 0 0 1 0]\n[1 0 0 0 1 0 0 0 0 1 1 1 1 0 0 0]\n[1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1]\n[1 0 1 1 0 1 0 0 0 1 0 0 0 1 0 0]\n[1 1 0 1 0 0 1 0 0 0 1 0 0 0 1 0]\n[0 1 1 1 1 0 0 0 1 0 0 0 1 0 0 0]\n\nThere are 2 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1 + x2*x3\nClique polynomial: 8*t^4 + 32*t^3 + 48*t^2 + 16*t + 1\nStrongly regular parameters: (16, 6, 2, 2)\nRank: 6 Order: 1152\n\nLinear code from representative:\n[6, 4] linear code over GF(2)\nGenerator matrix:\n[1 0 0 0 0 1]\n[0 1 0 1 0 0]\n[0 0 1 1 0 0]\n[0 0 0 0 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 2: 6, 4: 9}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1 + x0 + x1 + x2*x3\nClique polynomial: 16*t^5 + 120*t^4 + 160*t^3 + 80*t^2 + 16*t + 1\nStrongly regular parameters: (16, 10, 6, 6)\nRank: 6 Order: 1920\n\nLinear code from representative:\n[10, 4] linear code over GF(2)\nGenerator matrix:\n[1 0 1 0 1 0 0 1 0 0]\n[0 1 1 0 1 1 0 1 1 0]\n[0 0 0 1 1 1 0 0 0 1]\n[0 0 0 0 0 0 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 4: 5, 6: 10}\n"}︡{"done":true}︡
︠2035fa5c-dc40-4344-bcb7-b582201c5765s︠
c[1].algebraic_normal_form
︡6f89e6c5-2b07-4508-ae58-c1bd9a691337︡{"html":"<div align='center'>$\\displaystyle x_{0} x_{1} + x_{2} x_{3}$</div>"}︡{"done":true}︡
︠5f7ba64c-9491-4365-9520-87064981f913s︠
matrix_plot(c[1].weight_class_matrix,cmap='gist_stern')
︡580a092b-4066-440b-a644-47ca02f16c99︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/24418/tmp_IgDq3k.svg","show":true,"text":null,"uuid":"f4734d67-bf2f-4eb7-aa17-5351f8b31d6b"},"once":false}︡{"done":true}︡
︠28af0dcb-9270-463d-a316-557954d57a64s︠
matrix_plot(c[1].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡b9ab6b13-bce0-47d6-ab41-149f806470e0︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/24418/tmp_v3ZunI.svg","show":true,"text":null,"uuid":"4a11fafc-c422-4ac0-b86d-3498450d4c7c"},"once":false}︡{"done":true}︡
︠d35b0383-da06-4c7c-8254-5e95791bf5acs︠
matrix_plot(c[1].dual_cayley_graph_index_matrix,cmap='gist_stern')
︡83256887-67ed-4679-b58c-81510797acf6︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/24418/tmp_0bJlhz.svg","show":true,"text":null,"uuid":"3f84ec50-460f-46d4-9ddb-7556f8ca2ed4"},"once":false}︡{"done":true}︡
︠4f022867-96ca-4fc9-a8b3-ca3aa2d71b39s︠
︡a00b4739-d85d-4dd5-a87a-88486d2a50a7︡{"done":true}︡
︠430a8618-be5c-48f9-bafc-7b3f7a16b7efs︠

︡5c8cc32c-1118-4ed9-98ff-bc7de2410b8d︡{"done":true}︡









