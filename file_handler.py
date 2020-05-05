import xlrd
import json
# def make_json_from_data(header, column_names, row_data):
   
#     row_list = []
#     for item in row_data:
#         json_obj = {}
#         for i in range(0, column_names.__len__()):
#             json_obj[column_names[i]] = item[i]
#         row_list.append(json_obj)
#     result_dict = {}
#     for i, e in enumerate(row_list):
        
#         result_dict[header[i]] = e
        
#     return result_dict

# def xls_to_dict(workbook_url):
#     """
#     Convert the read xls file into JSON.
#     """
#     workbook_dict = {}
#     book = xlrd.open_workbook(workbook_url)
#     sheets = book.sheets()
#     for sheet in sheets:
        
       
#         header = sheet.col_values(0,2)
#         columns = sheet.row_values(1)
#         rows = []
#         for row_index in range(2, sheet.nrows):
#             row = sheet.row_values(row_index)
#             rows.append(row)
#     return make_json_from_data(header,columns, rows)
    
def make_json_from_data(column_names, row_data):
    """
    take column names and row info and merge into a single json object.
    :param data:
    :param json:
    :return:
    """
    row_list = []
    for item in row_data:
        json_obj = {}
        for i in range(0, column_names.__len__()):
            json_obj[column_names[i]] = item[i]
        row_list.append(json_obj)
    return row_list

def xls_to_dict(workbook_url):
    """
    Convert the read xls file into JSON.
    :param workbook_url: Fully Qualified URL of the xls file to be read.
    :return: json representation of the workbook.
    """
    workbook_dict = {}
    book = xlrd.open_workbook(workbook_url)
    sheets = book.sheets()
    for sheet in sheets:
        if sheet.name == 'PortHoles & Discrete Appurtenan':
            continue
        workbook_dict['plants'] = {}
        columns = sheet.row_values(0)
        rows = []
        for row_index in range(1, sheet.nrows):
            row = sheet.row_values(row_index)
            rows.append(row)
        sheet_data = make_json_from_data(columns, rows)
        workbook_dict['plants'] = sheet_data
    return workbook_dict
# Sample Call: 
sample = xls_to_dict('C:/Users/dorms/Desktop/plant_data.xlsx')
print(sample)

with open('data1.txt', 'w') as outfile:
    json.dump(sample, outfile, indent=4, separators=(',', ':'))
    
    
def return_json_from_data(header, column_names, row_data):
       
    row_list = []
    for item in row_data:
        json_obj = {}
        for i in range(0, column_names.__len__()):
            json_obj[column_names[i]] = item[i]
        row_list.append(json_obj)
    result_dict = {}
    for i, e in enumerate(row_list):
        
        result_dict[header[i]] = e
        
    return result_dict

def table_to_dict(workbook_url):
    """
    Convert the read xls file into JSON.
    """
    book = xlrd.open_workbook(workbook_url)
    sheets = book.sheets()
    for sheet in sheets:
        
       
        header = sheet.col_values(0,1)
        columns = sheet.row_values(1,1)
        rows = []
        for row_index in range(2, sheet.nrows):
            row = sheet.row_values(row_index,1)
            rows.append(row)
    return return_json_from_data(header,columns, rows)
# Sample Call: 
# sample = xls_to_dict('C:/Users/dorms/Desktop/response.xlsx')
# print(sample)

# with open('response.txt', 'w') as outfile:
#     json.dump(sample, outfile, indent=4, separators=(',', ':'))