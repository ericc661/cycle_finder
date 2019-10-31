'''
Problem spec: given a 2D matrix containing capital letters A-Z, find if the
matrix contains a cycle. A cycle is a sequence of consecutive cells with the
same letter such that each cell is adjacent to the cells before and after it,
and the last cell is the same as the first. To be adjacent is 4-directional, not
including diagonals. The minimum cycle is a 'square' of length 4.
'''
import sys
from queue import Queue

class CycleFinder(object):

    # read in matrix from input and store as member variable
    def __init__(self, file):
        self.cells = [] # to store the matrix
        self.untouched = [] # stores coordinates we have not yet visited
        self.visited = {} # dictionary stores (visited: prev)

        try:
            # read in file, ensure valid dimensions
            f = open(file, 'r')
            line = f.readline().rstrip()
            width = len(line) #width of matrix established by first line
            while (line):
                if len(line) != width: # if this line is a diff. length
                    sys.exit('Inconsistent line width in input, exiting')
                else: # valid line, add to matrix
                    self.cells.append([char for char in line])
                    line = f.readline().rstrip()
            f.close()
        except FileNotFoundError:
            print("Invalid file name '{0}', exiting".format(file))
            sys.exit()

    '''
    summary: finds if there is a cycle in the matrix
    requires: nothing
    effects: returns true/false.
    '''
    def find_cycle(self):

        # add all coordinates to untouched list
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.untouched.append((i, j))

        # while there is a vertex we haven't reached yet
        while self.untouched:
            start = self.untouched.pop() # pick one such vertex & remove from untouched
            q = [] # init queue for this connected region
            self.visited[start] = None # there is no prev for a start of connected region
            q.append((start, None))

            # BFS over this connected region
            while q:
                v, prev = q.pop(0)
                neighbors = self.get_neighbors(v)
                for u in neighbors: #look @ every neighbor of v
                    # cycle found if neighbor already visited and isn't
                    #   this node's previous node
                    if (u in self.visited) and (u != prev):
                        return True
                    elif not u in self.visited:
                        # new node: add to visited, remove from untouched,
                        #   add to queue
                        self.visited[u] = v
                        self.untouched.remove(u)
                        q.append((u, v))
        # here: traversed entire graph (all connected regions) without finding cycle
        return False


    '''
    summary: gets the neighbors of the location of a cell
        (i.e. same letter, 4-directional, within boundaries)
    requires: location - a 2-tuple representing the location of a cell
    effects: raises error if location out of bounds. otherwise returns
        list of neighbors as 2-tuples
    '''
    def get_neighbors(self, location):
        if not self.in_bounds(location):
            raise IndexError('Location requested is out of bounds')
        row, col = location
        letter = self.cells[row][col]

        # check top, bottom, left, and right neighbors
        neighbors = []
        for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if self.in_bounds((row+x, col+y)):
                if self.cells[row+x][col+y] == letter:
                    neighbors.append((row+x, col+y))

        return neighbors


    '''
    given a location, determine if it is inside the matrix
    '''
    def in_bounds(self, location):
        num_rows = len(self.cells)
        if num_rows == 0: # matrix is empty: everything otut of bounds
            return False
        num_cols = len(self.cells[0])

        if (0<= location[0] < num_rows) and \
           (0<= location[1] < num_cols):
            return True
        else:
            return False


def main():
    if len(sys.argv) < 2:
        print('Correct usage: python cycle_finder.py filename')
        sys.exit()
    cf = CycleFinder(sys.argv[1])
    print(cf.find_cycle())

if __name__ == '__main__':
    main()
