import os
import pandas as pd
import files



def main():
    datafile_folder = os.path.join("G:\My Drive\Desktop Files\DataSets for Visualizations\DateSets_2Dec2023\Restaurant\Restaurant+Orders+CSV")
    csv_files = files.get_file(datafile_folder)
    dataframes = []
    for file in csv_files:
        # print(file)
        if file == 'order_details.csv':
            order_details = pd.read_csv(f"{datafile_folder}\{file}")
            order_details['order_date'] = pd.to_datetime(order_details['order_date'], format="%d/%m/%Y")
            # print(order_details)
            dataframes.append(order_details)
        if file == 'menu_items.csv':
            menu_items = pd.read_csv(f"{datafile_folder}\{file}")
            # print("-----------------")
            # print(menu_items.head(5))
            dataframes.append(menu_items)

if __name__ == "__main__":
    main()
