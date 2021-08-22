from abc import ABCMeta
from abc import abstractmethod
import logging
from dbhelper import DatabaseHelper

class ModelAbstract(metaclass = ABCMeta):

    def __init__(self):
        self.db = DatabaseHelper.getInstance().db()
        self.tablename = ""
        self.primary_key = ""
        self.logger = logging.getLogger('root')

    @abstractmethod
    def transform(self, row):
        pass

    @abstractmethod
    def fillByDataSet(self, data):
        pass

    def selectOneByKeyValue(self, key_value):
        pass

    def save(self):
        # generate insert sql from class fields and save it to database
        fields = []
        values = []
        for key, value in self.__dict__.items():
            if key in ['db','logger', 'tablename', 'primary_key', self.primary_key]:
                continue
            fields.append(key)
            if value is None:
                values.append("null")
            else:
                values.append(str(value).lower())

        sql = f"insert into {self.tablename} ({','.join(fields)}) values ({','.join(['%s',]*len(fields))})"
        cursor = self.db.cursor(buffered = True)
        cursor.execute(sql, tuple(values))
        self.db.commit()
        cursor.close()

    def selectOneByField(self, field, value):
        # select one record by the given field and its value
        cursor = self.db.cursor(buffered = True)
        cursor.execute(f"select * from {self.tablename} where lower({field}) <=> %s", (value.lower(),))
        data = cursor.fetchone()
        if data:
            self.fillByDataSet(data)
        else:
            pass
        cursor.close()

    def selectOneByFields(self, dict):
        # the given fields and their values
        cursor = self.db.cursor(buffered = True)
        sql = ""
        values = []
        if len(dict) > 0:
            conditions = []
            for field, value in dict.items():
                conditions.append(f"lower({field}) <=> %s")
                values.append(value.lower())

            condition_sql = " and ".join(conditions)
            sql = f" where {condition_sql}"
        
        cursor.execute(f"select * from {self.tablename} {sql}", tuple(values))
        data = cursor.fetchone()
        if data:
            self.fillByDataSet(data)
        else:
            pass
        cursor.close()

class DimDate(ModelAbstract):

    def __init__(self):
        super(DimDate, self).__init__()
        self.tablename = 'dim_Date'
        self.primary_key = "date_key"
        self.date_key = None
        self.date_text = None
        self.day_name = None
        self.month_name = None
        self.month_number = None
        self.year = None
        self.is_holiday_NSW = False
        self.is_holiday_QLD = False
        self.is_holiday_VIC = False
    
    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.date_key = data[0]
        self.date_text = data[1]
        self.day_name = data[2]
        self.month_name = data[3]
        self.month_number = data[4]
        self.year = data[5]
        self.is_holiday_NSW = data[6]
        self.is_holiday_VIC = data[7]
        self.is_holiday_QLD = data[8]

class DimDepartment(ModelAbstract):

    def __init__(self):
        super(DimDepartment, self).__init__()
        self.tablename = 'dim_Department'
        self.primary_key = "department_key"
        self.department_key = None
        self.department_name = None
        self.department_location = None
        self.front_desk_phone = None
    
    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.department_key = data[0]
        self.department_name = data[1]
        self.department_location = data[2]
        self.front_desk_phone = data[3]

class DimMaintenanceJob(ModelAbstract):

    def __init__(self):
        super(DimMaintenanceJob, self).__init__()
        self.tablename = 'dim_Maintenance_Job'
        self.primary_key = "maintenance_job_key"
        self.maintenance_job_key = None
        self.maintenance_job_type_code = None
        self.maintenance_job_desc = None
        self.is_holiday = None
        self.hour_rate = None
    
    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.maintenance_job_key = data[0]
        self.maintenance_job_type_code = data[1]
        self.maintenance_job_desc = data[2]
        self.is_holiday = data[3]
        self.hour_rate = data[4]

class DimTravelAllowancePolicy(ModelAbstract):

    def __init__(self):
        super(DimTravelAllowancePolicy, self).__init__()
        self.tablename = 'dim_Travel_Allowance_Policy'
        self.primary_key = "travel_allowance_policy_key"
        self.travel_allowance_policy_key = None
        self.travel_allowance_policy_id = None
        self.vehicle_type = None
        self.allowance_per_km = None
    
    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.travel_allowance_policy_key = data[0]
        self.travel_allowance_policy_id = data[1]
        self.vehicle_type = data[2]
        self.allowance_per_km = data[3]

