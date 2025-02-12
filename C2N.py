import os
import pandas as pd
import re

curre_direct = os.getcwd()

user_file = os.path.join(curre_direct, "Convert_to_Numbers_input.xlsx")
df = pd.read_excel(user_file)

df['Source ID'] = df['Source ID'].astype(str).apply(lambda x: re.sub(r'[^0-9]', '', x))

df['Source ID'] = pd.to_numeric(df['Source ID'], errors='coerce')

df['Source ID 2'] = pd.to_numeric(df['Source ID 2'], errors='coerce')

df.to_excel('Output_Sheet.xlsx', index=False)