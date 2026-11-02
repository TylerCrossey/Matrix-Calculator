import cmd, shlex
from fractions import Fraction
from matrix_operations import Matrix 
import matrix_operations as mo

class MatrixShell(cmd.Cmd):
    intro = 'Welcome to the matrix shell, Type help or ? to list commands.\n'
    prompt = "matrix> "
    file = None

    def __init__(self):
        super().__init__()
        self.matrices: dict[str, Matrix] = {} #dict mapping key string to stored matrix of Matrix type

    def onecmd(self, line):
        try:
            return super().onecmd(line)
        except KeyboardInterrupt:
            print("\n(command cancelled)")
            return False
        except (KeyError, ValueError, ZeroDivisionError) as e:
            print(f"error: {e.args[0] if e.args else e}")
            return False

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
        return self.matrices[name]

    def _row_index(self, m, text):
        """Convert an input row number to the corresponding validated index"""
        i = int(text)
        if not 1<= i <= len(m): #validate index will not be out of bounds
            raise ValueError(f"rows must be between 1 and {len(m)}")
        return i - 1
    

    def show(self, name):
        """show NAME: print a stored matrix"""
        try:
            print(self.format_matrix(self._get(name)))
        except KeyError as e:
            print(e.args[0])

    #do commands   

    def do_mul(self, arg):
        """mul NAME MATRIX1 MATRIX2, e.g. mul C A B"""
        args = arg.split()
        if len(args) != 3:
            print("usage: mul NAME MATRIX1 MATRIX2")
            return

        name, m1_text, m2_text = args
        m1, m2 =  self._get(m1_text), self._get(m2_text)
        self.matrices[name] = mo.matrix_mul(m1, m2)

        print(f"Updated matrix {name} is:")
        self.show(name)
        return 


    def do_set(self, arg):
        """set NAME MATRIX: store a matrix, e.g. set A 1,1/2;3,4"""
        name, _, text = arg.partition(" ")
        if not name or not text.strip():
            print("usage: set NAME MATRIX")
            return
        self.matrices[name] = self.parse_matrix(text)
        print(f"Stored matrix {name} as:")
        self.show(name)

    def do_show(self, arg):
        """show NAME: print a stored matrix"""
        name = arg.strip()
        self.show(name)

    def do_swap(self, arg):
        """swap NAME ROW1 ROW2: swap two rows in a matrix, e.g. swap A 1 2"""
        args = arg.split()
        if len(args) != 3:
            print("usage: swap NAME ROW1 ROW2")
            return

        name, i_text, j_text = args
        m = self._get(name)
        i, j = self._row_index(m, i_text), self._row_index(m, j_text)
        mo._swap_rows(m, i, j)

        print(f"Updated matrix {name} is:")
        self.show(name)

    def do_scale(self, arg):
        """scale NAME ROW FACTOR: multiply a row by a factor, e.g. scale A 1 1/2"""
        args = arg.split()
        if len(args) != 3:
            print("usage: scale NAME ROW FACTOR")
            return

        name, row_text, factor_text = args
        m = self._get(name)
        factor = Fraction(factor_text)
        row = self._row_index(m, row_text)

        mo._scale_row(m, row, factor)
        print(f"Updated matrix {name} is:")
        self.show(name)


    def do_rref(self, arg):
        "rref NAME: show the reduced row echelon form (does not edit original)"
        m = self._get(arg.strip())
        print(self.format_matrix(mo.row_reduce(m))) #row reduce matrix, then format, then print

    def do_add(self, arg):
        """add NAME TARGET SOURCE FACTOR: add factor times source row to target row, in place"""
        args = arg.split()
        if len(args) != 4:
            print("usage: scale NAME ROW FACTOR")
            return

        name, target_text, source_text, factor_text = args
        m = self._get(name)
        target, source = self._row_index(m, target_text), self._row_index(m, source_text)
        factor = Fraction(factor_text)

        mo._add_multiple(m, target, source, factor)
        print(f"Updated matrix {name} is:")
        self.show(name)

    def do_inv(self, arg):
        """inv NAME: show the inverse of a matrix (does not edit original)"""
        m = self._get(arg.strip())
        print(self.format_matrix(mo.inverse(m)))



    ##add to pytest!!
    #add debug and verbosity settings, numpad mode (eventually)
    


    #exit handling

    def do_quit(self, arg): #exit on quit
        """quit: exit the shell"""
        print("Exiting")
        return True

    do_exit = do_quit #alias to accept exit

    def do_EOF(self, arg): return True #exit on ctrl-d


