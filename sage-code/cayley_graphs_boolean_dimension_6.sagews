︠62a40188-3970-4cce-97b0-5c9b45dabef7sir︠
%typeset_mode True
︡5aefb0ba-5cf5-400f-b8df-a794ec91578b︡
︠c4a3aebc-07c7-4137-8c46-76dfd88ed80ai︠
%md
# Cayley graphs of binary bent functions of dimension 6.
︡ae60f69b-a9b4-4f85-af90-7e9efcdef735︡{"done":true,"md":"# Cayley graphs of binary bent functions of dimension 6."}
︠0dbcadda-44a8-46a8-8f9c-2608ba1b054bs︠
load("boolean_dimension_cayley_graph_classifications.sage")
︡169c8d2b-8484-4aa0-8155-6bf20f74f22b︡{"done":true}︡
︠00586feb-1239-45ff-8ebf-ece110e22385i︠
%md
Import the controls module so that the time for the following operations can be shown. Enable the display of time.
︡7c952b08-92d4-4b45-a88f-ba16da6927d4︡{"done":true,"md":"Import the controls module so that the time for the following operations can be shown. Enable the display of time."}
︠d9455086-c462-408e-a50f-35ba7436bbdds︠
import boolean_cayley_graphs.cayley_graph_controls as controls
controls.timing = True
︡0b8f42ee-38b1-4a62-b2e8-1dc1f4d55517︡{"done":true}︡
︠6a9760de-9316-46d4-9c91-d4579ef24a78︠
%md
Save all of the classifications for dimension 6, based on `"bent_function_extended_affine_representative_polynomials.sage"`.
Set `c` to be the list of these classifications, starting from 1. `c[0]` is `None`.

