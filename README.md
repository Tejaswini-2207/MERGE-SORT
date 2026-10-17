# Merge Sort — Advanced Algorithm Design

## 📌 About the Project

This repository contains Python implementations of **Merge Sort and its applications**, developed as part of my Advanced Algorithm Design practice.

The project focuses on the **Divide and Conquer** technique through scenario-based problems involving sorting, merging, linked lists, inversion counting, and external sorting.

Each problem includes a practical scenario, Python implementation, sample input/output, and time and space complexity analysis.

## 🎯 Objectives

- Understand the Divide and Conquer paradigm.
- Implement Merge Sort using recursion.
- Understand how two sorted arrays or lists are merged.
- Analyze time and auxiliary space complexity.
- Apply Merge Sort to real-world algorithmic problems.
- Practise algorithm design and problem-solving using Python.

## 🧠 Algorithm: Merge Sort

Merge Sort works in three stages:

1. **Divide:** Split the input array into two halves.
2. **Conquer:** Recursively sort both halves.
3. **Combine:** Merge the sorted halves into a single sorted array.

### Pseudocode

```text
MERGE_SORT(A):
    if length(A) <= 1:
        return A

    mid = length(A) // 2

    left = MERGE_SORT(A[0:mid])
    right = MERGE_SORT(A[mid:])

    return MERGE(left, right)
```

## 📂 Problems Implemented

| No. | Problem | Key Concept |
|---|---|---|
| 1 | Student Marks Sorting | Basic Merge Sort |
| 2 | Sorting Transaction Records | Index-based Merge Sort |
| 3 | Sorting a Singly Linked List | Recursive Divide and Conquer |
| 4 | Counting Inversions | Modified Merge Sort |
| 5 | Merging K Sorted Linked Lists | Pairwise Merging |
| 6 | Hospital Patient ID Sorting | Array Sorting |
| 7 | Employee Salary Sorting | Array Sorting |
| 8 | Sorting Prices in Descending Order | Modified Merge Procedure |
| 9 | Counting Inversions in an Array | Efficient Inversion Counting |
| 10 | Merging Two Sorted Arrays | Two-Pointer Technique |
| 11 | Sorting a Linked List | Slow/Fast Pointers and Merging |
| 12 | External Merge Sort | Sorting Large Datasets |

*Note: Update the problem titles or numbering if your actual Python files differ.*

## ⚙️ Technologies Used

- **Programming Language:** Python 3
- **Editor:** Visual Studio Code / GitHub Codespaces
- **Version Control:** Git and GitHub

## ▶️ How to Run the Programs

### Prerequisites

- Python 3 installed, or a GitHub Codespace with Python available.
- GitHub repository cloned or opened in Codespaces.

### Steps

1. Open the repository in VS Code or GitHub Codespaces.
2. Open the Python file you want to execute.
3. Open the integrated terminal.
4. Run the appropriate command:

```bash
python problem1.py
```

For a file containing spaces in its name:

```bash
python "problem 1.py"
```

Replace the filename with the name of the program you want to run.

## ⏱️ Time and Space Complexity

| Property | Complexity |
|---|---|
| Best-case time | O(n log n) |
| Average-case time | O(n log n) |
| Worst-case time | O(n log n) |
| Auxiliary space — array implementation | O(n) |
| Stability | Stable when equal elements are handled consistently |

The recurrence relation for standard Merge Sort is:

\[
T(n) = 2T(n/2) + \Theta(n)
\]

Using the Master Theorem:

\[
T(n) = \Theta(n \log n)
\]

## 🌍 Applications

Merge Sort and its variants can be applied to:

- Student ranking and marks management.
- Sorting financial transactions and employee records.
- Sorting linked lists.
- Counting inversions in arrays.
- Combining multiple sorted datasets.
- External sorting when datasets exceed available memory.

## 📚 Key Learnings

Through this project, I practised:

- Recursive algorithm design.
- Divide and Conquer problem-solving.
- Array manipulation and linked-list operations.
- Two-pointer merging techniques.
- Recurrence relations and complexity analysis.
- Applying sorting algorithms to practical scenarios.

## 🚀 Future Improvements

- Add implementations in C++ and Java.
- Include automated test cases for edge conditions.
- Compare Merge Sort with Quick Sort and other sorting algorithms.
- Add visualizations of recursive division and merging.

## 👩‍💻 Author

**Tejaswini**

This repository is part of my ongoing practice in Advanced Algorithm Design and Python-based problem-solving.

---

⭐ If you find this repository useful for learning sorting algorithms, feel free to explore the implementations and practise the problems.
