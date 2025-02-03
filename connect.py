''' соединение с базой данных'''
from peewee import MySQLDatabase, Model, CharField, AutoField, IntegerField, \
                ForeignKeyField, DateField, TextField, TimeField


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


class TrainingCategories(BaseModels):
    '''классификации обучения'''
    name = CharField(unique=True)  # Название категории обучения
    description = TextField(null=True)  # Описание категории


class Trainings(BaseModels):
    ''' информация о мероприятия'''
    title = CharField()  # Название обучения
    description = TextField()  # Описание обучения
    date = DateField()  # Дата проведения
    category = ForeignKeyField(TrainingCategories, backref='trainings')
    materials = TextField(null=True)


class Materials(BaseModels):
    ''' материаллы для обучения'''
    title = CharField()  # Название материала
    file_path = CharField()  # Путь к файлу материала
    training = ForeignKeyField(Trainings, backref='materials')


class Absences(BaseModels):
    ''' запись об  отсутствии'''
    employee = ForeignKeyField(Employee, backref='absences')
    start_date = DateField()  # Начало отсутствия
    end_date = DateField()    # Конец отсутствия
    absence_type = CharField(choices=['Отпуск', 'Командировка', 'Невыход'])


class Replacements(BaseModels):
    ''' заменяющий сотрудник'''
    absence = ForeignKeyField(Absences, backref='replacements')
    replacement_employee = ForeignKeyField(Employee, backref='replacements')
    replacement_start_date = DateField()  # Дата начала замещения
    replacement_end_date = DateField()


class Events(BaseModels):
    ''' информация о мероприятиях'''
    title = CharField()  # Наименование мероприятия
    event_type = CharField(choices=['Собесед', 'Презентация', 'Обучение'])
    status = CharField(choices=['Запланировано', 'Проходит', 'Завершено'])
    date = DateField()  # Дата проведения
    time = TimeField()  # Часы проведения
    description = TextField(null=True)  # Краткое описание
    responsible = CharField(null=True)  # Ответственные лица


class MaterialsInform(BaseModels):
    ''' информация о материаллах'''
    title = CharField()  # Наименование материала
    approval_date = DateField(null=True)  # Дата утверждения
    modification_date = DateField(null=True)  # Дата изменения
    status = CharField(choices=['В работе', 'Утверждено', 'Отклонено'])
    material_type = CharField()  # Тип
    area = CharField()  # Область
    author = CharField()


class User(BaseModels):
    ''' авторизация'''
    id = AutoField()
    id_emplo = ForeignKeyField(Employee, backref='user')
    name = CharField()
    password = CharField()


db.connect()
db.create_tables([Department, Employee, EmployeeCard, EmployeeInformation,
                  TrainingCategories, Trainings, Materials, Absences,
                  Replacements, Events, MaterialsInform, User],
                 safe=True)
db.close()
