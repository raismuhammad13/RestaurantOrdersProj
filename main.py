import os
import pandas as pd
import util
import files



def main():
    datafile_folder = os.path.join("G:\My Drive\Desktop Files\DataSets for Visualizations\DateSets_2Dec2023\Restaurant\Restaurant+Orders+CSV")
    file = files.get_file(datafile_folder)
    print(file)

def bulkInsert(filename, tablename):

    query = f"""
            BULK INSERT {tablename}
            from '{filename}'
            WITH
            (
            FORMAT = 'CSV',
            FIRSTROW = 2,
            FILEDTERMINATOR = ',',
            ROWTERMINATOR = '\\n'
            )
        """
    return query


def getRecords(filename):
    pass


def insertRecords(tablename):
    pass


if __name__ == "__main__":
    main()