Each line of the timing information below shows the current time, the current row -- 0 to 63, and the number of extended Cayley classes found so far.
︡51e5bb0d-b308-4798-b41e-5a701b499c13︡{"done":true,"md":"Save all of the classifications for dimension 6, based on `\"bent_function_extended_affine_representative_polynomials.sage\"`.\nSet `c` to be the list of these classifications, starting from 1. `c[0]` is `None`.\n\nEach line of the timing information below shows the current time, the current row -- 0 to 63, and the number of extended Cayley classes found so far."}
︠98ed0bfd-b764-4224-b2a7-df6cf05aaf4es︠
sage_server.MAX_OUTPUT_MESSAGES = 300
c = save_boolean_dimension_cayley_graph_classifications(6)
︡df971d31-336f-4ab3-a43d-5037dbd53fc4︡{"stdout":"2017-05-06 02:57:14.338114 0 0\n2017-05-06 02:57:17.858057"}︡{"stdout":" 1 2\n2017-05-06 02:57:21.492273"}︡{"stdout":" 2 2\n2017-05-06 02:57:24.925958"}︡{"stdout":" 3 2\n2017-05-06 02:57:28.308339"}︡{"stdout":" 4 2\n2017-05-06 02:57:31.644064"}︡{"stdout":" 5 2\n2017-05-06 02:57:34.932377"}︡{"stdout":" 6 2\n2017-05-06 02:57:38.233048"}︡{"stdout":" 7 2\n2017-05-06 02:57:41.559879"}︡{"stdout":" 8 2\n2017-05-06 02:57:44.859109"}︡{"stdout":" 9 2\n2017-05-06 02:57:48.216253"}︡{"stdout":" 10 2\n2017-05-06 02:57:51.526914"}︡{"stdout":" 11 2\n2017-05-06 02:57:54.813409"}︡{"stdout":" 12 2\n2017-05-06 02:57:58.064567"}︡{"stdout":" 13 2\n2017-05-06 02:58:01.288779"}︡{"stdout":" 14 2\n2017-05-06 02:58:04.739659"}︡{"stdout":" 15 2\n2017-05-06 02:58:08.017131"}︡{"stdout":" 16 2\n2017-05-06 02:58:11.237898"}︡{"stdout":" 17 2\n2017-05-06 02:58:14.489104"}︡{"stdout":" 18 2\n2017-05-06 02:58:17.825219"}︡{"stdout":" 19 2\n2017-05-06 02:58:21.044478"}︡{"stdout":" 20 2\n2017-05-06 02:58:24.336474"}︡{"stdout":" 21 2\n2017-05-06 02:58:27.706370"}︡{"stdout":" 22 2\n2017-05-06 02:58:31.181929"}︡{"stdout":" 23 2\n2017-05-06 02:58:34.446237"}︡{"stdout":" 24 2\n2017-05-06 02:58:37.728852"}︡{"stdout":" 25 2\n2017-05-06 02:58:40.940538"}︡{"stdout":" 26 2\n2017-05-06 02:58:44.187469"}︡{"stdout":" 27 2\n2017-05-06 02:58:47.507031"}︡{"stdout":" 28 2\n2017-05-06 02:58:50.771241"}︡{"stdout":" 29 2\n2017-05-06 02:58:53.979139"}︡{"stdout":" 30 2\n2017-05-06 02:58:57.531209"}︡{"stdout":" 31 2\n2017-05-06 02:59:00.978623"}︡{"stdout":" 32 2\n2017-05-06 02:59:04.248961"}︡{"stdout":" 33 2\n2017-05-06 02:59:07.614130"}︡{"stdout":" 34 2\n2017-05-06 02:59:10.796605"}︡{"stdout":" 35 2\n2017-05-06 02:59:14.025167"}︡{"stdout":" 36 2\n2017-05-06 02:59:17.307669"}︡{"stdout":" 37 2\n2017-05-06 02:59:20.600155"}︡{"stdout":" 38 2\n2017-05-06 02:59:23.812997"}︡{"stdout":" 39 2\n2017-05-06 02:59:27.074759"}︡{"stdout":" 40 2\n2017-05-06 02:59:30.309353"}︡{"stdout":" 41 2\n2017-05-06 02:59:33.521919"}︡{"stdout":" 42 2\n2017-05-06 02:59:36.778813"}︡{"stdout":" 43 2\n2017-05-06 02:59:40.010204"}︡{"stdout":" 44 2\n2017-05-06 02:59:43.281245"}︡{"stdout":" 45 2\n2017-05-06 02:59:46.587512"}︡{"stdout":" 46 2\n2017-05-06 02:59:49.924342"}︡{"stdout":" 47 2\n2017-05-06 02:59:53.328917"}︡{"stdout":" 48 2\n2017-05-06 02:59:56.733704"}︡{"stdout":" 49 2\n2017-05-06 03:00:00.093701"}︡{"stdout":" 50 2\n2017-05-06 03:00:03.509686"}︡{"stdout":" 51 2\n2017-05-06 03:00:06.945458"}︡{"stdout":" 52 2\n2017-05-06 03:00:10.260684"}︡{"stdout":" 53 2\n2017-05-06 03:00:13.556968"}︡{"stdout":" 54 2\n2017-05-06 03:00:16.831035"}︡{"stdout":" 55 2\n2017-05-06 03:00:20.147962"}︡{"stdout":" 56 2\n2017-05-06 03:00:23.441133"}︡{"stdout":" 57 2\n2017-05-06 03:00:26.715238"}︡{"stdout":" 58 2\n2017-05-06 03:00:29.999464"}︡{"stdout":" 59 2\n2017-05-06 03:00:33.279286"}︡{"stdout":" 60 2\n2017-05-06 03:00:36.624413"}︡{"stdout":" 61 2\n2017-05-06 03:00:39.916577"}︡{"stdout":" 62 2\n2017-05-06 03:00:43.170842"}︡{"stdout":" 63 2\n2017-05-06 03:00:46.443298"}︡{"stdout":"\n2017-05-06 03:00:46.475957 0 0\n2017-05-06 03:00:49.857487"}︡{"stdout":" 1 3\n2017-05-06 03:00:53.209303"}︡{"stdout":" 2 3\n2017-05-06 03:00:56.590481"}︡{"stdout":" 3 3\n2017-05-06 03:00:59.934789"}︡{"stdout":" 4 3\n2017-05-06 03:01:03.332409"}︡{"stdout":" 5 3\n2017-05-06 03:01:06.767768"}︡{"stdout":" 6 3\n2017-05-06 03:01:10.150601"}︡{"stdout":" 7 3\n2017-05-06 03:01:13.498354"}︡{"stdout":" 8 3\n2017-05-06 03:01:16.912269"}︡{"stdout":" 9 3\n2017-05-06 03:01:20.342795"}︡{"stdout":" 10 3\n2017-05-06 03:01:23.781301"}︡{"stdout":" 11 3\n2017-05-06 03:01:27.220874"}︡{"stdout":" 12 3\n2017-05-06 03:01:30.636999"}︡{"stdout":" 13 3\n2017-05-06 03:01:34.405399"}︡{"stdout":" 14 3\n2017-05-06 03:01:37.921937"}︡{"stdout":" 15 3\n2017-05-06 03:01:42.173126"}︡{"stdout":" 16 3\n2017-05-06 03:01:46.041212"}︡{"stdout":" 17 3\n2017-05-06 03:01:49.471837"}︡{"stdout":" 18 3\n2017-05-06 03:01:52.883164"}︡{"stdout":" 19 3\n2017-05-06 03:01:56.263126"}︡{"stdout":" 20 3\n2017-05-06 03:01:59.648789"}︡{"stdout":" 21 3\n2017-05-06 03:02:03.130634"}︡{"stdout":" 22 3\n2017-05-06 03:02:07.131534"}︡{"stdout":" 23 3\n2017-05-06 03:02:11.251890"}︡{"stdout":" 24 3\n2017-05-06 03:02:14.660818"}︡{"stdout":" 25 3\n2017-05-06 03:02:18.320493"}︡{"stdout":" 26 3\n2017-05-06 03:02:21.840588"}︡{"stdout":" 27 3\n2017-05-06 03:02:25.476045"}︡{"stdout":" 28 3\n2017-05-06 03:02:29.002557"}︡{"stdout":" 29 3\n2017-05-06 03:02:32.349310"}︡{"stdout":" 30 3\n2017-05-06 03:02:35.682508"}︡{"stdout":" 31 3\n2017-05-06 03:02:39.156114"}︡{"stdout":" 32 3\n2017-05-06 03:02:42.791616"}︡{"stdout":" 33 3\n2017-05-06 03:02:46.512094"}︡{"stdout":" 34 3\n2017-05-06 03:02:49.927659"}︡{"stdout":" 35 3\n2017-05-06 03:02:53.247957"}︡{"stdout":" 36 3\n2017-05-06 03:02:56.586279"}︡{"stdout":" 37 3\n2017-05-06 03:02:59.941705"}︡{"stdout":" 38 3\n2017-05-06 03:03:03.283344"}︡{"stdout":" 39 3\n2017-05-06 03:03:06.657078"}︡{"stdout":" 40 3\n2017-05-06 03:03:09.989166"}︡{"stdout":" 41 3\n2017-05-06 03:03:13.334691"}︡{"stdout":" 42 3\n2017-05-06 03:03:16.824372"}︡{"stdout":" 43 3\n2017-05-06 03:03:20.256090"}︡{"stdout":" 44 3\n2017-05-06 03:03:23.682410"}︡{"stdout":" 45 3\n2017-05-06 03:03:27.127888"}︡{"stdout":" 46 3\n2017-05-06 03:03:30.582320"}︡{"stdout":" 47 3\n2017-05-06 03:03:34.038168"}︡{"stdout":" 48 3\n2017-05-06 03:03:37.447851"}︡{"stdout":" 49 3\n2017-05-06 03:03:40.813001"}︡{"stdout":" 50 3\n2017-05-06 03:03:44.151762"}︡{"stdout":" 51 3\n2017-05-06 03:03:47.498631"}︡{"stdout":" 52 3\n2017-05-06 03:03:50.885220"}︡{"stdout":" 53 3\n2017-05-06 03:03:54.253785"}︡{"stdout":" 54 3\n2017-05-06 03:03:57.626165"}︡{"stdout":" 55 3\n2017-05-06 03:04:01.075487"}︡{"stdout":" 56 3\n2017-05-06 03:04:04.534410"}︡{"stdout":" 57 3\n2017-05-06 03:04:07.967902"}︡{"stdout":" 58 3\n2017-05-06 03:04:11.333126"}︡{"stdout":" 59 3\n2017-05-06 03:04:14.689994"}︡{"stdout":" 60 3\n2017-05-06 03:04:18.088075"}︡{"stdout":" 61 3\n2017-05-06 03:04:21.428326"}︡{"stdout":" 62 3\n2017-05-06 03:04:24.766350"}︡{"stdout":" 63 3\n2017-05-06 03:04:28.076117"}︡{"stdout":"\n2017-05-06 03:04:28.084457 0 0\n2017-05-06 03:04:31.442952"}︡{"stdout":" 1 4\n2017-05-06 03:04:34.788575"}︡{"stdout":" 2 4\n2017-05-06 03:04:38.250170"}︡{"stdout":" 3 4\n2017-05-06 03:04:41.564457"}︡{"stdout":" 4 4\n2017-05-06 03:04:45.025690"}︡{"stdout":" 5 4\n2017-05-06 03:04:48.392069"}︡{"stdout":" 6 4\n2017-05-06 03:04:51.854856"}︡{"stdout":" 7 4\n2017-05-06 03:04:55.203230"}︡{"stdout":" 8 4\n2017-05-06 03:04:58.585522"}︡{"stdout":" 9 4\n2017-05-06 03:05:01.953658"}︡{"stdout":" 10 4\n2017-05-06 03:05:05.504379"}︡{"stdout":" 11 4\n2017-05-06 03:05:08.783153"}︡{"stdout":" 12 4\n2017-05-06 03:05:12.185663"}︡{"stdout":" 13 4\n2017-05-06 03:05:15.660211"}︡{"stdout":" 14 4\n2017-05-06 03:05:19.117307"}︡{"stdout":" 15 4\n2017-05-06 03:05:22.589102"}︡{"stdout":" 16 4\n2017-05-06 03:05:25.894176"}︡{"stdout":" 17 4\n2017-05-06 03:05:29.192661"}︡{"stdout":" 18 4\n2017-05-06 03:05:32.499704"}︡{"stdout":" 19 4\n2017-05-06 03:05:35.843754"}︡{"stdout":" 20 4\n2017-05-06 03:05:39.161780"}︡{"stdout":" 21 4\n2017-05-06 03:05:42.531352"}︡{"stdout":" 22 4\n2017-05-06 03:05:45.928704"}︡{"stdout":" 23 4\n2017-05-06 03:05:49.387266"}︡{"stdout":" 24 4\n2017-05-06 03:05:52.779696"}︡{"stdout":" 25 4\n2017-05-06 03:05:56.324146"}︡{"stdout":" 26 4\n2017-05-06 03:05:59.791588"}︡{"stdout":" 27 4\n2017-05-06 03:06:03.280147"}︡{"stdout":" 28 4\n2017-05-06 03:06:06.734552"}︡{"stdout":" 29 4\n2017-05-06 03:06:10.221557"}︡{"stdout":" 30 4\n2017-05-06 03:06:13.673371"}︡{"stdout":" 31 4\n2017-05-06 03:06:17.095373"}︡{"stdout":" 32 4\n2017-05-06 03:06:20.592548"}︡{"stdout":" 33 4\n2017-05-06 03:06:23.859778"}︡{"stdout":" 34 4\n2017-05-06 03:06:27.264577"}︡{"stdout":" 35 4\n2017-05-06 03:06:30.674264"}︡{"stdout":" 36 4\n2017-05-06 03:06:34.108899"}︡{"stdout":" 37 4\n2017-05-06 03:06:37.555621"}︡{"stdout":" 38 4\n2017-05-06 03:06:40.994221"}︡{"stdout":" 39 4\n2017-05-06 03:06:44.439666"}︡{"stdout":" 40 4\n2017-05-06 03:06:47.882694"}︡{"stdout":" 41 4\n2017-05-06 03:06:51.417473"}︡{"stdout":" 42 4\n2017-05-06 03:06:54.698446"}︡{"stdout":" 43 4\n2017-05-06 03:06:57.951710"}︡{"stdout":" 44 4\n2017-05-06 03:07:01.376800"}︡{"stdout":" 45 4\n2017-05-06 03:07:04.727394"}︡{"stdout":" 46 4\n2017-05-06 03:07:08.203932"}︡{"stdout":" 47 4\n2017-05-06 03:07:11.700540"}︡{"stdout":" 48 4\n2017-05-06 03:07:15.242224"}︡{"stdout":" 49 4\n2017-05-06 03:07:18.829410"}︡{"stdout":" 50 4\n2017-05-06 03:07:22.463731"}︡{"stdout":" 51 4\n2017-05-06 03:07:26.000674"}︡{"stdout":" 52 4\n2017-05-06 03:07:29.358479"}︡{"stdout":" 53 4\n2017-05-06 03:07:32.732228"}︡{"stdout":" 54 4\n2017-05-06 03:07:36.129653"}︡{"stdout":" 55 4\n2017-05-06 03:07:39.540269"}︡{"stdout":" 56 4\n2017-05-06 03:07:42.852837"}︡{"stdout":" 57 4\n2017-05-06 03:07:46.155062"}︡{"stdout":" 58 4\n2017-05-06 03:07:49.557746"}︡{"stdout":" 59 4\n2017-05-06 03:07:52.882232"}︡{"stdout":" 60 4\n2017-05-06 03:07:56.209306"}︡{"stdout":" 61 4\n2017-05-06 03:07:59.523191"}︡{"stdout":" 62 4\n2017-05-06 03:08:02.877766"}︡{"stdout":" 63 4\n2017-05-06 03:08:06.174567"}︡{"stdout":"\n2017-05-06 03:08:06.182396 0 0\n2017-05-06 03:08:09.388952"}︡{"stdout":" 1 3\n2017-05-06 03:08:13.183461"}︡{"stdout":" 2 3\n2017-05-06 03:08:16.483058"}︡{"stdout":" 3 3\n2017-05-06 03:08:19.806751"}︡{"stdout":" 4 3\n2017-05-06 03:08:23.163525"}︡{"stdout":" 5 3\n2017-05-06 03:08:26.462869"}︡{"stdout":" 6 3\n2017-05-06 03:08:29.786921"}︡{"stdout":" 7 3\n2017-05-06 03:08:33.111935"}︡{"stdout":" 8 3\n2017-05-06 03:08:36.412669"}︡{"stdout":" 9 3\n2017-05-06 03:08:39.738183"}︡{"stdout":" 10 3\n2017-05-06 03:08:43.031023"}︡{"stdout":" 11 3\n2017-05-06 03:08:46.330998"}︡{"stdout":" 12 3\n2017-05-06 03:08:49.662947"}︡{"stdout":" 13 3\n2017-05-06 03:08:52.972137"}︡{"stdout":" 14 3\n2017-05-06 03:08:56.273644"}︡{"stdout":" 15 3\n2017-05-06 03:08:59.549249"}︡{"stdout":" 16 3\n2017-05-06 03:09:02.953003"}︡{"stdout":" 17 3\n2017-05-06 03:09:06.447408"}︡{"stdout":" 18 3\n2017-05-06 03:09:09.823532"}︡{"stdout":" 19 3\n2017-05-06 03:09:13.421080"}︡{"stdout":" 20 3\n2017-05-06 03:09:16.737438"}︡{"stdout":" 21 3\n2017-05-06 03:09:20.120502"}︡{"stdout":" 22 3\n2017-05-06 03:09:23.335930"}︡{"stdout":" 23 3\n2017-05-06 03:09:26.563003"}︡{"stdout":" 24 3\n2017-05-06 03:09:29.776140"}︡{"stdout":" 25 3\n2017-05-06 03:09:33.084004"}︡{"stdout":" 26 3\n2017-05-06 03:09:36.308600"}︡{"stdout":" 27 3\n2017-05-06 03:09:39.515895"}︡{"stdout":" 28 3\n2017-05-06 03:09:42.675989"}︡{"stdout":" 29 3\n2017-05-06 03:09:45.841564"}︡{"stdout":" 30 3\n2017-05-06 03:09:48.999030"}︡{"stdout":" 31 3\n2017-05-06 03:09:52.155152"}︡{"stdout":" 32 3\n2017-05-06 03:09:55.304934"}︡{"stdout":" 33 3\n2017-05-06 03:09:58.596474"}︡{"stdout":" 34 3\n2017-05-06 03:10:01.903995"}︡{"stdout":" 35 3\n2017-05-06 03:10:05.390688"}︡{"stdout":" 36 3\n2017-05-06 03:10:08.840430"}︡{"stdout":" 37 3\n2017-05-06 03:10:12.474374"}︡{"stdout":" 38 3\n2017-05-06 03:10:15.757449"}︡{"stdout":" 39 3\n2017-05-06 03:10:19.041673"}︡{"stdout":" 40 3\n2017-05-06 03:10:22.336798"}︡{"stdout":" 41 3\n2017-05-06 03:10:25.651817"}︡{"stdout":" 42 3\n2017-05-06 03:10:28.972698"}︡{"stdout":" 43 3\n2017-05-06 03:10:32.294299"}︡{"stdout":" 44 3\n2017-05-06 03:10:35.581016"}︡{"stdout":" 45 3\n2017-05-06 03:10:38.838032"}︡{"stdout":" 46 3\n2017-05-06 03:10:42.080805"}︡{"stdout":" 47 3\n2017-05-06 03:10:45.301204"}︡{"stdout":" 48 3\n2017-05-06 03:10:48.516306"}︡{"stdout":" 49 3\n2017-05-06 03:10:51.720965"}︡{"stdout":" 50 3\n2017-05-06 03:10:54.955197"}︡{"stdout":" 51 3\n2017-05-06 03:10:58.175330"}︡{"stdout":" 52 3\n2017-05-06 03:11:01.426895"}︡{"stdout":" 53 3\n2017-05-06 03:11:04.701654"}︡{"stdout":" 54 3\n2017-05-06 03:11:07.907437"}︡{"stdout":" 55 3\n2017-05-06 03:11:11.100536"}︡{"stdout":" 56 3\n2017-05-06 03:11:14.333730"}︡{"stdout":" 57 3\n2017-05-06 03:11:17.621868"}︡{"stdout":" 58 3\n2017-05-06 03:11:20.838720"}︡{"stdout":" 59 3\n2017-05-06 03:11:24.040763"}︡{"stdout":" 60 3\n2017-05-06 03:11:27.276837"}︡{"stdout":" 61 3\n2017-05-06 03:11:30.445434"}︡{"stdout":" 62 3\n2017-05-06 03:11:33.689148"}︡{"stdout":" 63 3\n2017-05-06 03:11:36.900394"}︡{"stdout":"\n"}︡{"done":true}︡{"stdout":" 37 3\n2017-05-06 03:10:12.474374"}︡{"stdout":" 38 3\n2017-05-06 03:10:15.757449"}︡{"stdout":" 39 3\n2017-05-06 03:10:19.041673"}︡{"stdout":" 40 3\n2017-05-06 03:10:22.336798"}︡{"stdout":" 41 3\n2017-05-06 03:10:25.651817"}︡{"stdout":" 42 3\n2017-05-06 03:10:28.972698"}︡{"stdout":" 43 3\n2017-05-06 03:10:32.294299"}︡{"stdout":" 44 3\n2017-05-06 03:10:35.581016"}︡{"stdout":" 45 3\n2017-05-06 03:10:38.838032"}︡{"stdout":" 46 3\n2017-05-06 03:10:42.080805"}︡{"stdout":" 47 3\n2017-05-06 03:10:45.301204"}︡{"stdout":" 48 3\n2017-05-06 03:10:48.516306"}︡{"stdout":" 49 3\n2017-05-06 03:10:51.720965"}︡{"stdout":" 50 3\n2017-05-06 03:10:54.955197"}︡{"stdout":" 51 3\n2017-05-06 03:10:58.175330"}︡{"stdout":" 52 3\n2017-05-06 03:11:01.426895"}︡{"stdout":" 53 3\n2017-05-06 03:11:04.701654"}︡{"stdout":" 54 3\n2017-05-06 03:11:07.907437"}︡{"stdout":" 55 3\n2017-05-06 03:11:11.100536"}︡{"stdout":" 56 3\n2017-05-06 03:11:14.333730"}︡{"stdout":" 57 3\n2017-05-06 03:11:17.621868"}︡{"stdout":" 58 3\n2017-05-06 03:11:20.838720"}︡{"stdout":" 59 3\n2017-05-06 03:11:24.040763"}︡{"stdout":" 60 3\n2017-05-06 03:11:27.276837"}︡{"stdout":" 61 3\n2017-05-06 03:11:30.445434"}︡{"stdout":" 62 3\n2017-05-06 03:11:33.689148"}︡{"stdout":" 63 3\n2017-05-06 03:11:36.900394"}︡{"stdout":"\n"}︡{"done":true}︡
︠e8ea4e89-a6b4-4927-bd1f-df4c1ae89209i︠
%md
Display the length of c, the list of classifications.
︡293d0252-233d-4c33-8b46-ca1b492a0b79︡{"done":true,"md":"Display the length of c, the list of classifications."}
︠a4d0250c-e19a-4860-a47f-1c36364dbcf6sw︠
len(c)
︡d9f01fdd-7d18-4390-bac3-fa6fe90af61f︡{"html":"<div align='center'>$\\displaystyle 5$</div>"}︡{"done":true}︡
︠c60f5217-b5f5-44d2-84c2-482d0ff85754i︠
%md
Verify that `c[0]` is `None`.
︡b653ab43-e2f0-40a4-a962-258e6505ec9b︡{"done":true,"md":"Verify that `c[0]` is `None`."}
︠b9252c7a-e9d0-4b27-8e13-5c52af4203f6s︠
print c[0]
︡81986c73-c019-4d58-a51d-2238f43e8199︡{"stdout":"None\n"}︡{"done":true}︡
︠f7d9adbd-e5b1-4677-a7f6-1b8b0e2936c1i︠
%md
Print the algebraic normal form of the bent function corresponding to `c[1]`.
︡64ede573-3f25-4eb8-96ed-1b0e71a00ac4︡{"done":true,"md":"Print the algebraic normal form of the bent function corresponding to `c[1]`."}
︠48469662-da5a-4b88-b3ac-37ea6473a772s︠
c[1].algebraic_normal_form
︡de6b1bfa-41ce-4437-baaa-67e11423fae3︡{"stdout":"x0*x1 + x2*x3 + x4*x5\n"}︡{"done":true}︡
︠797c47ef-f3dc-41e7-9c0b-3bd8bac37613i︠
%md
Produce a report on the classification `c[1]`.
︡b37f77a9-f376-4103-8db5-d2044c09bab8︡{"done":true,"md":"Produce a report on the classification `c[1]`."}
︠be785fa8-53d6-49b8-9a34-9012e7bda88ds︠
c[1].report()
︡3d9e976b-0365-4d8c-810e-35cbbd8e6603︡{"stdout":"Algebraic normal form of Boolean function: x0*x1 + x2*x3 + x4*x5\nFunction is bent.\n\nWeight class matrix:\n64 x 64 dense matrix over Integer Ring\n\nSDP design incidence structure t-design parameters: (True, (2, 64, 28, 12))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n64 x 64 dense matrix over Integer Ring\n\nThere are 2 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1 + x2*x3 + x4*x5\nClique polynomial: 64*t^8 + 512*t^7 + 1792*t^6 + 3584*t^5 + 5376*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 8 Order:"}︡{"stdout":" "}︡{"stdout":"2580480\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 0 0 1 0 1 1 1 1 0 0 1 1 1 1 0 0 0 1 1 1 0 1 1 0 1]\n[0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 1 1 0 0 0 1 1 1]\n[0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 1 1 0 1 1 1 0 0 1]\n[0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 0 1 1 0 1 1 0 1 1 0]\n[0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1 + x0 + x1 + x2*x3 + x4*x5\nClique polynomial: 2304*t^6 + 13824*t^5 + 19200*t^4 + 7680*t^3 + 1152*t^2 + 64*t + 1\nStrongly regular parameters: (64, 36, 20, 20)\nRank: 8 Order: 3317760\n\nLinear code from representative:\n[36, 6] linear code over GF(2)"}︡{"stdout":"\nGenerator matrix:\n[1 0 1 0 1 0 0 1 0 0 0 1 0 1 0 1 1 0 1 1 0 1 0 1 0 1 1 0 1 1 0 1 1 1 0 1]\n[0 1 1 0 1 1 0 1 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1 0 1 1 0 1 1 0 0 0 0 0 1 1]\n[0 0 0 1 1 1 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 1 0 1 1 1]\n[0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 1 0 0 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 27, 20: 36}\n"}︡{"done":true}︡
︠f485a984-9876-47bf-80d5-f32bcf51cc08i︠
%md
Produce a matrix plot of the `weight_class_matrix`.
︡85cdb152-92b1-4b3b-b5f4-5d05f3ebdcf8︡{"done":true,"md":"Produce a matrix plot of the `weight_class_matrix`."}
︠7d1b8ad2-fdbb-41eb-95da-63d0ad74ee6fs︠
matrix_plot(c[1].weight_class_matrix,cmap='gist_stern')
︡b6011867-bf65-49d9-932e-b101bc322510︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_LnO2HP.svg","show":true,"text":null,"uuid":"380bd91c-88ff-454f-81f6-e5f0954481b1"},"once":false}︡{"done":true}︡
︠a3f1831d-128a-440e-9f06-580bd6570e78i︠
%md
Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class.
︡45f8f0b2-ac6f-4531-b430-ba800a4c8b9e︡{"done":true,"md":"Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class."}
︠97711f70-c6e0-4a5a-8ad1-11188fa19280s︠
matrix_plot(c[1].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡76001c71-e374-4c56-86e8-d4fc8a1c7c68︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_kk1IRS.svg","show":true,"text":null,"uuid":"d657b800-b156-4aed-b6f6-6848f463e776"},"once":false}︡{"done":true}︡
︠6e7b0acd-69e6-469c-88df-67a52c868d93i︠
%md
Print the algebraic normal form of the bent function corresponding to `c[2]`.
︡3064da44-2ac5-400a-ab7f-e3caf174455c︡{"done":true,"md":"Print the algebraic normal form of the bent function corresponding to `c[2]`."}
︠898671a8-5b82-489e-b70c-c66a0a0352cas︠
c[2].algebraic_normal_form
︡73799198-7e29-47b3-b9b6-0fb16d8114f8︡{"stdout":"x0*x1*x2 + x0*x3 + x1*x4 + x2*x5\n"}︡{"done":true}︡
︠88ebd904-4b27-406a-8fd0-249ba97f3a39i︠
%md
Produce a report on the classification `c[2]`.
︡e4cb9359-7e7d-4c53-8e81-7265feb02da1︡{"done":true,"md":"Produce a report on the classification `c[2]`."}
︠9084f164-6ee0-4fef-8032-024da725bff5s︠
c[2].report()
︡9a867f2d-b54f-49e3-99a8-59f9cd301c68︡{"stdout":"Algebraic normal form of Boolean function: x0*x1*x2 + x0*x3 + x1*x4 + x2*x5\nFunction is bent.\n\nWeight class matrix:\n64 x 64 dense matrix over Integer Ring\n\nSDP design incidence structure t-design parameters: (True, (2, 64, 28, 12))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n64 x 64 dense matrix over Integer Ring\n\nThere are 3 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x3 + x1*x4 + x2*x5\nClique polynomial: 64*t^8 + 512*t^7 + 1792*t^6 + 3584*t^5 + 5376*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 8 Order: 2580480\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 0 0 1 1 0 0 1 0 1 1 0 1 1]\n[0 1 0 0 0 0 1 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 1 1 0 1 0 0]\n[0 0 1 0 0 1 0 1 1 1 1 0 0 1 1 0 1 1 0 1 0 1 1 0 1 1 1 0]\n[0 0 0 1 0 1 1 0 1 1 0 1 0 1 0 1 1 1 1 0 1 0 0 1 1 1 0 1]\n[0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x3 + x1*x2 + x1*x4 + x2*x5 + x3\nClique polynomial: 256*t^6 + 1536*t^5 + 4352*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 8 Order: 24576\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 1 0 0 1 0 0 1 1 1 0 0 0 1 1 0 0 0 1 1 0 0 0 1 1 0]\n[0 1 0 0 0 0 1 0 1 1 0 0 0 0 1 0 1 1 0 0 1 1 1 1 0 1 0 0]\n[0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 1 1 1 0 0 1 1]\n[0 0 0 0 1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 0 1 1 0 0]\n[0 0 0 0 0 1 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 0 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution:"}︡{"stdout":" {0: 1, 16: 35, 12: 28}\n\nEC class 2 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x2 + x0*x3 + x0 + x1*x2 + x1*x4 + x1 + x2*x5 + x2 + x3 + x4 + x5\nClique polynomial: 192*t^8 + 1536*t^7 + 8960*t^6 + 19968*t^5 + 20224*t^4 + 7680*t^3 + 1152*t^2 + 64*t + 1\nStrongly regular parameters: (64, 36, 20, 20)\nRank: 8 Order: 73728\n\nLinear code from representative:\n[36, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 1 0 1 0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 0 1 1 1 0 1 0 1 0 0 1]\n[0 1 1 0 0 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 0 1 1 0 0 1 0 1]\n[0 0 0 1 1 1 1 0 0 0 1 1 0 0 0 1 1 0 1 1 0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]\n[0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 27, 20: 36}\n"}︡{"done":true}︡
︠50521388-ea9b-47e6-b8fe-90624cc59386i︠
%md
Produce a matrix plot of the `weight_class_matrix`.
︡f1ad65a6-6f2b-4fa4-af2f-d1d1a72540f1︡{"done":true,"md":"Produce a matrix plot of the `weight_class_matrix`."}
︠f03aac01-97a3-4bc8-9e7e-e5c907adbdf9s︠
matrix_plot(c[2].weight_class_matrix,cmap='gist_stern')
︡08b93870-9931-4f76-8522-339afd2398ac︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_oEypEm.svg","show":true,"text":null,"uuid":"25f8f7ff-f41f-4b22-8b61-b4f3a406f8a1"},"once":false}︡{"done":true}︡
︠a4225b0d-e9b3-470e-b556-27253496668ei︠
%md
Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class.
︡e2eb7b5e-e36f-4227-871f-3e70e6e17ec2︡{"done":true,"md":"Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class."}
︠01b0335f-8b1b-49b0-85a9-200968f08d70s︠
matrix_plot(c[2].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡4095a0c6-ebc7-4366-830e-7f79600b572f︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_Y7IvLD.svg","show":true,"text":null,"uuid":"895ee58f-e652-4c97-83e4-3b2dadd8b95f"},"once":false}︡{"done":true}︡
︠d2767a1a-6845-4376-a4d6-f30c45246f4ci︠
%md
Print the algebraic normal form of the bent function corresponding to `c[3]`.
︡f42700c5-fe86-41e8-8e68-da65fa62075f︡{"done":true,"md":"Print the algebraic normal form of the bent function corresponding to `c[3]`."}
︠3805f17f-3fe5-4803-8ff3-b99c8f913b2ds︠
c[3].algebraic_normal_form
︡61e3868b-8633-42f9-b26f-845a43e5bbdf︡{"stdout":"x0*x1*x2 + x0*x1 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x4 + x3*x4\n"}︡{"done":true}︡
︠8b5e46e3-d7b3-4402-91c4-218ee40c5098i︠
%md
Produce a report on the classification `c[3]`.
︡0b03bbad-ec88-4d42-92f5-01cf35f8ec1b︡{"done":true,"md":"Produce a report on the classification `c[3]`."}
︠f9bff1b2-a911-41aa-8073-8da31a598499s︠
c[3].report()
︡da539589-774f-4609-a891-253f1d2e1abf︡{"stdout":"Algebraic normal form of Boolean function: x0*x1*x2 + x0*x1 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x4 + x3*x4\nFunction is bent.\n\nWeight class matrix:\n64 x 64 dense matrix over Integer Ring\n\nSDP design incidence structure t-design parameters: (True, (2, 64, 28, 12))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n64 x 64 dense matrix over Integer Ring\n\nThere are 4 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x4 + x3*x4\nClique polynomial: 32*t^8 + 256*t^7 + 896*t^6 + 2048*t^5 + 4608*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 12 Order: 6144\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 0 0 1 0 1 0 0 1 0 0 0 1 0 1 0 0 1 1 1 0 0 0 1 1 1]\n[0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0]\n[0 0 1 0 0 1 0 0 1 1 1 1 0 1 0 1 1 0 0 0 0 0 1 0 1 0 0 1]\n[0 0 0 1 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0]\n[0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x3 + x0 + x1*x2 + x1*x3*x4 + x1*x4 + x1*x5 + x1 + x2*x4 + x3*x4 + x3 + x4\nClique polynomial: 160*t^8 + 1280*t^7 + 9344*t^6 + 21504*t^5 + 20480*t^4 + 7680*t^3 + 1152*t^2 + 64*t + 1\nStrongly regular parameters: (64, 36, 20, 20)\nRank: "}︡{"stdout":"12 Order: 10240\n\nLinear code from representative:\n[36, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 1 0 0 0 1 1 1 0 1 0 0 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 1 1 1 1 0 1 0 1]\n[0 1 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0 1 1 1]\n[0 0 0 1 1 0 0 0 1 1 1 1 0 0 0 1 1 0 0 0 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 1]\n[0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 27, 20: 36}\n\nEC class 2 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x2 + x0*x3 + x0 + x1*x3*x4 + x1*x5 + x2*x4 + x5\nClique polynomial: 64*t^6 + 1024*t^5 + 4096*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 12 Order: 7680\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 0 0 1 0 1 0 0 0 1 0 0 1 1 0 0 1 0 1 1 0 0 1 0 1 1]\n[0 1 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0]\n[0 0 1 0 0 0 0 1 1 0 1 0 0 0 0 1 1 0 1 0 0 1 1 1 1 0 1 0]\n[0 0 0 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 1 0 0 0 1 1 0 0 1]\n[0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 3 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x2 + x0*x3 + x0 + x1*x2 + x1*x3*x4 + x1*x5 + x1 + x2*x4 + x2 + x3 + x5\nClique polynomial:"}︡{"stdout":" 160*t^8 + 1664*t^7 + 9792*t^6 + 21504*t^5 + 20480*t^4 + 7680*t^3 + 1152*t^2 + 64*t + 1\nStrongly regular parameters: (64, 36, 20, 20)\nRank: 12 Order: 7680\n\nLinear code from representative:\n[36, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 1 0 1 0 1 0 1 1 1 1 0 1 0 1 0 1 1 0 0 0 1 0 1 1 0 1 1 1 0 1 0 1 0 0]\n[0 1 1 0 0 1 1 0 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 0 1 1 0 0 1 0 1]\n[0 0 0 1 1 1 1 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 1 1 0 1 1 0 0 0 1 1 0 1 1]\n[0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 27, 20: 36}\n"}︡{"done":true}︡
︠aeabd93e-98d2-488d-993b-8c1c63fcd7ffi︠
%md
Produce a matrix plot of the `weight_class_matrix`.
︡06f52ab8-946e-414e-84de-f5d0330f1448︡{"done":true,"md":"Produce a matrix plot of the `weight_class_matrix`."}
︠832021a0-542a-4b75-84bc-3f91abe8f40cs︠
matrix_plot(c[3].weight_class_matrix,cmap='gist_stern')
︡37ad750f-68be-41fa-8920-3c78d1d94450︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_dUpzBj.svg","show":true,"text":null,"uuid":"a787ec87-85ac-493d-ad7e-b70035c78bc6"},"once":false}︡{"done":true}︡
︠597e9a5e-5e70-44e8-9795-38a9b940eb0ai︠
%md
Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class.
︡13894a29-fd15-4958-9778-e3610ebe2765︡{"done":true,"md":"Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class."}
︠d49228cd-4cc6-47cf-95ec-06dbeb12fb68s︠
matrix_plot(c[3].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡78ed9ff5-66b8-46ad-a061-49ff3d357c0b︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_ETvpSM.svg","show":true,"text":null,"uuid":"49eafd4e-c33b-4857-887e-829dded7eaec"},"once":false}︡{"done":true}︡
︠c78e46e7-4550-4c24-aa2a-ba1487a3697di︠
%md
Print the algebraic normal form of the bent function corresponding to `c[4]`.
︡8f579051-e8ea-445d-bdee-639e470cf155︡{"done":true,"md":"Print the algebraic normal form of the bent function corresponding to `c[4]`."}
︠fb0ca2d2-5cdf-4e80-b85b-fbbbbce71541s︠
c[4].algebraic_normal_form
︡16e41d7b-93b4-4d9d-a799-0f53ee3ff508︡{"stdout":"x0*x1*x2 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x3*x5 + x2*x3 + x2*x4 + x2*x5 + x3*x4 + x3*x5\n"}︡{"done":true}︡
︠a7424806-05a8-478d-b87b-12d5924eeed2i︠
%md
Produce a report on the classification `c[4]`.
︡fe91be4f-ebc2-43f1-9a18-439e2d33ddad︡{"done":true,"md":"Produce a report on the classification `c[4]`."}
︠e6a76c34-5584-4a15-8191-f2477eb134f4s︠
c[4].report()
︡a5773be6-3d15-4515-9418-94e91f5324a7︡{"stdout":"Algebraic normal form of Boolean function: x0*x1*x2 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x3*x5 + x2*x3 + x2*x4 + x2*x5 + x3*x4 + x3*x5\nFunction is bent.\n\nWeight class matrix:\n64 x 64 dense matrix over Integer Ring\n\nSDP design incidence structure t-design parameters: (True, (2, 64, 28, 12))\n\nClassification of Cayley graphs and classification of Cayley graphs of duals are the same:\n\nMatrix of indices of Cayley graphs:\n64 x 64 dense matrix over Integer Ring\n\nThere are 3 extended Cayley classes in the extended translation class:\n\nFor each extended Cayley class in the extended translation class:\nClique polynomial, strongly regular parameters, rank, and order of a representative graph; and\nlinear code and generator matrix for a representative bent function:\n\nEC class 0 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x3*x5 + x2*x3 + x2*x4 + x2*x5 + x3*x4 + x3*x5\nClique polynomial: 32*t^8 + 256*t^7 + 896*t^6 + 1792*t^5 + 4480*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 14 Order: 5376\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 1 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0 1 0 0 1 0 0 0 0]\n[0 1 0 0 1 0 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0]\n[0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 1 1 1 1 0 0 1 1]\n[0 0 0 0 0 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1 0 1 1 0 0 1 1 0]\n[0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 1 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x2 + x0*x3 + x1*x3*x4 + x1*x5 + x2*x3*x5 + x2*x3 + x2*x4 + x2*x5 + x3*x5 + x5\nClique polynomial: 16*t^8 + 128*t^7 + 448*t^6 + 1280*t^5 + 4224*t^4 + 3584*t^3 + 896*t^2 + 64*t + 1\nStrongly regular parameters: (64, 28, 12, 12)\nRank: 14 Order: 1536\n\nLinear code from representative:\n[28, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 0 1 0 1 0 0 1 0 1 1 0 1 1 0 1 0 1 1 0 0 0 1 0 0 0 0]\n[0 1 0 1 0 0 0 1 0 0 0 1 0 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0]\n[0 0 1 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 1 1]\n[0 0 0 0 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 1 0 0 1 1 0]\n[0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 35, 12: 28}\n\nEC class 2 :\nAlgebraic normal form of representative: x0*x1*x2 + x0*x1 + x0*x2 + x0*x3 + x0 + x1*x2 + x1*x3*x4 + x1*x5 + x1 + x2*x3*x5 + x2*x3 + x2*x4 + x2*x5 + x2 + x4\nClique polynomial:"}︡{"stdout":" 176*t^8 + 1408*t^7 + 9664*t^6 + 22272*t^5 + 20608*t^4 + 7680*t^3 + 1152*t^2 + 64*t + 1\nStrongly regular parameters: (64, 36, 20, 20)\nRank: 14 Order: 1536\n\nLinear code from representative:\n[36, 6] linear code over GF(2)\nGenerator matrix:\n[1 0 1 0 1 0 1 0 1 1 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 1 1 1 0 1 0 1 0 0 0 0]\n[0 1 1 0 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 0 0 1 1 0 1 0 0 1 1 1 1 1 1 0 1 0]\n[0 0 0 1 1 1 1 0 1 1 0 1 1 1 1 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 0 0 0 1 1]\n[0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1]\n[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]\nLinear code is projective.\nWeight distribution: {0: 1, 16: 27, 20: 36}\n"}︡{"done":true}︡
︠2035fa5c-dc40-4344-bcb7-b582201c5765i︠
%md
Produce a matrix plot of the `weight_class_matrix`.
︡27e3ba16-c85d-4d9d-b3ec-7d4f9038087c︡{"done":true,"md":"Produce a matrix plot of the `weight_class_matrix`."}
︠5f7ba64c-9491-4365-9520-87064981f913s︠
matrix_plot(c[4].weight_class_matrix,cmap='gist_stern')
︡87a1258a-3f26-4a3a-acc7-aeefdd076c0a︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_6F9A4c.svg","show":true,"text":null,"uuid":"b803010d-a207-48fe-bd68-af4dde0933ec"},"once":false}︡{"done":true}︡
︠bbf0e5f7-f55f-4ab4-9ba7-6fc4eec2b3d2i︠
%md
Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class.
︡3259a59a-ddf4-461c-8486-cc6d09b278af︡{"done":true,"md":"Produce a matrix plot of `bent_cayley_graph_index_matrix`, the matrix of indices of extended Cayley classes within the extended translation class."}
︠28af0dcb-9270-463d-a316-557954d57a64s︠
matrix_plot(c[4].bent_cayley_graph_index_matrix,cmap='gist_stern')
︡eff9d4a3-2d4f-452a-a432-f22b9b6da220︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_SxAj5_.svg","show":true,"text":null,"uuid":"39c61b40-4e59-4100-98dc-52003690679c"},"once":false}︡{"done":true}︡
︠6fedd900-54a0-4222-b2fa-7ab71072df23i︠
%md
Now produce a reclassification `r` by seeing which extended Cayley classes are repeated between extended translation classes.
︡3bf27cf1-e36c-48d2-b96f-a7fa0f8115a2︡{"done":true,"md":"Now produce a reclassification `r` by seeing which extended Cayley classes are repeated between extended translation classes."}
︠0f4258ea-f31e-45e6-a723-ced7e8bc205bs︠
r = BooleanDimensionCayleyGraphReclassification(c)
︡f1e7c8b1-82eb-489d-aec3-5e7162310547︡{"done":true}︡
︠279e49a9-965f-4252-9c93-f3a3070900f4i︠
%md
Print the structure of `r`.
︡87131a8b-f8d8-46e7-afd9-94f3c71b334b︡{"done":true,"md":"Print the structure of `r`."}
︠4e1d0036-ced2-4193-83ad-99c1a0a6b27ds︠
print r.__dict__
︡322a3384-b47e-4ec0-99cd-5b26d9f01175︡{"stdout":"{'classification_list': [None, <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>, <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>, <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>, <class 'boolean_cayley_graphs.bent_function_cayley_graph_classification.BentFunctionCayleyGraphClassification'>], 'dim': 6, 'reclassification_table': [None, [   0    1]\n[   0    1]\n[2304 1792]\n[   0    1]\n[2304 1792], [   0    2    3]\n[   0    1    2]\n[ 512 1792 1792]\n[   0    1    2]\n[ 512 1792 1792], [   4    5    6    7]\n[   0    1    2    3]\n[1280  768 1024 1024]\n[   0    1    2    3]\n[1280  768 1024 1024], [   8    9   10]\n[   0    1    2]\n[ 512 1792 1792]\n[   0    1    2]\n[ 512 1792 1792]], 'cayley_graph_class_list': ['~?@?JLZW[xTZFaUHJQFaXXIjQXk[KXSdYLBlpFFClGpHSihBHrCrHJHSclhKHNWwVGbIdSalEeHFZa@pwwBoN?{w`pFDTCiaiZCWwbb`wwF_^_??F~~fAxBcLTQiQhDmLKQpGz{OMGwm]QsbQLpLHSiQjP]Oq[Hqo}RKcqRKrhSciQtT]RARHNJLvCMJFSAMtCidTcGjwbFBbaPFpwwC^_`w{BoN~ABoN_@~w?^_@}weMfCaPsEgijTOdDSNCVFb_UGqMN?~[AEN?f_^}?Fo}?D~~o??B{?N~}FwF_OpwDCf\\\\FC[ApEQPiyiaiCgia`wzMGwcQM`_~{?N?}Fo?on', '~?@??Kpx{~NX|fzTFT[itYmNUw\\\\Wziqmys\\\\|f`wXMxJImdkpuNY[RmYiJ\\\\lWb\\\\zO{M~dMEzuTSlu{kY\\\\r{nCM~]W\\\\w^me[k]^[tUdlvrW{dy~hF\\\\wzgh[n`^SstZhVX\\\\MNUemNiw\\\\vCV]gzjkgzlQmziHm|S\\\\|sD\\\\~B~oBo~oo~B~BoBuZXqsx`rxujQjTJVruZBLhZNrZphWrplxuslSisn]]sfeQsfz{ZLhfBq]RqtThYUisnerF`ksxc~b]QrF`lqNquiUdhTsj{ufBqXW{f^xJE]RKwZZ^hIislTPZZ~cLeW{qPln~HfKLeWrZX~hTTJQihZZ^{eRKwXkLlz', '~?@?JThyCTIWidLOnBbjKbIpKkppoGtL@KsdLLCRKnB_^`bZJGHxY`UEdXKcssW^_]_KrOyDBArWWhPRXhOgtUkShURLIDXTJiEEXNF_?N~~?_??F~~_?^w@~]@py@FKupLEJAhxDXHcVKrBgRHdeXwOeREovSHKabcfXBD`Hb{[KAMPeEDeNGXKqdDMXSeFiDElITIVdITbKhBqtAkhYIatmEEXowWrNuXC`UYjGvdW`AyYtC{[[PbmDs[DdeGRXcwrFpoGmNAD}@ehgVOealMDKsctBSeegxhgaqeS\\\\KS_^`w]@o{?N_^}F_@~?Bo^oN?N?w]@w^{?N{?Nw?@}', '~?@??CXHSrN@~f}P]QmiZYwvWyxkjZiTzsR|^fgVxDz]mgmuuR]\\\\[VZtIyMuhkjrk\\\\F`\\\\^cyIu|T[emup{wnNB}bff]MjHuxr\\\\iLzTVvOnta~fyyJ_VfyDs^gtzYdETlltdIhjm][WyM]nWjVLQdlqYtUSlrs[wmK^BroN~?~rKrLnKuuidTutVYzQLNks}rxWdnYU|hygT]tTzY}WE]uXz]^w?]^`x~wrrN@nBxKNUlYJYVQh]r[qZKuRK}]]FqF_v`nUmdsdglhZuZXkeXLhf^K{rckpkrZ\\\\JjUdQditZ{NNMRBErpnxfXbYXqUZX|JshYlYQtZ^`}ELffG]Lz', '~?@?JTaQKVIprErFcJWgFwE^ELWcyaygR\\\\OHrBONBoovsDC}gK[KNGQ`^OghVoYpBSoXChTDBKokWgKZZhOQ\\\\ZWQaZUlGSTutgQorls?savZH_??F~~sShyQc[SL[eKMWXfcGZk~BC`KA\\\\jSCqGD[moQQGCQQZaMquEEMofc|dGeYajUdOalKaxwqSawiUkxgUEqI]XkqiHQVPBMwidOfp@Zn_F`cx_NNkBwNWoyEYIy`]_irC{JjC}?mhE~sgRMCSHEftgEi`EBCtrossWKaEY]zAOMZE}_C\\\\qO`UqVt?`{rCC]Bz`aB_{zKEByW?[rBuo`kY`_NLHZqOkdccBj', '~?@?@KxwWREXFcnP{QrIdjPt[Tp@~y~fByhtyxZZrszl\\\\Vjrno^Y|O]xzGluvajmuw[n_}@}ZI|\\\\KxMx{\\\\NB~@qkZmijkd|sVS\\\\xjX^Qzhmbzi|bqZ]l]dke|VLkrXu[zjeKece}YhXWUl]pRcs\\\\d}PUdo|N[oxm@~NBLjVe\\\\tgl[xuU~oc{xle{\\\\PMxqnD||@ZlW|Luoy{mVVdawk|ZT\\\\hpmQuvk\\\\TeesLmzRdZXJ_\\\\xwxrxo]]mCjorUh}ltC\\\\pLjEzxoXbxKfFzyjSLy`vIZViXQ]wUsrkzjCfMdlfW|ulPUkfknH|zXDjSq{Zqn]\\\\@ysg|JuNVK{NM@}Lkur', '~?@?HSihTT@zoNB@}FbKLg{eW[klEAdKHYoHQwBXajbKUbbMdqE\\\\SZLIrOHXXSHhhdAQtLOK?]F~xeBHYaXBEXSr?[qiRGEssW?~oBv_?N~o]_??F~~_F`w@~RLYp_XKrTRc@rxdTc_MZeShkBH\\\\hTd@bIEUTiASiEstL@HdAqtQgKdO[?~o{GWFuWKYTkBTrGXKtcEVkoErTcHVXcBddkCt[?B~BwXwNjP`IkidejQeBJHYTlLYoEhatSyUdoHiTTRTN`lGJcrgp_fbKDFKtoWNBd_S}FUK@RqXAkwYeoB}@feE@kKFB`xx`w@boFK^BBK{?pwAX{NrBooL`_fe', '~?@??KoosdHh~f}TqTMlXJPtRT|MfzanrdNl|jH^epjzPknrFLU|c{U|ZBk}qXrNjXbbU|eiMjxelavrItdVkqmVEnMndLVrV|UL^a}tEj}T|nXqYXbndpdYRvketRML{hqklde}fKcxMZxbLkZLNswZFMTNrFcwpnB~~??B~uSUi}djutAinii}{iTQ~TJxxghY|YjtrorNNK{}XeFfx`~cve@fxe^fr{Ko~o{~Hz{KN{?{N]Fw^_F}F_{Ej[jHsrXXnU]YWtY[qvtZYhpXWzLukzIuTKfdl|LrRWjQ\\\\huyfdXqeW{rryZXUMhfJRr\\\\RlSekleXu]Fw@~~w?Br~', '~?@?ITYYpSHxVE[IUHdeDxXYLUGyUAJMaTdHRHgA]wWMnEAT{SXKbiYaMsMGikbYGcq]K@TLuGGmWBoyTGEg{JSAk[rRB?mZmWgE]jlB?MvXw_??F~~xIJowa\\\\OjK[EFaclFAG_\\\\A}eKMAwRtLD[EWNXkR[zhoGeaI]xSGIcafrbC@YECWBj`cyur?XspFlkd?mqPVLkwIs`FiEN[ILEBwc\\\\^CLIOzaInrY_diSwkjVP?xojTcUtHA]KLqqDQ]_tKNIg}eXgLhRWxMkLhDsIkwjd[shKgcmO?uejID`TaOHmRJaU@qh?JqsqpOqgPWbwskuOKwBF@}bTbPDc`Eg^', '~?@?JLZrl{Jy^`cGbOT@IoKYGKT?igsAwiD\\\\oFoBE~@HkVHDg|KQtmScy\\\\LGloRKKyBCxKzoYIypOibjd@T?{hTD_lW\\\\AfgRWoIyc[hmCwCE~_??F~~wo{sAXVAHYgJmgSMs@zgshI_}JBHWdDw\\\\BnSPGYmD]iGcjQtC\\\\cRGku`JiHKFKRZqDPaIouuoJHHSfHKKBxNocNrKq@KNT`R\\\\U_DHUWbNJc?kLekP_djaVUTiH@fUEldQpBGx^@RuKodPUm_jn{CoRoZo{?wMNN@_o{?{}MEwKEF_W|cWFwKX`fdir`DmOdgsaptQE]GiSwQuUBHZQQxREUbPKNWTULHa', '~?@?@KGhwyJpl?~UXXLkXyTtTUt]FyN{rzPTzpQ^JrJulilzVU\\\\muqVfX}LlmkRfjZHn_w^qeX}]LQ[|x\\\\`k}s}Jrjd]dY{wz[zmWhjr\\\\u`UujjxpJiltxgfTtfiE|YdexQ]vPnwFwMoqxzwXC{K\\\\xyabJ{myxRCtzDMjTzsmolsi}}F^?zrp}E^z`Hm^viRucLZ^^gYwXx}O{{oXsZhrSvYmmDxlQrvEyK^oxYn_vpH}dUT|Dn]_LvLI\\\\ivlOMyisZfNLsR{T\\\\aNdszA}hjcRunYta\\\\?umzf]VXEqC{|]ZxxWFnBNKN{vTqqq@zYjLzTuUh@Zrbf^o{KNe^`k]Z']}"}︡{"stdout":"\n"}︡{"done":true}︡
︠4703e40b-2747-48c6-82d3-cb6b28104e56i︠
%md
Each entry in `reclassification_table` has as row 0, the "global" index of each extended Cayley class in the extended translation class.

Row 1 contains the local index of each extended Cayley class in the extended translation class, as given by the corresponding bent functions.

Row 2 contains the size of each extended Cayley class in the extended translation class, as given by the corresponding bent functions.

Row 3 contains the local index of each extended Cayley class in the extended translation class, as given by the Walsh Hadamard dual of each of the corresponding bent functions.

Row 4 contains the size of each extended Cayley class in the extended translation class, as given by the Walsh Hadamard dual of each of the corresponding bent functions.
︡d0b3950e-ad73-42f5-8fa7-46c5510e5eca︡{"done":true,"md":"Each entry in `reclassification_table` has as row 0, the \"global\" index of each extended Cayley class in the extended translation class.\n\nRow 1 contains the local index of each extended Cayley class in the extended translation class, as given by the corresponding bent functions.\n\nRow 2 contains the size of each extended Cayley class in the extended translation class, as given by the corresponding bent functions.\n\nRow 3 contains the local index of each extended Cayley class in the extended translation class, as given by the Walsh Hadamard dual of each of the corresponding bent functions.\n\nRow 4 contains the size of each extended Cayley class in the extended translation class, as given by the Walsh Hadamard dual of each of the corresponding bent functions."}
︠10a90af1-9f73-4719-aa20-79cd83f14293i︠
%md
We see that extended Cayley class 0 occurs in both extended translation class 1 (2304 Cayley graphs) and extended translation class 2 (512 Cayley graphs).
︡21cf67bd-07ed-48e0-baae-ed47b3f806c6︡{"done":true,"md":"We see that extended Cayley class 0 occurs in both extended translation class 1 (2304 Cayley graphs) and extended translation class 2 (512 Cayley graphs)."}
︠c7883a6c-f433-4641-a54e-6a69193c34e4s︠
for n in range(1,len(r.reclassification_table)):
    print n
    print r.reclassification_table[n]
︡021c1986-496b-48bb-a63d-5290091cfc55︡{"stdout":"1\n[   0    1]\n[   0    1]\n[2304 1792]\n[   0    1]\n[2304 1792]\n2\n[   0    2    3]\n[   0    1    2]\n[ 512 1792 1792]\n[   0    1    2]\n[ 512 1792 1792]\n3\n[   4    5    6    7]\n[   0    1    2    3]\n[1280  768 1024 1024]\n[   0    1    2    3]\n[1280  768 1024 1024]\n4\n[   8    9   10]\n[   0    1    2]\n[ 512 1792 1792]\n[   0    1    2]\n[ 512 1792 1792]\n"}︡{"done":true}︡
︠8a87aa66-84c7-4600-a399-9bdf31787876i︠
%md
The list `r.classification_list` contains the classifications in `c`, but with each of the matrices `bent_cayley_graph_index_matrix` and `dual_cayley_graph_index_matrix` 
using the indices from row 0 of `reclassification_table` corresponding to each index from row 1 and row 3 respectively.
︡919e6f34-8295-4b9f-b2f2-b9972947ea07︡{"done":true,"md":"The list `r.classification_list` contains the classifications in `c`, but with each of the matrices `bent_cayley_graph_index_matrix` and `dual_cayley_graph_index_matrix` \nusing the indices from row 0 of `reclassification_table` corresponding to each index from row 1 and row 3 respectively."}
︠ee6bb7d5-03ae-485b-8b97-dec58cfb3586s︠
M = r.classification_list[2].bent_cayley_graph_index_matrix
matrix_plot(M, cmap='gist_earth')
︡db96ad8b-5008-43fa-951a-847ed793ea52︡{"file":{"filename":"/projects/80f4c9e7-8a37-4f59-82e7-aa179ec0b652/.sage/temp/compute7-us/26682/tmp_gqRSxM.svg","show":true,"text":null,"uuid":"f671388f-e516-4969-bdcb-241a463387f8"},"once":false}︡{"done":true}︡
︠c6a6694c-8ffa-42cf-b1af-320ae9f3b11ei︠
%md
Now take a look at binary projective two weight codes relevant to dimension 6.
References: Tonchev 1996, Tonchev 2006.
︡ad8e825c-b858-4a16-aa3d-34c71506a96b︡{"done":true,"md":"Now take a look at binary projective two weight codes relevant to dimension 6.\nReferences: Tonchev 1996, Tonchev 2006."}
︠0ec482cb-8453-4c34-81f7-270e7293137fs︠
print r
︡1611cf2e-343f-4af3-a84a-8f9cab2491b3︡{"stdout":"<class 'BooleanDimensionCayleyGraphReclassification'>\n"}︡{"done":true}︡
︠8fe7248b-a964-4704-8ed8-1e46ed83470as︠
from sage.graphs.strongly_regular_db import strongly_regular_from_two_weight_code
︡6b4032f4-f9b6-4ae6-828e-06bacd9d6703︡{"done":true}︡
︠1a09b00e-3a74-40e8-985c-3ad05380b738s︠
from boolean_cayley_graphs.binary_projective_two_weight_codes import *
︡09d03c9a-3237-401f-b756-8e39ebcd32a1︡{"done":true}︡
︠068bb86d-1c90-4899-96bf-e4e083541212s︠
def linear_code_from_gen_tuple(gen_tup):
    gen_mat = matrix(GF(2),[list(row) for row in gen_tup])
    return LinearCode(gen_mat)
︡cd8fff62-63a7-4994-b5a7-78f42b5b47a1︡{"done":true}︡
︠f90251e9-99fb-48ab-aac8-b3e274b33938s︠
gens_27_6_12 = binary_projective_two_weight_27_6_12()
︡d490ce76-cfc3-42bb-ae32-5701e31a6d81︡{"done":true}︡
︠46aa962c-f777-4228-97ba-04b297660f0as︠
code_27_6_12 = [linear_code_from_gen_tuple(gen_tup) for gen_tup in gens_27_6_12]
︡51b9b515-0e9b-4ac5-b461-7125be3ed7d7︡{"done":true}︡
︠dcaa5be1-3c18-46e5-8809-e51a2a78e370s︠
srg_27_6_12 = [strongly_regular_from_two_weight_code(code).canonical_label().graph6_string() for code in code_27_6_12]
︡32edf628-13d9-4c8f-a457-841cba529fc2︡{"done":true}︡
︠ba5529cc-d465-44ba-ade2-b33bd903b037s︠
print [(i,j) for i in range(len(r.cayley_graph_class_list)) 
       for j in range(len(srg_27_6_12)) 
       if r.cayley_graph_class_list[i] == srg_27_6_12[j]]
︡483707ef-cbe1-4a44-954b-066479beecb5︡{"stdout":"[(1, 0), (3, 1), (5, 2), (7, 3), (10, 4)]\n"}︡{"done":true}︡
︠6b8298c8-ca84-4f10-aa91-a07d59f8ab8cs︠
gens_35_6_16 = binary_projective_two_weight_35_6_16()
︡47a9e305-44a2-4533-a62f-446e05ab0765︡{"done":true}︡
︠956c3882-07dc-4a0c-9204-fb58292bba43s︠
code_35_6_16 = [linear_code_from_gen_tuple(gen_tup) for gen_tup in gens_35_6_16]
︡87ac5715-fc04-472f-ac53-678e9b548097︡{"done":true}︡
︠8d465265-0988-4c3d-b4c0-1ee27126a4dfs︠
srg_35_6_16 = [strongly_regular_from_two_weight_code(code).complement().canonical_label().graph6_string() for code in code_35_6_16]
︡3fa73fa3-6e69-41ce-afb2-3762c533626c︡{"done":true}︡
︠df9a70e9-826e-4f3c-aa73-41c456583499s︠
print [(i,j) for i in range(len(r.cayley_graph_class_list)) 
       for j in range(len(srg_35_6_16)) 
       if r.cayley_graph_class_list[i] == srg_35_6_16[j]]
︡c57a6214-b7d2-4ae5-8b07-243587ddcb39︡{"stdout":"[(0, 0), (0, 1), (2, 2), (4, 3), (6, 4), (8, 6), (9, 5)]\n"}︡{"done":true}︡
︠076fac84-4efe-488d-918e-408b5fbe0ace︠
︡84d0a006-c9af-4eac-abe4-6c592a782186︡









