import util
import os
import files

connex = util.connection_to_db()
cursor = connex.cursor()
query1 = """
        INSERT INTO [dbo].[order_details]
           ([order_details_id]
           ,[order_id]
           ,[order_date]
           ,[order_time]
           ,[item_id]) 
        values(12236, 5372, getdate(), '11:11:11 AM', 161.0)
    """
query = """
        select * from [dbo].[order_details]
    """
# print(query)
cursor.execute(query1)
connex.commit()
cursor.close()
connex.close()
for val in cursor:
    print(val)


# cursor.execute("select * from order_details;")
# for i in cursor:
#     print(i)

# def bulkInsert(filename):

#     query = f"""
#             BULK INSERT {tablename}
#             from '{filename}'
#             WITH
#             (
#             FORMAT = 'CSV',
#             FIRSTROW = 2,
#             FILEDTERMINATOR = ',',
#             ROWTERMINATOR = '\\n'
#             )
#         """
#     return query




# def getRecords(filename):
#     pass


# def insertRecords(tablename):
#     pass