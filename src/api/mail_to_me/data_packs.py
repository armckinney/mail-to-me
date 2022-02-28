from flask import request


def form_dict(field_list):
    # collecting items from form and making data dictionary

    form_data = {}

    # looping through passed field list
    for field in field_list:

        field_value = request.form[field]

        # adding to data dictionary if user selection made
        if field_value != "":
            form_data[field] = field_value

    return form_data
