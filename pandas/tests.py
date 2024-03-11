# write your tests here

import pandas as pd
from src import average_prices, list_unique_products_by_categories_by_df


COLS = ['categorieenseigne', 'prixproduit', 'pe_ref_in_enseigne', 'ean', 'disponible', 'pe_id', 'p_id_cat']


def test_average_prices():
    
    df_merged_1 = pd.DataFrame([['cat_1', 6.8, None, None, None, 123, None], ['cat_2', 6.2, None, None, None, 123, None]], columns=COLS)
    df_merged_2 = pd.DataFrame([['cat_1', 8, None, None, None, 123, None], ['cat_2', 6.2, None, None, None, 124, None]], columns=COLS)
    
    res = average_prices(df_merged_1, df_merged_2)
        
    assert res[123] == 7
    assert res[124] == 6.2


def test_list_unique_products_by_categories_by_df():
    
    df_merged_1 = pd.DataFrame([['cat_1', 5.8, None, None, None, 123, None], ['cat_1', 6.2, None, None, None, 124, None],
                                ['cat_1', 6.2, None, None, None, 125, None]], columns=COLS)
    df_merged_2 = pd.DataFrame([['cat_1', 8, None, None, None, 123, None]], columns=COLS)

    res_1 = list_unique_products_by_categories_by_df(df_merged_1)
    res_2 = list_unique_products_by_categories_by_df(df_merged_2)

    result = list_unique_products_by_categories_by_df()
    res_1 = result['df_merged_1']
    res_2 = result['df_merged_2']

    assert 125 in res_1['cat_1']
    assert len(res_1['cat_1']) == 3
    assert 125 not in res_2['cat_1']
    assert len(res_2['cat_1']) == 1