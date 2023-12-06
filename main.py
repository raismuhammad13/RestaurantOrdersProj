import os
import pandas as pd
import files
import execute
import util


def main():
    datafile_folder = os.path.join("G:\My Drive\Desktop Files\DataSets for Visualizations\DateSets_2Dec2023\Restaurant\Restaurant+Orders+CSV")
    csv_files = files.get_file(datafile_folder)
    
    for file in csv_files:
        if file == 'order_details.csv':
            order_details = pd.read_csv(f"{datafile_folder}\{file}")
            order_details['order_date'] = pd.to_datetime(order_details['order_date'])
            order_details['item_id'] = order_details['item_id'].fillna(0).astype(int)
            order_details.fillna("", inplace=True)
            connex = util.connection_to_db()
            cursor = connex.cursor()
            row_processed = 0
            for index, row in order_details.iterrows():
                row_processed = row_processed+1
                try:
                    cursor.execute("""
                                    INSERT INTO order_details ([order_details_id],
                                [order_id]
                                ,[order_date]
                                ,[order_time]
                                ,[item_id]) VALUES (?,?,?,?,?)
                                    """
                                , row['order_details_id'], row['order_id'], row['order_date'], row['order_time'], row['item_id']
                                )
                except Exception as e:
                    print("e", e)
            connex.commit()
            cursor.close()
            connex.close()
        if file == 'menu_items.csv':
            menu_items = pd.read_csv(f"{datafile_folder}\{file}")
            menu_items.fillna("", inplace=True)
            connex = util.connection_to_db()
            cursor = connex.cursor()
            row_processed = 0
            for index, row in menu_items.iterrows():
                row_processed = row_processed+1
                try:
                    cursor.execute("""
                                    INSERT INTO menu_items (
                                    [menu_item_id]
                                    ,[item_name]
                                    ,[category]
                                    ,[price])
                                    VALUES (?,?,?,?)
                                    """
                                , row['menu_item_id'], row['item_name'], row['category'], row['price']
                                )
                except Exception as e:
                    print("e", e)
            connex.commit()
            cursor.close()
            connex.close()



if __name__ == "__main__":
    main()
