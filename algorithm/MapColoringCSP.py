from CSP import CSP


class MapColoringCSP(CSP):
    def conflicts(self, state1, color1, state2, color2):
        # Check if two states are neighbors and have the same color
        return color1 == color2 and state2 in self.adjList[state1]