class DimWeatherAllowancePolicy(ModelAbstract):

    def __init__(self):
        super(DimWeatherAllowancePolicy, self).__init__()
        self.tablename = 'dim_Weather_Allowance_Policy'
        self.primary_key = "weather_allowance_policy_key"
        self.weather_allowance_policy_key = None
        self.policy_key = None
        self.weather = None
        self.weather_allowance = None
    
    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.weather_allowance_policy_key = data[0]
        self.policy_key = data[1]
        self.weather = data[2]
        self.weather_allowance = data[3]


class DimStaff(ModelAbstract):

    def __init__(self):
        super(DimStaff, self).__init__()
        self.tablename = 'dim_Staff'
        self.primary_key = "staff_id"
        self.staff_id = None
        self.staff_natural_id = None
        self.name = None
        self.contact_phone = None
        self.home_address = None
        self.email_address = None
        self.department = None

    def transform(self, row):
        pass

    def fillByDataSet(self, data):
        self.staff_id = data[0]
        self.staff_natural_id = data[1]
        self.name = data[2]
        self.contact_phone = data[3]
        self.home_address = data[4]
        self.execute = data[5]
        self.department_key = data[6]

class FactMaintenanceContractorPayment(ModelAbstract):

    def __init__(self):
        super(FactMaintenanceContractorPayment, self).__init__()
        self.tablename = 'fact_Maintenance_Contractor_Payment'
        self.primary_key = "payment_id"
        self.payment_id = None
        self.date_key = None
        self.maintenance_job_key = None
        self.staff_key = None
        self.department_key = None
        self.travel_allowance_policy_key = None
        self.weather_allowance_policy_key = None
        self.maintenance_hours = 0
        self.holiday_payment = 0
        self.length_of_travel = 0
        self.travel_allowance_amount = 0
        self.weather_condition = None
        self.weather_allowance_amount = 0
        self.total_amount_paid = 0
    
    def transform(self, row):
        # fetch staff id
        staff = DimStaff()
        staff.selectOneByField("Natural_Staff_ID", str(row[0]))
        self.staff_key = staff.staff_id

        # fetch data key
        dim_date = DimDate()
        dim_date.selectOneByField("Date_Text", row[6].strip())
        self.date_key = dim_date.date_key

        # fetch maintenance job key_value
        dim_job_key = DimMaintenanceJob()
        dim_job_key.selectOneByField("Maintenance_Job_Desc", row[8].strip())
        self.maintenance_job_key = dim_job_key.maintenance_job_key

        # fetch department key
        dim_department = DimDepartment()
        dim_department.selectOneByField("Department_Name", row[5].strip())
        self.department_key = dim_department.department_key

        # fetch travel allowance policy key
        dim_travel_allowance = DimTravelAllowancePolicy()
        dim_travel_allowance.selectOneByField("Vehicle_Type", row[10].strip())
        # if dim_travel_allowance.travel_allowance_policy_key is None:
        #    print(row)
        #    raise Exception()
        self.travel_allowance_policy_key = dim_travel_allowance.travel_allowance_policy_key

        # fetch weather allowance policy key
        dim_weather_allowance = DimWeatherAllowancePolicy()
        weather = row[11].strip().lower()
        if weather in ["sunny", "cloud"]:
            weather = "sunny cloud"
        dim_weather_allowance.selectOneByFields({"Weather" : weather, "Temperature" : row[12].strip()})
        self.weather_allowance_policy_key = dim_weather_allowance.weather_allowance_policy_key

        # transform other data
        self.maintenance_hours = float(row[7])

        if row[13].lower() == 'yes':
            self.holiday_payment = 1
        else:
            self.holiday_payment = 0

        self.length_of_travel = float(row[9])
        self.travel_allowance_amount = self.length_of_travel * float(row[16])
        self.weather_condition = row[11]
        self.weather_allowance_amount = float(row[18])

        # transform total amount paid
        work_payment = float(row[7]) * float(row[14])
        self.total_amount_paid = work_payment + self.travel_allowance_amount + self.weather_allowance_amount

        self.logger.debug(self.__dict__)

    def fillByDataSet(self, data):
        pass
