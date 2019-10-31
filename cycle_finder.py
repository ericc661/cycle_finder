'''
Problem spec: given a 2D matrix containing capital letters A-Z, find if the
matrix contains a cycle. A cycle is a sequence of consecutive cells with the
same letter such that each cell is adjacent to the cells before and after it,
and the last cell is the same as the first. To be adjacent is 4-directional, not
including diagonals. The minimum cycle is a 'square' of length 4.
'''
import sys


class CycleFinder(object):

    # read in matrix from input and store as member variable
    def __init__(self, file):
        self.cells = [] # to store the matrix

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

        neighbors = []
        top = (row-1, col)
        bot = (row+1, col)
        left = (row, col-1)
        right = (row, col+1)
        if self.in_bounds(top):
            if self.cells[top[0]][top[1]] == letter:
                neighbors.append(top)
        if self.in_bounds(bot):
            if self.cells[bot[0]][bot[1]] == letter:
                neighbors.append(bot)
        if self.in_bounds(left):
            if self.cells[left[0]][left[1]] == letter:
                neighbors.append(left)
        if self.in_bounds(right):
            if self.cells[right[0]][right[1]] == letter:
                neighbors.append(right)

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

if __name__ == '__main__':
    main()
