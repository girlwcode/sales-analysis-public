import pandas as pd
import numpy as np

# shipping state 합치기
def concat_shipping_state(df):
    result = []
    for i in df.index:
        if pd.isnull(df.loc[i, 'Shipping State']) and pd.isnull(df.loc[i, 'Shipping State-']):
            result.append(np.nan)
        elif pd.notnull(df.loc[i, 'Shipping State']):
            result.append(df.loc[i, 'Shipping State'])
        elif pd.notnull(df.loc[i, 'Shipping State-']):
            result.append(df.loc[i, 'Shipping State-'])

    df['Shipping_State'] = result
    new_df = df.drop(['Shipping State', 'Shipping State-'], axis=1)
    return(new_df)


# billing state 합치기
def concat_billing_state(df):
    result = []
    for i in df.index:
        if pd.isnull(df.loc[i, 'Billing State']) and pd.isnull(df.loc[i, 'Billing State-']):
            result.append(np.nan)
        elif pd.notnull(df.loc[i, 'Billing State']) and pd.notnull(df.loc[i, 'Billing State-']):
            result.append(df.loc[i, 'Billing State'])
        elif pd.notnull(df.loc[i, 'Billing State']):
            result.append(df.loc[i, 'Billing State'])
        elif pd.notnull(df.loc[i, 'Billing State-']):
            result.append(df.loc[i, 'Billing State-'])

    df['Billing_State'] = result
    new_df = df.drop(['Billing State', 'Billing State-'], axis=1)
    return (new_df)

