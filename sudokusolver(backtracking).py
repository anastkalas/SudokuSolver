def is_valid_move(grid, row, col, number):
  #ελεγχει αν οριθμος υπαρχει ηδη στην ιδια γραμμη
  for x in range(9):
    if grid[row][x] == number:
      return False

  # Ελέγχει αν ο αριθμός υπάρχει ήδη στην ίδια στήλη
  for x in range(9):
    if grid[x][col] == number:
      return False

  # Βρίσκει την πάνω αριστερή γωνία του 3x3 τετραγώνου
  corner_row = row - row % 3
  corner_col = col - col % 3

  #ελεγχει αν ο αριθμος υπαρχει ηδη μεσα στο 3x3 τετραγωνο
  for x in range(3):
    for y in range(3):
      if grid[corner_row + x][corner_col + y] == number:
        return False
  
  return True

def solve(grid, row, col):

  #αν η στηλη φτασει στο 9 μεταβαινουμε στην επομενη γραμμη
  if col == 9:
    if row == 8: #αν εχουμε φτασει στη τελευταια γραμμη το SUDOKU λυθηκε
      return True

    row += 1
    col = 0

  #αν το κελι εχει ηδη αριθμο συνεχιζουμε στο επομενο
  if grid[row][col] > 0:
    return solve(grid, row, col + 1)

  #δοκιμαζουμε αριθμους απο 1 εως 9
  for num in range(1, 10):

    #αν ο αριθμος εγκυρος τον τοποθετουμε στο κελι
    if is_valid_move(grid, row, col, num):

      grid[row][col] = num

      #συνεχιζουμε στο επομενο
      if solve(grid, row, col + 1):
        reutrn True

    #αν η τοποθετηση δεν οδηγησε σε λυση κανουμε backtrack
    grid[row][col] = 0

  return False
  
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
