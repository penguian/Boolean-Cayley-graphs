import os
import sys

os.environ['SAGE_LOCAL'] = '/usr'
os.environ['SAGE_ROOT'] = '/usr/share/sagemath'

os.environ['SAGE_DATA'] = '/usr/share/sagemath'
os.environ['SAGE_SHARE'] = '/usr/share/sagemath'

os.environ['SAGE_DOC'] = '/usr/share/doc/sagemath'
os.environ['SAGE_EXTCODE'] = '/usr/share/sagemath/ext'
os.environ['SAGE_SCRIPTS_DIR'] = '/usr/share/sagemath/bin'
os.environ['SAGE_SPKG_INST'] = '/usr/share/sagemath/installed'

os.environ['SAGE_SERVER'] = 'http://www.sagemath.org/'

os.environ['DOT_SAGE'] = '/home/ubuntu/.sage'
os.environ['SAGE_STARTUP_FILE'] = '/home/ubuntu/.sage/init.sage'
os.environ['SAGE_TESTDIR'] = '/home/ubuntu/.sage/tmp'

os.environ['SAGE_NUM_THREADS'] = '1'
os.environ['SAGE_NUM_THREADS_PARALLEL'] = '1'

bcg_sage_dir = '/home/ubuntu/src/sage-sandbox/Boolean-Cayley-graphs/sage-code'

os.chdir(bcg_sage_dir)

sys.path.insert(0, '/home/ubuntu/.local/lib/python2.7/site-packages')
sys.path.insert(0, '/usr/share/sagemath/bin')
sys.path.insert(0, bcg_sage_dir)
sys.path.append('/usr/share/sagemath/src')

from bent_function_cayley_graph_dashboard import app
application = app.server
