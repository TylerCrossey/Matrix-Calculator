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

    def show(self, name):
        """show NAME: print a stored matrix"""
        try:
            print(self.format_matrix(self._get(name)))
        except KeyError as e:
            print(e.args[0])

    #do commands    

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
        i, j = int(i_text), int(j_text) #get args and convert row values to int
        m = self._get(name)
        mo._swap_rows(m, i-1, j-1)

        if not (1 <= i <= len(m) and 1 <= j <= len(m)): #validate not out of bounds
            raise ValueError(f"rows must be between 1 and {len(m)}")
            

        print(f"Updated matrix {name} is:")
        self.show(name)

    #def do_scale

    

    ##TODO: more error handling, add to pytest!!
    #add debug and verbosity settings, numpad mode
    #finish implementing do_funcs


    #exit handling

    def do_quit(self, arg): #exit on quit
        """quit: exit the shell"""
        print("Exiting")
        return True

    do_exit = do_quit #alias to accept exit

    def do_EOF(self, arg): return True #exit on ctrl-d


