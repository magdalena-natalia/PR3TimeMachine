import datetime


def ask_for_input(question):
    """ Ask an user for input. """
    response = ''
    while not response:
        response = input(question)
    return response


def ask_for_date(question):
    """ Ask an user for a date and return it as datetime object. """
    response = ask_for_input(question)
    try:
        response_date_obj = datetime.datetime.strptime(response, '%d.%m.%Y')
    except ValueError:
        response_date_obj = None
        ask_for_date(question)
    return response_date_obj


