# comp-359-assignment-2

## TO-DO

- [x] GUI Setup
- [x] Matplotlib plots and graph setup
- [x] Research AC-3 arc-constraint algorithm
- [x] Implement AC-3 algorithm for checking
- [x] Load GeoJSON data from various countries
- [x] Load Neighbour and states JSON data

# Assignment 1

## Topic

**Implement a naive graph colouring algorithm (does not need to find the minimal number of colours) program with a GUI to visualize the colouring(s)**

<img width="712" alt="Screenshot 2024-10-18 at 9 15 06 PM" src="https://github.com/user-attachments/assets/c5e285a6-4196-46c8-9c86-a44f61e546f6">
<img width="712" alt="Screenshot 2024-10-18 at 9 15 11 PM" src="https://github.com/user-attachments/assets/9e067e0f-2b79-417d-81bf-8e1f9719b885">
<img width="712" alt="Screenshot 2024-10-18 at 9 15 15 PM" src="https://github.com/user-attachments/assets/3b18bda8-3346-4ea6-bb65-2b73b4f5b9db">
<img width="712" alt="Screenshot 2024-10-18 at 9 15 27 PM" src="https://github.com/user-attachments/assets/9f3cb27a-b60b-4a34-b2c3-eca8cb5834ca">
<img width="1112" alt="Screenshot 2024-10-18 at 9 15 34 PM" src="https://github.com/user-attachments/assets/474387c0-7cd9-41af-b47d-954c515910b3">



### Members

- Ishwak Sharda (300205473 - ishwak.sharda@student.ufv.ca)
- Kshitij Goyal (300197764 - kshitij.goyal@student.ufv.ca)
- Joshua Lepon (300189001 - joshuakarle.lepon@student.ufv.ca)

### Source code

- Python (GUI): https://github.com/shardaishwak/comp-359-assignment-2

---

### Requirements

### Planning

- Readme file: dividing the tasks, requirements, rubric and general progress of each user.
- Github: for keeping track of the code files, versioning, branching and issues.
  - Java Repository: https://github.com/shardaishwak/comp-359-assignment-1-java
  - Typescript Respository: https://github.com/shardaishwak/comp-359-assignment-1
- Github Board -We primary used Roadmap Check it out at: [https://github.com/users/shardaishwak/projects/1/views/4](https://github.com/users/shardaishwak/projects/1/views/4)

### Submission model

- Powerpoint presentation: describing briefly all the algorithms, space and time complexity, research involved and the specialty.

### Source:

- AC-3: http://redwood.cs.ttu.edu/~yuazhang/publications/ac3-1-ijcai01.pdf
- https://en.wikipedia.org/wiki/AC-3_algorithm
- https://medium.com/swlh/how-to-solve-constraint-satisfaction-problems-csps-with-ac-3-algorithm-in-python-f7a9be538cfe
- https://people.eecs.berkeley.edu/~russell/classes/cs188/f05/slides/chapter05-6pp.pdf
- https://chatgpt.com/share/67131118-07a8-800c-acd4-fd6b5ef475fa (wanted to integrate images in the canvas)

### Technologies required

- Python
- AC3
- Recursion (backtracking)
- KTinker

---

## Algorithms

### AC-3 (Arc Consistency Algorithm 3)

The AC-3 algorithm ensures arc consistency between variables in a **Constraint Satisfaction Problem (CSP)**. In a CSP, each variable has a domain of values, and constraints exist between variables. AC-3 operates by eliminating values from the domains that do not satisfy constraints.

### Arc Consistency Definition

For each pair of variables \(X_i, X_j\), AC-3 ensures that for every value \(x\) in the domain of \(X_i\), there exists a value \(y\) in the domain of \(X_j\) that satisfies the constraint. If no such \(y\) exists, \(x\) is removed from \(X_i\)'s domain.

### Algorithm Steps:

1. Start with a queue of arcs (pairs of variables with constraints).
2. For each arc \((X_i, X_j)\), check if any values in \(X_i\)'s domain conflict with \(X_j\)'s domain.
3. If a value \(x\) in \(X_i\)'s domain has no consistent value in \(X_j\), remove it.
4. If any value is removed, add neighboring arcs back into the queue to enforce consistency further.

The algorithm terminates when no more values can be removed, leaving the problem simpler.

### Pseudo-code:

```pseudocode
Algorithm PC
begin
  INITIALIZE(Q);
  while Q is not empty do
    Select and delete any ((i, x), j) from Q;
    REVISE PC((i, x), j, Q);
  endwhile
end
```

```pseudocode
Procedure INITIALIZE(Q)
begin
  for any i, j, k ∈ N do
    for any x ∈ D_i, y ∈ D_j such that c_ij(x, y) do
      if there is no z ∈ D_k such that c_ik(x, z) ∧ c_kj(z, y)
      then
        c_ij(x, y) ← false;
        c_ji(y, x) ← false;
        Q ← Q ∪ {(i, x), j} ∪ {(j, y), i};
      else
        ResumePoint((i, x), (j, y), k) ← z;
end
```

## Application to Graph Coloring

In the **Graph Coloring Problem**, variables represent the nodes, and the domains represent possible colors. Constraints exist between adjacent nodes that must not share the same color. AC-3 helps by pruning the domain of possible colors for each node based on its neighbors.

### Example:

If a node \(X_i\) has a domain of colors \( \{R, G, B\} \), and its neighbor already has the color \(R\), AC-3 will remove \(R\) from \(X_i\)’s domain, potentially leaving \( \{G, B\} \). This reduces the search space and makes finding a valid coloring easier.

### Formula:

Given a pair of nodes \(X_i\) and \(X_j\), the algorithm ensures that for each color \(x\) in \(X_i\)’s domain, there exists a color \(y\) in \(X_j\)’s domain such that \(x \neq y\). If no such \(y\) exists, \(x\) is removed from \(X_i\)’s domain:

\[
\forall x \in \text{Domain}(X_i), \exists y \in \text{Domain}(X_j) \text{ such that } x \neq y
\]

This constraint enforcement speeds up the graph coloring process by reducing the possibility of conflicts before backtracking occurs.

---

### Test suitcase

To ensure that our implementations of the algorithms are correct, we can develop a test suitcase to run on each algorithm. This suitcase makes sure that all the algorithms do sort accordingly given some input.

---

## Rubric

10 marks total (marked individually per team member)

- [1 mark] plan and logging of work
  - e.g., git log and Kanban task board
- [2 marks] references / citations
  - e.g., any format will be fine, APA, MLA, etc.
  - place in [README.md](http://readme.md/) file if code, or place at end of report in bibliography
- **[1 mark] apply the analysis framework, or collect others’ analysis results**
- [4 marks] one of the following
  - implementation,
  - or statistical experiment,
  - or writing about a collection of topics surrounding a data structure / problem
    - majority of the writing is yours---not simply copying quotes / AI as filler
- note that members of group can overlap in choice, but then must use different
  algorithm / implementation, or different programming language, or different computer
  hardware comparison, or different subtopic - in other words, not duplicating someone else’s work
- **[2 marks] debugging / testing code, or logical reasoning in your writing**
