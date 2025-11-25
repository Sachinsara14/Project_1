Goal: Merge multiple compressed BED files, filter them against a "chromosome rulebook," and sort them first by chromosome (custom order) and then by start position.

Files
project1.py: The main sorting script.

standard_selection.tsv: A text file listing chromosomes to keep, in the desired order.

Usage
Bash

# 1. Ensure your data files (shuf.a.bed.gz, etc.) and selection file are present.
# 2. Run the script:
python3 project1.py
Output: sorted_bed_file_per_sample/X.standard.sorted.bed
