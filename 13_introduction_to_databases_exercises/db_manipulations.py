from db import dc
from utilities import is_str


def get_employees_and_salary(sql_statement: str):
    result_list = []
    if is_str(sql_statement):
        try:
            # skips id key and appends only the names and salaries
            for _, employee, salary in dc.db_fetch(sql_statement):
                result_list.append(f"Employee name: {employee},  salary: {salary}")
            return result_list
        # returns sqlite code and error name
        except dc.db_exceptions() as e:
            return e.sqlite_errorcode, e.sqlite_errorname
    else:
        return "Incorrect argument"


def insert_new_product(sql_statement: str):
    if is_str(sql_statement):
        try:
            dc.db_execute(sql_statement)
            dc.db_commit()
            return "Record added"
        except dc.db_exceptions() as e:
            return e.sqlite_errorcode, e.sqlite_errorname
    else:
        return "Incorrect argument"
