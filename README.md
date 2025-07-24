# Flowers

## Task description
Residents of a newly built residential park want to beautify the area by planting flowers. Each resident offers to plant flowers in one or more flower beds along the boundary fence of the park. The offers are provided in the `offers.txt` file and include the range of flower bed numbers they wish to plant and the flower color. Each offer is represented by the starting and ending bed number (inclusive) and a single uppercase letter denoting the color. The number of flower beds does not exceed 3000.

The program reads the offers and answers several questions, including identifying overlapping offers, counting offers, and determining whether all flower beds are covered. The final result should also be written into a file named `colors.txt` indicating which flower bed got which color and by which offer.

## Files
- `offers.txt`: Contains the number of flower beds in the first line, followed by multiple lines describing each resident's offer (start, end, color).
- `colors.txt`: The output file listing, for each flower bed, the color and the index of the offer that resulted in the planting.

### Function 1
Reads and stores the data from the `offers.txt` file.

### Function 2
Prints the number of planting offers contained in the input file.

### Function 3
Identifies offers that cover both the first and last flower beds. Prints the offer indices separated by space.

### Function 4
Asks the user for a flower bed number and:
- Prints how many offers include that bed.
- Prints the color if only the first applicable offer is executed.
- Prints all possible colors if multiple offers apply.
- Prints a message if no offer includes that bed.

### Function 5
Determines whether all flower beds are covered, and if not, whether the planting could still be rearranged to cover all beds.

### Function 6
Performs the planting simulation in order of offers. Each bed is only planted once. Writes the final status to `colors.txt`, one line per bed: the planted color or '#' if unplanted, and the offer index or 0 if unplanted.

## Output files
After running the program, it generates a `colors.txt` file with one line per flower bed. This file is not included in the repository. It is automatically created during execution.

---
Developed by Áron Domonkos, 2024.