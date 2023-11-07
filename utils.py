def get_col_types(df):
    out = dict(
        float_cols  = df.select_dtypes('float').columns,
        int_cols  = df.select_dtypes('int').columns,
        bool_cols  = df.select_dtypes('bool').columns,
        object_cols = df.select_dtypes('object').columns,
        str_cols = df.select_dtypes('string').columns,
        datetime_cols = df.select_dtypes('datetime').columns,
    )
    return out