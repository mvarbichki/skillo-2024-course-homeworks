from db import dc


def employees_and_salary(sql_statement: str):
    result_list = []
    # skips id key and appends only the desired info
    for _, employee, salary in dc.db_fetch(sql_statement):
        result_list.append(f"Employee name: {employee},  salary: {salary}")
    return result_list
