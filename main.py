import openpyxl
from pathlib import Path
from models import DimDate
from models import FactMaintenanceContractorPayment
from dbhelper import DatabaseHelper
import logging
import os

# logging setting begin
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
cur_dir = os.path.abspath(__file__).rsplit("\\", 1)[0]
# set two handlers
log_file = "{}.log".format(__file__)
# rm_file(log_file)
fileHandler = logging.FileHandler(os.path.join(cur_dir, log_file), mode = 'w')
fileHandler.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# set formatter
formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# add
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

# logging setting end


# Step 1: use openpyxl library to open xls file and extract data from the file
xlsx_file = Path('data', '41091_maintenanceStaffLogbookV1a.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active
logger.debug(f"we find {sheet.max_row} rows and {sheet.max_column} columns in file {xlsx_file}")

# Step 2 Transform: the transform detail is located in the function transform of Model class
# and we will put transformed model into a list

data = []
for i, row in enumerate(sheet.iter_rows(values_only = True)):

    if i == 0:
        # we ignore the first row, which is just the head titles
        continue

    if row[0] is None:
        # may be the last row
        continue
    
    logger.debug(f"transform data: {row}")
    payment_record = FactMaintenanceContractorPayment()
    payment_record.transform(row)
    data.append(payment_record)

# Step 3 Load: we will use model function save to load the data into database

for model in data:
    logger.debug(f"load data into database: {model}")
    model.save()

# close database connection

DatabaseHelper.getInstance().close()
