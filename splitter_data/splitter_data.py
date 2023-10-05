import pandas as pd


def split_and_write(input_file, parts=3):
  """Split a CSV file into parts and write each part to a separate file.

  Args:
    input_file: The path to the CSV file to split.
    parts: The number of parts to split the CSV file into.
  """

  # Read the CSV file into a DataFrame.
  df = pd.read_csv('datasets/cd.csv')

  # Calculate the number of rows in each part.
  rows_per_part = len(df) // parts
  # If there is a remainder, add it to the last part.
  if len(df) % parts > 0:
    rows_per_part += 10

  # Iterate over the parts, writing each part to a separate file.
  for i in range(parts):
    # Get the part of the DataFrame for this iteration.
    part = df[i * rows_per_part:(i + 1) * rows_per_part]

    # Create the output file path.
    output_file_path = f'part{i + 1}.csv'

    # Write the part to the output file, without the index.
    part.to_csv(output_file_path, index=False)


# Run the function.
split_and_write('data.csv')
