import util

def insertQuery(df, file):
    tablename = file.split('.')[0]
    column_names = list(df.columns.values)
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '?'), column_names))
    column_values_string = ', '.join(column_values)
    column_to_insert = ', '.join([f"row['{column}']" for column in column_names])
    
    query = f"""
            INSERT INTO {tablename} ({column_names_string}) VALUES ({column_values_string})
    
            """
    
    return query, column_to_insert

def dataLoad(dataframe, file):
    query, column_to_insert = insertQuery(dataframe, file)
    connex = util.connection_to_db()
    cursor = connex.cursor()
    row_processed = 0
    for index, row in dataframe.iterrows():
        print(row)
        row_processed = row_processed+1
        cursor.execute(query+column_to_insert)
        try:
            
            cursor.execute(f"""
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