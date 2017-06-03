# Program to get the length of longest connected 1's

class Graph:
 
    def __init__(self, row, col, g):
        self.count = 1
        self.row = row
        self.col = col
        self.graph = g
 
    def is_safe(self, i, j, visited):
        '''
        row number is in range, column number
        is in range and value is 1 
        and not yet visited
        '''
        return (i >= 0 and i < self.row and
                j >= 0 and j < self.col and
                not visited[i][j] and self.graph[i][j])
             
 
    
    def DFS(self, i, j, visited, count):
        '''
        A utility function to do DFS for a 2D 
        boolean matrix. It only considers
        the 8 neighbours as adjacent vertices
        '''
        row_num = [-1, -1, -1,  0, 0,  1, 1, 1];
        col_num = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.is_safe(i + row_num[k], j + col_num[k], visited):
                self.count += 1
                self.DFS(i + row_num[k], j + col_num[k], visited, self.count)
 
 
    #Function which retuens the largest connected graph
    def largest_connected(self):
        
        # Make a bool array to mark visited cells.
        # Default to False
        visited = [[False for j in range(self.col)]for i in range(self.row)]
 
        
        # Result as minimum
        result = - 111111111111111111 # -Infinity

        for i in range(self.row):
            for j in range(self.col):
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

    number_of_times = int(input('Enter Number of test cases: '))
    for i in range(number_of_times):
        row = int(input('Enter row number: '))
        col = int(input('Enter column number: '))

        # Input Matrix
        graph = [[int(input()) for x in range(col)] for y in range(row)]

        ####Sample Input:
        # 4
        # 4
        # 1 1 0 0
        # 0 1 1 0
        # 0 0 1 0
        # 1 0 0 0

        # graph = [[1,1,0,0],
        #         [0,1,1,0],
        #         [0,0,1,0],
        #         [1,0,0,0]]
         
        g= Graph(row, col, graph)
         
        print "Number of connected 1's are {} " .format(g.largest_connected())