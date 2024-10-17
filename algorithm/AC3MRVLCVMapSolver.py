# For some reason, AC3 is not recognized in my environment, so i need this to run
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from AC3 import *
from gui import MapColoringGUI
from AC3MapColoringSolver import AC3MapColoringSolver


class AC3MRVLCVMapSolver(AC3MapColoringSolver):
    # counts the conflict of color among a state's list of neighbors
    def count_conflict(self, csp, state, color):
        cnt = 0
        for neighbor in csp.adjList[state]:
            if color in csp.domains[neighbor]:
                cnt += 1
        return cnt

    # basically just pops the shortest element from array
    def popMin(self, array, key):
        minimum, idx = float("inf"), 0
        # basically find the shortest array
        for i in range(len(array)):
            if key(array[i]) < minimum:
                idx = i
                minimum = key(array[i])
        # put the shortest element to end of array to pop
        array[idx], array[-1] = array[-1], array[idx]
        return array.pop()

    def solveMapColoring(self, country_choice, states, neighbors, color_choices):
        csp = self.buildCspProblem(
            states, neighbors, color_choices
        )  # Creates the CSP using the inputted information

        # print(f"\n CSP ADJLIST\n {csp.adjList} \n")
        # print(f"\n CSP VARIABLES\n {csp.variables} \n")
        # print(f"\n CSP DOMAINS\n {csp.domains} \n")

        if not AC3(csp, makeArcQueue(csp)):
            print("No solution could be found.")
            return False

        # uncertain elements are those with colors > 1
        uncertain = []
        # csp.domains.items() = state: colorList
        for state, colors in csp.domains.items():
            if len(colors) > 1:
                uncertain.append(state)
        self.backtrack(csp, uncertain)

        if not self.backtrack(csp, uncertain):
            return False

        if self.backtrack(csp, uncertain):
            self.print_solution(csp, country_choice)

    def backtrack(self, csp, uncertain):
        if not uncertain:
            return True

        # selects the next state to assign a color to, using the Minimum Remaining Values (MRV) heuristic
        # key or lambda X is a function that just returns length of csp.domans
        # X is the state with min domains
        X = self.popMin(uncertain, key=lambda X: len(csp.domains[X]))

        removals = defaultdict(set)

        # Sort the values in domain in the order of LCV and loop in that order
        domainlist = list(csp.domains[X])
        domainlist.sort(key=lambda x: self.count_conflict(csp, X, x))

        # Attempting to assign a color
        for x in domainlist:
            # store the colors of X temporarily
            domainX = csp.domains[X]
            # build up new set of colors of X
            csp.domains[X] = set([x])
            if AC3(csp, makeArcQueue(csp), removals):
                retval = self.backtrack(csp, uncertain)
                if retval:
                    return True
            # Backtrack
            csp.restore_domains(removals)
            # Restore original domains
            csp.domains[X] = domainX
        # Put it back as uncertain
        uncertain.append(X)
        return False

    def print_solution(self, csp, country_choice):
        states_colors = {}
        for state, colors in csp.domains.items():
            if len(colors) == 1:
                states_colors[state] = next(iter(colors))
                # print(f"{state} ----> Color {next(iter(colors))}")
            else:
                print(f"{state}: No solution found")
        # print(states_colors)
        MapColoringGUI.ColorCountry(
            states_colors=states_colors, country_choice=country_choice
        )
