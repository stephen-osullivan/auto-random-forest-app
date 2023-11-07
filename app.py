import streamlit as st
import pandas as pd
import numpy as np
from utils import get_col_types

st.title('Auto ML App')
df = pd.read_csv('data/titanic.csv')
columns = df.columns
n = len(df)

st.dataframe(df)

model_types = ['numeric', 'boolean', 'categorical', 'exclude']
model_type_map = dict(f = 'numeric', i='numeric', bool='boolean', O='categorical')


summary = df.dtypes.to_frame(); summary.columns = ['datatype']
summary['modelled_as'] = summary['datatype'].apply(lambda x: model_type_map.get(x.kind, 'exclude'))
summary['nulls'] = df.isnull().sum(axis=0)
summary['null %'] = round(summary['nulls']/n * 100,1)
summary['buckets'] = df.nunique()

st.dataframe(summary)

column_types = {}
for c in columns:
    column_types[c] = st.selectbox("Select Modelling Approach", tuple(model_types), index=2, key=c+'_type')