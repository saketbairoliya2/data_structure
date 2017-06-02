# Program to count islands in boolean 2D matrix
class Graph:
 
    def __init__(self, row, col, g):
        self.count = 1
        self.ROW = row
        self.COL = col
        self.graph = g
 
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1 
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
             
 
    # A utility function to do DFS for a 2D 
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, count):
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.count += 1
                self.DFS(i + rowNbr[k], j + colNbr[k], visited, self.count)
 
 
    #Function which retuens the largest connected graph
    def largest_connected(self):
        
        # Make a bool array to mark visited cells.
        # Set to False
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
 
        
        # Result as minimum
        result = -1111111111111111111111
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, 
                # then new connection found
                if visited[i][j] == False and self.graph[i][j] ==1:
                    # Visit all cells in this adjecency
                    # and increment 1's count
                    self.count = 1
                    self.DFS(i, j, visited, self.count)

                    result = max(result, self.count)
 
        return result

if __name__ == '__main__':

    number_of_times = input('Enter Number of test cases: ')
    for i in number_of_times:
        row = input('Enter row number: ')
        col = input('Enter column number: ')
        row = int(row)
        col = int(col)
        
        # Input Matrix
        graph = [[int(input()) for x in range(col)] for y in range(row)]

        # graph = [[1,1,0,0],
        #         [0,1,1,0],
        #         [0,0,1,0],
        #         [1,0,0,0]]
         
        g= Graph(row, col, graph)
         
        print "Number of connected 1's are"
        print g.largest_connected()