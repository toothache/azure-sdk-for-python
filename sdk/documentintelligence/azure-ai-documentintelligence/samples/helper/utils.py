# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: utils.py

DESCRIPTION:
    These util functions provide an intuitionistic way to organize data. Make sample code more concise.
"""

def print_table(header_names, table_data):
    """Print a two-dimensional array like a table.

    Based on provided column header names and two two-dimensional array data, print the strings like table.

    Args:
        header_names: An array of string, it's the column header names.  e.g. ["name", "gender", "age"]
        table_data: A two-dimensional array, they're the table data.  e.g. [["Mike", "M", 25], ["John", "M", 19], ["Lily", "F", 23]]
    Return: None
        It's will print the string like table in output window. e.g.
         Name    Gender    Age
         Mike    M         25
         John    M         19     
         Lily    F         23
    """
    max_len_list = []
    for i in range(len(header_names)):
        col_values = list(map(lambda row: len(str(row[i])), table_data))
        col_values.append(len(str(header_names[i])))
        max_len_list.append(max(col_values))

    row_format_str = "".join(map(lambda len: f"{{:<{len + 4}}}", max_len_list))

    print(row_format_str.format(*header_names))
    for row in table_data:
        print(row_format_str.format(*row))
