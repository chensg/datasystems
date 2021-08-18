from abc import ABCMeta
from abc import abstractmethod
from dbhelper import DatabaseHelper

class ModelAbstract(metaclass = ABCMeta):

    db = DatabaseHelper.getInstance().db()

    @abstractmethod
    def transform(self, row):
        pass

    @abstractmethod
    def selectOneByKeyValue(self, key_value):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def selectOneByField(self, field, value):
        pass

class DimDate(ModelAbstract):

    __tablename = 'dim_date'

    def __init__(self):
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

    def save(self):
        pass

    def selectOneByKeyValue(self, key_value):
        pass

    def selectOneByField(self, field, value):
        pass

class DimStaff(ModelAbstract):

    __tablename = 'dim_Staff'

    def __init__(self):
        self.staff_id = None
        self.staff_natural_id = None
        self.name = None
        self.contact_phone = None
        self.home_address = None
        self.email_address = None
        self.department = None

    def transform(self, row):
        pass

    def save(self):
        pass

    def selectOneByKeyValue(self, key_value):
        pass

    def selectOneByField(self, field, value):
        cursor = self.db.cursor()
        cursor.execute(f"select * from {self.__tablename} where {field}='{value}'")
        data = cursor.fetchone()
        if data:
            self.staff_id = data[0]
            self.staff_natural_id = data[1]
            self.name = data[2]
            self.contact_phone = data[3]
            self.home_address = data[4]
            self.execute = data[5]
            self.department_key = data[6]
        else:
            pass
        cursor.close()


class FactMaintenanceContractorPayment(ModelAbstract):

    __tablename = 'fact_Maintenance_Contractor_Payment'

    def __init__(self):
        self.payment_key = None
        self.date_key = None
        self.maintenance_job_key = None
        self.staff_key = None
        self.department_key = None
        self.travel_allowance_policy_key = None
        self.weather_Allowance_Policy_Key = None
        self.maintenance_hours = 0
        self.holiday_payment = 0
        self.length_of_travel = 0
        self.travel_allowance_amount = 0
        self.weather_condition = None
        self.weather_allowance_amount = 0
        self.total_amount_paid = 0
    
    def selectOneByKeyValue(self, key_value):
        pass

    def selectOneByField(self, field, value):
        pass
    
    def transform(self, row):
        staff_natural_key = row[0]
        # fetch staff id
        staff = DimStaff()
        staff.selectOneByField("Natural_Staff_ID", str(row[0])) #.strip()
        self.staff_key = staff.staff_id
        # fetch data key

        

    def save(self):
        pass