import cmd, shlex
from fractions import Fraction 
import matrix_operations as mo

class MatrixShell(cmd.Cmd):
    intro = 'Welcome to the matrix shell, Type help or ? to list commands.\n'
    prompt = "matrix> "
    file = None

    def __init__(self):
        super().__init__()
        self.matrices: dict[str, Matrix] = {} #dict mapping key string to stored matrix of Matrix type

    #non-do functions
    @staticmethod
    def parse_matrix(text: str) -> Matrix:
        """Convert arg in form of 1,1/2;3,4 to matrix"""
        rows = [r.strip() for r in text.split(";")] #rows as arg list seperated by ;
        matrix = [[Fraction(x.strip()) for x in row.split(",")] for row in rows]
        if len({len(r) for r in matrix}) != 1:
            raise ValueError("all rows must have the same number of entries")
        return matrix

    @staticmethod
    def format_matrix(m: Matrix) -> str:
        """Per row, seperate value as string by space, seperate rows by line break"""
        return "\n".join("  ".join(str(x) for x in row) for row in m) 

    def _get(self, name):
        """Match key of matrix to the matrix"""
        if name not in self.matrices:
            raise KeyError(f"no matrix named {name}")
        return self.matrices(name)

    #do commands    

    def do_set(self, arg):
        """set NAME MATRIX: store a matrix, e.g. set A 1,1/2;3,4"""
        name, _, text = arg.partition(" ")
        if not name or not text.strip():
            print("usage: set NAME MATRIX")
            return
        self.matrices[name] = self.parse_matrix(text)

    def do_show(self, arg):
        """show NAME: print a stored matrix"""
        try:
            print(self._get(arg.strip()))
        except KeyError as e:
            print(e.args[0])

    def do_EOF(self, arg): return True


