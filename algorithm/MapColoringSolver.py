from collections import defaultdict
from MapColoringCSP import MapColoringCSP


class MapColoringSolver(object):
    def addEdge(self, state1, state2, adjList):
        # add neighborstate to state
        adjList[state1].add(state2)

    def buildCspProblem(self, states, neighbors, color_choices):

        adjList = defaultdict(
            set
        )  # sets each key's default value as a set (helps prevent repetition)

        # Build graph (constraints) based on neighboring information
        # state1 is the state we are finding neigbours for
        # adjStates are the neighbors
        for state1, adjStates in neighbors.items():
            for state2 in adjStates:
                self.addEdge(state1, state2, adjList)

        # Set domains (colors available for each state)
        variables = list(states.keys())

        domains = {state: color_choices.copy() for state in states}

        # Adjslist is a dict set with key of state and values of neighboring states
        # Variables contains the "keys", in this case, the states
        # Domain contains a dict with key of state and values of assigned colors
        return MapColoringCSP(variables, adjList, domains)

    def solveMapColoring(self, country_choice, states, neighbors, color_choices):
        pass
