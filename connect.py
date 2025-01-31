''' соединение с базой данных'''
from peewee import MySQLDatabase, Model, CharField, AutoField, IntegerField, \
                    ForeignKeyField, DateField


db = MySQLDatabase('corporation', user='root', password='lenok',
                   host='localhost', port=3306)


class BaseModels(Model):
    ''' hjh'''
    class Meta:
        ''' kjk'''
        database = db


class Department(BaseModels):
    ''' информация о подразделениях и должностях'''
    id = AutoField()
    description = CharField()
    director = CharField()
    assistant = CharField()


class Employee(BaseModels):
    ''' информация по сотруднику'''
    id = AutoField()
    fcs = CharField()
    department = ForeignKeyField(Department, backref='employee')
    post = CharField()
    work_phone = CharField()
    personal_phone = CharField(null=True)
    office = IntegerField()
    cor_email = CharField()
    birth_date = CharField(null=True)


class EmployeeCard(BaseModels):
    ''' карточка сотрудника'''
    id = AutoField()
    fcs = CharField()
    mobile_phone = CharField()
    date_birth = DateField()
    department = ForeignKeyField(Department, backref='employeecard')
    position = CharField()
    director = ForeignKeyField(Department, backref='emoloyeecard')
    assistant = ForeignKeyField(Department, backref='emoloyeecard')
    work_phone = CharField()
    email = CharField()
    cabinet = CharField(max_length=10)
    other_information = CharField()


class EmployeeInformation(BaseModels):
    ''' сведения о работнике - занятость'''
    id = AutoField()
    id_employee = ForeignKeyField(Employee, backref='employeeinformation')
    training_calendar = DateField()
    absence = CharField()
    vacation = CharField()
    start_vac = DateField()
    end_vac = DateField()


db.connect()
db.create_tables([Department, Employee, EmployeeCard, EmployeeInformation],
                 safe=True)
db.close()
