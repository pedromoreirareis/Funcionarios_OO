from utils.date_formatters import date_to_str


def prepare_employee_log(employee):
    employee_log = {}

    employee_dict = employee._asdict()
    registration = employee_dict["matricula"]
    employee_dict["dt_nasc"] = date_to_str(employee_dict["dt_nasc"])
    employee_log[registration] = employee_dict

    return employee_log


def prepare_json_export(employee_tuple):
    employee_json = {}

    for registration, employee in employee_tuple.items():
        employee_dict = employee._asdict()
        employee_dict["dt_nasc"] = date_to_str(employee_dict["dt_nasc"])
        employee_json[registration] = employee_dict

    return employee_json
