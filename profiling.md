# Average runtimes for AI Algorithms

## Random Algorithm
In a sample list of 12 boards...

1) ...with 1 remaining move to finish the game each, the execution lasted:
137 µs ± 19.1 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

2) with 4 remaining move to finish the game each, the execution lasted:
130 µs ± 2.49 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

3) with 7 remaining move to finish the game each, the execution lasted:
133 µs ± 12 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

## Unbeatable Algorithm
In a sample list of 12 boards...

1) ...with 1 remaining move to finish the game each, the execution lasted:
187 µs ± 6.62 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

2) with 4 remaining move to finish the game each, the execution lasted:
197 µs ± 12.2 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

3) with 7 remaining move to finish the game each, the execution lasted:
208 µs ± 14.1 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

# Remarks
It can be noticed that for the random algorithm, the running time remains similar when increasing the empty spots in the table.
In another hand, the unbeatable algorithm's running time increases the more empty cells there are. That's probably due to it's recursivity.
Because of how it is defined, the more empty spaces there are in the board, the more scenarios the unbeatable algorithm will have to evaluate with its minimax algorith.