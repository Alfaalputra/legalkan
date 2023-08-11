import os
import sys

path_this = os.path.abspath(os.path.dirname(__file__))
path_src = os.path.join(path_this, "src")
sys.path.append(path_src)

from query import Query