import util


def insertQuery(df, file):
    tablename = file.split('.')[0]
    column_names = list(df.columns.values)
    column_names_string = ', '.join(column_names)
    column_values = tuple(map(lambda column: column.replace(column, '?'), column_names))
    column_values_string = ', '.join(column_values)
    
    query = f"""
                INSERT INTO {tablename} ({column_names_string}) VALUES ({column_values_string})
    
            """
    
    return query

def dataLoad(dataframe, order_details, file):
    query = insertQuery(order_details, file)

    connex = util.connection_to_db()
    cursor = connex.cursor()
    
    print(query)
    for index, row in dataframe.iterrows():
        cursor.execute(query, row.order_details_id, row.order_id, row.order_date, row.order_time, row.item_id)
    connex.commit()
    cursor.close()
    connex.close()
    