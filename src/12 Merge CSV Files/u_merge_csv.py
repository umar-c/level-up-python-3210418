import csv
import pandas

# See https://stackoverflow.com/questions/26599137/merge-csvs-in-python-with-different-columns
# for reference.

def merge_csv(list_input_csv_files, output_csv_file = 'output.csv'):
    if len(list_input_csv_files) == 0:
        print('At least one input file is required! Exiting...')
        return

    fieldnames = []
    for file in list_input_csv_files:
        with open(file, 'rt', encoding='utf-8') as fin:
            fields = csv.DictReader(fin).fieldnames
            fieldnames.extend(f for f in fields if f not in fieldnames)
            
    with open(output_csv_file, 'wt', encoding='utf-8') as fout:
        csv_file_writer = csv.DictWriter(fout, fieldnames=fieldnames)
        csv_file_writer.writeheader()
        for file in list_input_csv_files:
            with open(file, 'rt', encoding='utf-8') as fin:
                csv_file_reader = csv.DictReader(fin)
                for line in csv_file_reader:
                    csv_file_writer.writerow(line)

def merge_csv_pandas(list_input_csv_files, output_csv_file = 'output.csv'):
    if len(list_input_csv_files) == 0:
        print('At least one input file is required! Exiting...')
        return
    
    list_of_data_frames = []
    for file in list_input_csv_files:
        data_frame = pandas.read_csv(file)
        list_of_data_frames.append(data_frame)

    merged_frame = pandas.concat(list_of_data_frames, ignore_index=True)
    print(merged_frame)

    merged_frame.to_csv(output_csv_file, index=False)

# commands used in solution video for reference
if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
    merge_csv_pandas(['class1.csv', 'class2.csv'], 'all_students_pandas.csv')
