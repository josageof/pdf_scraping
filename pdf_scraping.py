# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:47:42 2021

@author: Josa - josageof@gmail.com
"""

import os.path
from tabula import read_pdf
import pandas as pd


#%% busca o path no diretorio
directory = "folder_where_is_pdfs"

files_prop =[]
for root, subdirectories, files in os.walk(directory):
    for file in files:
        files_prop.append(os.path.join(root, file))
    break


#%% lança as tabelas de cada PCO em um Sheet do Excel
i = 0
df1_out = pd.DataFrame()
df2_out = pd.DataFrame()
print("")
for latest_file in files_prop:
    i += 1
    print("Reading "+str(i)+" file of "+str(len(files_prop))+" ...")
    print("")
    dfs_pdf = read_pdf(latest_file, pages="all")

    ## captura o CNPJ de interesse e popula o df_out
    for df1 in dfs_pdf:
        df1 = df1.T
        tabela1 = df1.apply(lambda row: row.astype(str).str.contains('CNPJ').any(), axis=1).sum()
        if tabela1 == 1:
            df1.insert(0, 'Arquivo', latest_file)
            # df1.drop(index=df1.index[0], axis=0, inplace=True)
            df1_out = df1_out.append(df1)

    ## captura o Total de interesse e popula o df_out
    for df2 in dfs_pdf:
        # df2 = df2.T
        tabela2 = df2.apply(lambda row: row.astype(str).str.contains('Total').any(), axis=1).sum()
        if tabela2 == 1:
            df2.insert(0, 'Arquivo', latest_file)
            # df2.drop(index=df2.index[0], axis=0, inplace=True)
            df2_out = df2_out.append(df2)


writer = pd.ExcelWriter('_pco2021.xlsx', engine='xlsxwriter')
df1_out.to_excel(writer, sheet_name="Revisão")
df2_out.to_excel(writer, sheet_name="Preço")
writer.close()
