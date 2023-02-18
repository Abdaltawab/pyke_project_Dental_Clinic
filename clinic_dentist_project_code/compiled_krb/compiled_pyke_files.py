# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_simple_rules.krb'):
           [1672165102.6616821, 'bc_simple_rules_bc.py'],
         ('', '', 'bc_simple_rules_questions.krb'):
           [1672165102.731505, 'bc_simple_rules_questions_bc.py'],
         ('', '', 'facts.kfb'):
           [1672165102.7403126, 'facts.fbc'],
         ('', '', 'questions.kqb'):
           [1672165102.7496014, 'questions.qbc'],
         ('', '', 'venv\\Lib\\site-packages\\pyke\\krb_compiler\\compiler.krb'):
           [1672165102.8405945, 'compiler_bc.py'],
        },
        compiler_version)

