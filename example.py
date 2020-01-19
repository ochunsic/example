#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def save_excel_file(csv_file_path, sep, encoding):
    path = r'C:\testpy\8_1_COMMENT.csv'
    df = pd.read_csv(path, sep=sep, encoding=encoding)
    #df['농심 2F 8_1 PLC_01 20190103백업']
    columns = ['Device Name', 'Comment']
    s = df['농심 2F 8_1 PLC_01 20190103백업'][1:]
    df_new = pd.DataFrame({'Device Name': s.index, 'Comment': s.to_list()})
    device_category = ['M', 'D', 'T', 'L', 'X', 'Y']
    with pd.ExcelWriter('output.xlsx') as writer:
        for category in device_category:
            df_device = df_new[df_new['Device Name'].str.startswith(category)]
            df_device.to_excel(writer, sheet_name=category, index=False)

def main():
    path = r'C:\testpy\8_1_COMMENT.csv'
    save_excel_file(path, sep='\t', encoding='utf-16')

def merge_dataframe():
    #merge example
    df_a = pd.DataFrame({'a': range(5), 'b': range(5)})
    df_b = pd.DataFrame({'c': range(5, 10), 'd': range(5, 10)})
    df_a.join(df_b)


if __name__ == '__main__':
    main()