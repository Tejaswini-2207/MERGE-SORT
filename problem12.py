#External Merge Sort — Large Files

import heapq
import os
import tempfile


def external_merge_sort(input_file, output_file, chunk_size=1000):
    temp_files = []

    try:
        # Read and sort manageable chunks
        with open(input_file, "r") as f:
            while True:
                values = []

                for _ in range(chunk_size):
                    line = f.readline()
                    if not line:
                        break
                    values.append(int(line.strip()))

                if not values:
                    break

                values.sort()

                temp = tempfile.NamedTemporaryFile(
                    mode="w",
                    delete=False,
                    encoding="utf-8"
                )
                temp_files.append(temp.name)

                with temp:
                    for value in values:
                        temp.write(str(value) + "\n")

        # Merge sorted files
        files = [open(name, "r") for name in temp_files]

        try:
            streams = (
                (int(line.strip()) for line in f)
                for f in files
            )

            with open(output_file, "w", encoding="utf-8") as out:
                for value in heapq.merge(*streams):
                    out.write(str(value) + "\n")
        finally:
            for f in files:
                f.close()

    finally:
        for name in temp_files:
            if os.path.exists(name):
                os.remove(name)


# Create a small sample input file
with open("transactions.txt", "w") as f:
    f.write("500\n100\n900\n200\n300\n")

external_merge_sort(
    "transactions.txt",
    "sorted_transactions.txt",
    chunk_size=2
)

with open("sorted_transactions.txt", "r") as f:
    print("Sorted transactions:")
    print(f.read(), end="")
