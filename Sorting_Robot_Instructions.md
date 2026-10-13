# CSC 225 — The Sorting Robot Lottery (Simplified)

**Coding mini-assignment | About 50 minutes | 50 points**

The sorting robots insist they are working hard. Your job is to keep **one list of comparison counts** for each robot. The campus has requested fewer spreadsheets and more common sense.

## 1. Randomly assign two algorithms — 5 points

Implement `choose_algorithms(seed)` using a seeded Python `random.Random(seed)` generator and `.sample(...)` to select **two distinct methods** from Bubble, Selection, Merge, Quick, and Heap. Record your seed in `Sorting_Robot_Results.md`. Do not redraw for a more convenient pair.

## 2. Create the `TimeSheet` class — 20 points

A `TimeSheet` object stores an `algorithm` name and a list `comparisons` of counts from separate runs. Implement:

- `__init__(algorithm)`: save the name and create an empty list.
- `add_run(count)`: append a nonnegative integer comparison count.
- `average()`: return the arithmetic mean.
- `median()`: return the middle count from sorted values (average the two middle counts if even).
- `minimum()` and `maximum()`: return the smallest and largest counts.
- `standard_deviation()`: compute the **population standard deviation** of the counts (divide by the number of runs, not one less).

For an empty list, all five statistics methods return `None`. Do not use the `statistics` module; implement the calculations. Built-in `sum`, `len`, `min`, `max`, and `sorted` are permitted in `TimeSheet`.

## 3. Implement your two assigned sorting methods — 20 points

Complete only the selected functions. Each must sort the supplied list **in place**, ascending, and return `(values, comparison_count)`. Count **comparisons between data values**, not loop or index checks. Helper functions are allowed; built-in `sort()` and `sorted()` are not allowed inside sorting functions.

- **Bubble:** Compare neighbors, swap out of order, stop on a pass with no swaps.
- **Selection:** Find the smallest item in the unsorted portion.
- **Merge:** Split recursively, merge sorted halves, count comparisons of front elements.
- **Quick:** Use the last element as pivot, count data-to-pivot comparisons.
- **Heap:** Use a max heap, count node-value comparisons when building and extracting.

## 4. Test using random lists of size 100 — 5 points

Run `python3 Sorting_Robot_Starter.py`. The supplied driver generates **50 random lists, each containing 100 integers**. Both chosen algorithms sort a copy of the **same list** on each run. The driver records the returned comparison counts in separate `TimeSheet` objects. It does not check sorting correctness.

Record the **50 comparison counts** for each algorithm, followed by its **average, median, minimum, maximum, and standard deviation**, in `Sorting_Robot_Results.md`. State which method used fewer comparisons across the 50 runs. No Big-O analysis or runtime measurement is required. Use the population standard deviation formula `sqrt(sum((x - mean)**2 for x in counts) / len(counts))`; you may use `math.sqrt` or `** 0.5`.

**Submit:** The URL to your public GitHub fork (with completed `Sorting_Robot_Starter.py` and `Sorting_Robot_Results.md`). No third-party Python packages required.

## 5. Publish your solution with a GitHub fork

**What is a fork?** A fork is your own copy of someone else's GitHub repository, stored under **your GitHub account**. You can edit and commit your solution without changing the instructor's original repository. **Cloning** then downloads your fork to your computer so you can work on it in VS Code or another editor.

1. **Fork the starter repository.** Open the GitHub repository link provided by your instructor. Click **Fork** (usually in the upper-right), choose your account as the owner, and select **Create fork**. Keep the repository public so it can be graded. **Do not fork a classmate's completed solution.**
2. **Clone your fork, not the instructor's original repository.** Open the green **Code** button on *your fork*, copy its HTTPS URL, and run:

   ```bash
   git clone https://github.com/YOUR-USERNAME/REPOSITORY-NAME.git
   cd REPOSITORY-NAME
   ```

   Replace the example with your fork's actual URL/repository name. The instructor will supply the real starter repository URL; none is assumed here.
3. **Complete the assignment.** Open the cloned folder in VS Code, implement your two selected algorithms and `TimeSheet` methods, and fill in `Sorting_Robot_Results.md`. Run:

   ```bash
   python3 Sorting_Robot_Starter.py
   ```

4. **Commit and push your work to your fork.** From inside your local cloned folder, run:

   ```bash
   git status
   git add Sorting_Robot_Starter.py Sorting_Robot_Results.md
   git commit -m "Complete Sorting Robot Lottery"
   git push origin HEAD
   ```

   If Git asks you to set your name/email, follow its instructions and retry the commit. Pushing publishes your commits to the fork on GitHub.
5. **Submit the GitHub URL of your fork** in the LMS (for example, `https://github.com/YOUR-USERNAME/REPOSITORY-NAME`). Check that the uploaded files and latest commit appear on your fork's page. **Do not submit a pull request** unless the instructor specifically asks for one.

**Reminder:** A fork lives on GitHub; a clone lives on your computer. `git push` sends your local commits back to **your fork**.

### Example statistics

```python
sheet = TimeSheet("Demo")
for count in [6, 2, 9, 3]:
    sheet.add_run(count)
# average = 5.0, median = 4.5, min = 2, max = 9, population standard deviation = 2.7386 (approximately)
```
