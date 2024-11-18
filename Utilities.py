import os
import sys

def resoursce_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, 'data')
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)