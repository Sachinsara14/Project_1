## 🧬 Project 1: Quick Bed Sort

**Goal:** Merge multiple compressed BED files, filter them against a "chromosome rulebook," and sort them first by chromosome (custom order) and then by start position.

### Files
* `project1.py`: The main Python script.
* `standard_selection.tsv`: A text file listing chromosomes to keep, in the specific desired order.

### Setup & Usage

1.  **Generate the Rulebook** (if not present):
    This command creates the standard human chromosome order (chr1-22, X, Y).
    ```bash
    (echo chr{1..22} | tr ' ' '\n'; echo chrX; echo chrY) > standard_selection.tsv
    ```

2.  **Run the Script:**
    ```bash
    python3 project1.py
    ```

**Output:** The script creates a directory `sorted_bed_file_per_sample/` containing the final merged and sorted BED file.
