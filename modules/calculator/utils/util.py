import logging
import traceback

import pandas as pd

logger = logging.getLogger(__name__)


def read_excel_file(data):
    """Read data from excel file.

    :param data:str, data in file
    :return:str, data after reading excel file
    """
    try:
        return pd.read_excel(data)
    except Exception as e:
        logger.info(f"Not able to read data. Error :- {e}")
        raise e


def create_excel_file(dataframe_dictionary, path):
    """
    Create a Pandas Excel writer using XlsxWriter as the engine. Convert the dataframe to an XlsxWriter Excel object.
    Close the Pandas Excel writer and output the Excel file.
    """
    df = pd.DataFrame(dataframe_dictionary)

    writer = pd.ExcelWriter(path, engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()


def check_input(item):
    """
    Check if the variable is string or not. Convert it to float if found as string. Raise exceptions for alphabets.
    """
    try:
        return float(item) if isinstance(item, str) else item
    except Exception:
        traceback.print_exc()
        logger.error('Exception encountered as input')
