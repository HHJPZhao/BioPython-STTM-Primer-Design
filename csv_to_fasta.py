
#!/usr/bin/env python3

import sys
import re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def csv_to_fasta(infile, outfile):
    total = 0

    with open(infile, "r") as fin, open(outfile, "w") as fout:

        for line in fin:
            match = re.search(
                r"(?P<ID>\w+),(?P<seq>\w+)", line
            )

            if match:
                seq_id = "nbt-" + match.group("ID")
                seq = match.group("seq")

                total += 1

                seq_obj = SeqRecord(
                    Seq(seq),
                    id=seq_id,
                    description=""
                )

                print(
                    f"{total}:{seq_obj.id}|{seq_obj.seq}"
                )

                SeqIO.write(seq_obj, fout, "fasta")

    print(f"Total sequences processed: {total}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: python csv_to_fasta.py "
            "input.csv output.fasta"
        )

    csv_to_fasta(sys.argv[1], sys.argv[2])
