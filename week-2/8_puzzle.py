def dfs(start, goal): 
    stack = [(start, [start])] 
    visited = set() 
    
    while stack: 
        state, path = stack.pop() 
        
       
        if state == goal: 
            return path 
            
       
        if state in visited: 
            continue 
        visited.add(state) 
        
       
        zero = state.index(0) 
        row = zero // 3 
        col = zero % 3 
        
        moves = [] 
        if row > 0: moves.append(-3) # Up 
        if row < 2: moves.append(3)  # Down 
        if col > 0: moves.append(-1) # Left 
        if col < 2: moves.append(1)  # Right 
        
  
        for move in moves: 
            new_state = list(state) 
            new_pos = zero + move 
           
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero] 
            new_state = tuple(new_state) 
            
            if new_state not in visited: 
                stack.append((new_state, path + [new_state])) 
                
    return None 
  
 
start = (1, 2, 3, 4, 0, 6, 7, 5, 8) 
# Goal state 
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0) 

solution = dfs(start, goal) 
 
if solution: 
    print("Solution found!") 
    print("Moves:", len(solution) - 1) 
    for state in solution: 
        print() 
        print(state[0], state[1], state[2]) 
        print(state[3], state[4], state[5]) 
        print(state[6], state[7], state[8]) 
else: 
    print("No solution found.")
