import pandas as pd
import gzip
import shutil
import pprint
from colorama import Fore, Style

# Initialize colorama
Fore.RESET

def unzip_file(input_file, output_file):
    try:
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"File '{input_file}' was successfully unzipped to '{output_file}'.")
        return True
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def import_raw_data():
    # todo exercise 1
    # Reading the CSV files
    df1_1 = pd.read_csv("./data/17-10-2018.3880.csv", delimiter=';', encoding='utf-8')
    df1_2 = pd.read_csv("./data/18-10-2018.3880.csv", delimiter=';', encoding='utf-8')
    df2 = pd.read_csv("./data/back_office.csv", delimiter=',', encoding='utf-8')

    # Remove leading and trailing whitespace characters from the 'categorieenseigne' columns
    df1_1['categorieenseigne'] = df1_1['categorieenseigne'].str.strip()
    df1_2['categorieenseigne'] = df1_2['categorieenseigne'].str.strip()

    # Checking if the 'categorieenseigne' columns contain the substring 'Promotions'
    mask1 = df1_1['categorieenseigne'].str.contains('Promotions')
    mask2 = df1_2['categorieenseigne'].str.contains('Promotions')

    # Replacing 'Promotions' with 'promo' where the condition is True
    df1_1.loc[mask1, 'categorieenseigne'] = df1_1.loc[mask1, 'categorieenseigne'].str.replace('Promotions', 'promo')
    df1_2.loc[mask2, 'categorieenseigne'] = df1_2.loc[mask2, 'categorieenseigne'].str.replace('Promotions', 'promo')

    # Printing the first 2 rows of each dataframe
    print(df1_1.head(5))
    print("\n")
    print(df1_2.head(5))
    print("\n")
    print(df2.head(5))

    # Convert the data type of 'identifiantproduit' in df1_1  and df1_2  to match the data type of 'pe_ref_in_enseigne' in df2
    print("\nConverting data types...")
    df1_1['identifiantproduit'] = df1_1['identifiantproduit'].astype(str)
    df1_2['identifiantproduit'] = df1_2['identifiantproduit'].astype(str)
    df2['pe_ref_in_enseigne'] = df2['pe_ref_in_enseigne'].astype(str)
    
    
    # Merging dataframes df1_1 and df1_2 with df2
    print("\nMerging dataframes...")
    df_merged_1 = pd.merge(df1_1, df2, left_on='identifiantproduit', right_on='pe_ref_in_enseigne')
    df_merged_2 = pd.merge(df1_2, df2, left_on='identifiantproduit', right_on='pe_ref_in_enseigne')
    
    return df_merged_1, df_merged_2



def average_prices():
    # todo exercise 2
    # Get the average price by Data Impact product
    avg_prices_df1 = df_merged_1.groupby('pe_id')['prixproduit'].mean()
    avg_prices_df2 = df_merged_2.groupby('pe_id')['prixproduit'].mean()

    # Convert the series to a dictionary 
    avg_prices_dict1 = avg_prices_df1.to_dict()
    avg_prices_dict2 = avg_prices_df2.to_dict()
    
    return {'df_merged_1': avg_prices_dict1, 'df_merged_2': avg_prices_dict2}


def list_unique_products_by_categories_by_df():
    # Get unique products by category for df_merged_1
    unique_products_df1 = df_merged_1.groupby('categorieenseigne')['identifiantproduit'].nunique()
    # Get unique products by category for df_merged_2
    unique_products_df2 = df_merged_2.groupby('categorieenseigne')['identifiantproduit'].nunique()
    
    # Convert the series to a dictionary 
    unique_products_dict1 = unique_products_df1.to_dict()
    unique_products_dict2 = unique_products_df2.to_dict()
    
    # Sort dictionaries by the count of unique products in descending order
    unique_products_dict1_sorted = dict(sorted(unique_products_dict1.items(), key=lambda item: item[1], reverse=True))
    unique_products_dict2_sorted = dict(sorted(unique_products_dict2.items(), key=lambda item: item[1], reverse=True))
    
    return {'df_merged_1': unique_products_dict1_sorted, 'df_merged_2': unique_products_dict2_sorted}


    

if __name__ == "__main__":
    print("Running main")
    print("Unzipping files...")
    unzip_file("./data/17-10-2018.3880.gz", "./data/17-10-2018.3880.csv")
    unzip_file("./data/18-10-2018.3880.gz", "./data/18-10-2018.3880.csv")
    unzip_file("./data/back_office.csv.gz", "./data/back_office.csv")
    print(Fore.GREEN + "\nFiles unzipped.")
    print(Style.RESET_ALL)

    print("Importing raw data...")
    df_merged_1, df_merged_2 = import_raw_data() 
    print(Fore.GREEN + "\nData imported.")
    print(Style.RESET_ALL)

    # Call the function and store the returned dictionaries in variables
    averages = average_prices()

    # Extract dictionaries from the returned dictionary
    avg_prices_df_merged_1 = averages['df_merged_1']
    avg_prices_df_merged_2 = averages['df_merged_2']
    
    print(Fore.YELLOW + "\nGet average prices per Data Impact product for df_merged_1 and df_merged_2:")
    print("- df_merged_1 : ", dict(list(avg_prices_df_merged_1.items())[:5]))
    print("- df_merged_2 : ", dict(list(avg_prices_df_merged_2.items())[:5]))

    print(Fore.BLUE +  "\nGet unique  Data Impact products per category for df_merged_1 and df_merged_2:")
   
    result = list_unique_products_by_categories_by_df()
    unique_products_by_categories_df_merged_1 = result['df_merged_1']
    unique_products_by_categories_df_merged_2 = result['df_merged_2']

    print(Fore.GREEN + "\nUnique Products Dictionary for df_merged_1:")
    pprint.pprint(dict(list(unique_products_by_categories_df_merged_1.items())[:5]))


    print(Fore.GREEN + "\nUnique Products Dictionary for df_merged_2:")
    pprint.pprint(dict(list(unique_products_by_categories_df_merged_2.items())[:5]))
