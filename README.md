[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8587220&assignment_repo_type=AssignmentRepo)
| EAPS 591 - Numerical Modeling of Planetary Orbits | Fall 2022 | [YOUR NAME] |
| ----------------------------- | --------- | ------------------ |

# Module 5 - Symplectic Integrators - Code infrastructure
## Problems 1-3. Kepler Solvers

### Instructions for using the Kepler solver code
Problem 1:
Since the new value of E is just a function of the previous values, I made a list of every value of E. 
I then ran code using an equation for the new value of E based on the equation for the problem, using [-1] to call on the previous value.
I used a while true loop to continue the process until the difference between the last two values was at the desired accuracy of 0.000001 degrees.
The output was saved as a csv file in my data folder. 

