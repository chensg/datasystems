import os
import openpyxl
from pathlib import Path

from models import DimDate
from models import FactMaintenanceContractorPayment
from dbhelper import DatabaseHelper
import log

# set up logger
logger = log.setup_logger('root')

# first of all, we need to clearn fact table for the demo proposal
DatabaseHelper.getInstance().cleanFactTable()

# Step 1 Extract: use openpyxl library to open xls file and extract data from the file
logger.debug(f"Starting Step 1 Extracting data from files")
xlsx_file = Path('data', '41091_maintenanceStaffLogbookV1a.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active
logger.debug(f"we find {sheet.max_row} rows and {sheet.max_column} columns in file {xlsx_file}")
logger.debug(f"Step 1 finished")

# Step 2 Transform: the transform detail is located in the function transform of Model class
# and we will put transformed model into a list

logger.debug(f"Starting Step 2 transforming data")
data = []
for i, row in enumerate(sheet.iter_rows(values_only = True)):

    if i == 0:
        # we ignore the first row, which is the head titles
        continue

    if row[0] is None:
        # may be the last row
        continue
    
    logger.debug(f"transform data: {row}")
    payment_record = FactMaintenanceContractorPayment()
    payment_record.transform(row)
    data.append(payment_record)
logger.debug(f"Step 2 finished")

# Step 3 Load: we will use model function save to load the data into database

logger.debug(f"Starting Step 3 loading data into database")
for model in data:
    logger.debug(f"load data into database: {model}")
    model.save()
logger.debug(f"Step 3 finished")

# close database connection

DatabaseHelper.getInstance().close()
