import gzip

good_chromosome = set()
chromosome_order = []

with open("standard_selection.tsv", "r") as f_1:
  for line in f_1:
    chromosome = line.strip()
    good_chromosome.add(chromosome)
    chromosome_order.append(chromosome)

data_to_sort = {}

file_list = ["shuf.a.bed.gz", "shuf.b.bed.gz"]

for bed_file in file_list:
  with gzip.open(bed_file, "rt") as f:
    for line in f:
      column = line.split('\t')
      chromosome = column[0]
      if chromosome in good_chromosome:
        if chromosome not in data_to_sort:
          data_to_sort[chromosome] = []
        data_to_sort[chromosome].append(line)


open_filename = "sorted_bed_file_per_sample/X.standard.sorted.bed"

with open(open_filename, "w") as out_file:
  for chromosome in chromosome_order:
    line_list = data_to_sort.get(chromosome, [])
    line_list.sort(key=lambda bed_line: (int(bed_line.split('\t')[1]), int(bed_line.split('\t')[2])))
    for bed_line in line_list:
          out_file.write(bed_line)
