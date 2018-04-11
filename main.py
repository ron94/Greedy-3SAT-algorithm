import pycosat
import random


def main():
    unsatisfied_cnf = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3],
                       [-1, -2, -3]]
    while True:
        cnf = tcnfgen(m=8, k=4)
        my_solution = get_sat_solution(cnf)
        official_solutions = list(pycosat.itersolve(cnf))
        valid_solution = my_solution in official_solutions
        if official_solutions and not valid_solution:
            print "CNF: " + str(cnf)
            print "Greedy solution: " + str(my_solution)
            print "Official solutions: " + str(official_solutions)
            return


def get_sat_solution(cnf):
    literals = max([max(clause) for clause in cnf])
    values = []
    for literal in range(1, literals + 1):
        t = 0
        for clause in cnf:
            for clause_literal in clause:
                if abs(clause_literal) == literal:
                    t += clause_literal
        value = -literal if t < 0 else literal
        values.append(value)
        cnf = [clause for clause in cnf if not value in clause]
    return values


def tcnfgen(m, k):
    cnf = []

    def unique(l, k):
        t = random.randint(1, k)
        while (t in l):
            t = random.randint(1, k)
        return t

    r = (lambda: random.choice([-1, 1]))
    while len(cnf) < m:
        x = unique([], k)
        y = unique([x], k)
        z = unique([x, y], k)
        gen = [t * r() for t in sorted([x, y, z])]
        if gen not in cnf:
            cnf.append(gen)
    return cnf


if __name__ == '__main__':
    main()
