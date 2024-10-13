from collections import defaultdict
from typing import List, Tuple, Dict, Set, Any
from CSP import CSP

def AC3(csp: CSP, queue: List[Tuple[str, str]] = None, removals: Dict[str, Set[Any]] = None) -> bool:
    """AC-3 algorithm for constraint propagation."""
    if removals is None:
        removals = defaultdict(set)

    while queue:
        # Pop an arc (variable, neighbor)
        Xt, Xh = queue.pop()

        if remove_inconsistent_values(csp, Xt, Xh, removals):
            if not csp.domains[Xt]:
                return False
            
            # NOTE: Add neighboring arcs if the domain of Xt is revised
            for X in csp.adjList[Xt]:
                if X != Xh:
                    queue.append((X, Xt))

    return True

def remove_inconsistent_values(csp: CSP, Xt: str, Xh: str, removals: Dict[str, Set[Any]]) -> bool:
    """Remove inconsistent values from the domain of Xt."""
    revised = False

    for x in csp.domains[Xt].copy():
        # Check if there's any value in Xh's domain that does not conflict with x
        if all(csp.conflicts(Xt, x, Xh, y) for y in csp.domains[Xh]):
            csp.domains[Xt].remove(x)
            removals[Xt].add(x)
            revised = True

    return revised

def makeArcQueue(csp: CSP) -> List[Tuple[str, str]]:
    """Create a queue of all arcs using list comprehension"""
    return [(state, neighbor) for state in csp.adjList for neighbor in csp.adjList[state]]
