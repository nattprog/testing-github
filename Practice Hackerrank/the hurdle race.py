print([[x for x in [-[int(i) for i in input("enter values n k: ").split()][1] + sorted({int(i) for i in input("enter heights: ").split()})[-1]] if x >= 0] + [0]][0][0])