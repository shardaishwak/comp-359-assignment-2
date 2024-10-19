from typing import List, Dict, Set, Any


class CSP:
    def __init__(
        self,
        variables: List[str] = None,
        adjList: Dict[str, List[str]] = None,
        domains: Dict[str, Set[Any]] = None,
    ):
        self.variables = variables if variables is not None else []
        self.adjList = adjList if adjList is not None else {}
        self.domains = domains if domains is not None else {}

    def restore_domains(self, removals: Dict[str, Set[Any]]) -> None:
        """Restore domains from removals by adding back removed values."""
        for X, removed_values in removals.items():
            if X in self.domains:
                self.domains[X].update(removed_values)
    def is_consistent(self, state1, color1, state2, color2):
        # Check if two states are neighbors and have the same color
        return state2 not in self.adjList[state1] or color1 != color2
