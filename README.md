The problem space is an n×n two-dimensional grid where n ≤ 6.
The starting cell is always at (1, 1).
From each cell, movement is allowed in eight possible directions.
We aim to find a path from the starting cell to the goal (G).
Some cells contain springs: upon entering such a cell, an enforced move must be made in a specified direction and magnitude.
For example, upon entering (2, 2), the agent is immediately moved to (1, 3).
The agent never moves outside the grid.
Some cells contain tunnels: upon entering a tunnel, the agent returns to the third immediately preceding location.
If no third preceding location exists, the agent returns to the starting cell.

---

Problem Space Construction:

After receiving n from the user, the problem space is constructed as follows:

· Two random numbers in the range [0, n-1] are generated, representing the goal location (row and column).
· A random number p in the range [0, 1] is generated, representing the number of tunnels.
· 2p random numbers in the range [0, n-1] are generated, representing the locations (rows and columns) of the tunnels.
· In each cell (except the start and goal cells), there is a 30% probability of a spring. The springs are inserted as follows:
  · A random number in the range [1, 8] is selected for the spring direction (direction numbers correspond to movement directions as shown in Figure 1).
  · A random number in the range [1, 2] is selected for the move magnitude.
