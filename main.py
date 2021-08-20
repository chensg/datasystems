import os
import openpyxl
from pathlib import Path

from models import DimDate
from models import FactMaintenanceContractorPayment
from dbhelper import DatabaseHelper
import log

# set up logger
logger = log.setup_logger('root')

class MainApp(object):

    def __init__(self):
        self.data = []
        self.sheet = None

    def extract(self):
        # Step 1 Extract: use openpyxl library to open xls file and extract data from the file
        logger.debug(f"Starting Step 1 Extracting data from files")
        xlsx_file = Path('data', '41091_maintenanceStaffLogbookV1a.xlsx')
        wb_obj = openpyxl.load_workbook(xlsx_file)
        self.sheet = wb_obj.active
        logger.debug(f"we find {self.sheet.max_row} rows and {self.sheet.max_column} columns in file {xlsx_file}")
        logger.debug(f"Step 1 finished")

    def transform(self):
        # Step 2 Transform: the transform detail is located in the function transform of Model class
        # and we will put transformed model into a list

        logger.debug(f"Starting Step 2 transforming data")
        self.data = []
        for i, row in enumerate(self.sheet.iter_rows(values_only = True)):
            if i == 0:
                # we ignore the first row, which is the head titles
                continue

            if row[0] is None:
                # may be the last row
                continue
            
            logger.debug(f"transform data: {row}")
            payment_record = FactMaintenanceContractorPayment()
            payment_record.transform(row)
            self.data.append(payment_record)

        logger.debug(f"Step 2 finished")

    def load(self):
        # Step 3 Load: we will use model function save to load the data into database

        logger.debug(f"Starting Step 3 loading data into database")
        for model in self.data:
            logger.debug(f"load data into database: {model}")
            model.save()
        logger.debug(f"Step 3 finished")

    def mainLoop(self):
        # step 1
        self.extract()
        # step 2
        self.transform()
        # step 3
        self.load()

def main():
    # first of all, we need to clearn fact table for the demo proposal
    DatabaseHelper.getInstance().cleanFactTable()

    # create an instance of MainApp
    main = MainApp()
    main.mainLoop()

    # close database connection
    DatabaseHelper.getInstance().close()

if __name__ == "__main__":
    main()
