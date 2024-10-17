from AC3 import *
from MapColoringSolver import MapColoringSolver
from collections import defaultdict


class AC3MapColoringSolver(MapColoringSolver):
    def solveMapColoring(self, country_choice, states, neighbors, color_choices):
        csp = self.buildCspProblem(states, neighbors, color_choices)

        AC3(csp, makeArcQueue(csp))

        uncertain = []
        for state, colors in csp.domains.items():
            if len(colors) > 1:
                uncertain.append(state)
        self.backtrack(csp, uncertain)

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True
        X = uncertain.pop()
        removals = defaultdict(set)
        for x in csp.domains[X]:
            domainX = csp.domains[X]
            csp.domains[X] = set([x])
            if AC3(csp, makeArcQueue(csp, [X]), removals):
                retval = self.backtrack(csp, uncertain)
                if retval:
                    return True
            csp.restore_domains(removals)
            csp.domains[X] = domainX
        uncertain.append(X)
        return False
