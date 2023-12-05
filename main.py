import os
import pandas as pd
import files
import execute



def main():
    datafile_folder = os.path.join("G:\My Drive\Desktop Files\DataSets for Visualizations\DateSets_2Dec2023\Restaurant\Restaurant+Orders+CSV")
    csv_files = files.get_file(datafile_folder)
    dataframes = []
    for file in csv_files:
        if file == 'order_details.csv':
            order_details = pd.read_csv(f"{datafile_folder}\{file}")
            # order_details['order_date'] = pd.to_datetime(order_details['order_date'])
            execute.dataLoad(order_details, order_details, file)
            dataframes.append(order_details)

if __name__ == "__main__":
    main()
