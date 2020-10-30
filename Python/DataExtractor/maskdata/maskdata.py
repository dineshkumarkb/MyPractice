# -*- encoding: utf-8 -*-

# Generic imports
import pandas as pd
import logging
from sqlalchemy import create_engine
import hashlib
import os
import argparse
import subprocess



# Setting the log level
logging.basicConfig(level=logging.DEBUG)
Dlog = logging.getLogger("maskdata")

# GLOBAL Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = "patients.db"
MODEL = "en_core_web_sm"
MODIFY_FLAG =True


# Connect to a sqlite DB
ENGINE = create_engine("sqlite:///{}".format(os.path.join(BASE_DIR,DB_NAME)))

# Check for spacy installation and import
try:
    import spacy
    # import scispacy
except ImportError as e:
    # if e.name == "scispacy":
    #     Dlog.error(" scispacy module is not installed.Please install scispacy module and retry. ")
    #     raise (ImportError," scispacy module is not available.")
    if e.name == "spacy":
        Dlog.error(" spacy module is not installed.Please install spacy module and retry. ")
        raise (ImportError, " spacy module is not available.")


def read_file(file_path, col_names):
    """
     A function to read the file.Only CSV files are supported for now
    :param file_path: Absolute path of the csv file
    :param col_names: A list of column names to be masked
    :return:None
    """
    if os.path.isdir(file_path):
        Dlog.info(" The file path is a directory.Reading csv files from directory ")
        csv_list = os.listdir(file_path)
    else:
        Dlog.info(" The file path is a csv file ")

    for files in csv_list:
        csv_file = files
        # Check the file type
        Dlog.info(" Checking the file type ")
        if csv_file.split(".")[1].lower() == "csv":
            Dlog.info(" File type is csv.Proceeding with file {}".format(os.path.join(file_path,csv_file)))
        else:
            raise (TypeError, "File format is not supported")
            Dlog.error(" File format not supported.Please upload a csv file ")

        Dlog.info(" Reading csv file {} ".format(csv_file))
        orig_csv = pd.read_csv(os.path.join(file_path,csv_file))

        Dlog.debug(" Calling rm_punc_spac ")
        Dlog.debug(" Found columns {} ".format(list(orig_csv.columns.values)))
        for col in col_names:
            Dlog.debug(" Data preprocessing for column {}".format(col))
            rm_punc_spac(orig_csv, col)

        Dlog.debug(" Calling extract_entities ")
        extract_entities(file_name=orig_csv, col_name=col_names)


def rm_punc_spac(file_name, col_name):
    """
    A function to remove punctuations and
    :param file_name: CSV file path
    :param col_name: col names to be masked
    :return: None
    """
    import string

    csv_file = file_name

    try:
        Dlog.info(" Preprocessing started.Reading column {} ".format(col_name))
        # Split the string and join them to remove unwanted spaces between names
        csv_file[col_name] = csv_file[col_name].str.split()
        csv_file[col_name] = csv_file[col_name].str.join("")

        # Remove all punctuations in a name and rejoin the string
        csv_file[col_name] = csv_file[col_name].map(
            lambda x: [char for char in str(x) if char not in string.punctuation])
        csv_file[col_name] = csv_file[col_name].str.join("")
        Dlog.info(" Preprocessing ended for column {} ".format(col_name))

    except (AttributeError,KeyError):
        Dlog.debug(" Column values empty/column not found ")


def extract_entities(file_name,col_name):

    """
    extract entities from the csv based on the model and store in a list for
    comparison
    :param file_name: csv file path
    :param col_name : column name
    :return:None
    """

    # Load a model
    try:
        Dlog.debug(" Loading model {}".format(MODEL))
        nlp = spacy.load(MODEL)

    except Exception as e:
        Dlog.info(" Error while loading model {}".format(MODEL))
        Dlog.info("{} model not found.Installing...".format(MODEL))
        code = subprocess.call(r'python -m spacy download en')
        if code == 0:
            Dlog.info(" {} model installation successful ".format(MODEL))
            nlp = spacy.load("en_core_web_sm")
            Dlog.info(" {} model loaded ".format(MODEL))

    doc_ent = []

    # Convert to string for nlp
    doc_txt = nlp(file_name.to_string())

    for X in doc_txt:
        # Check if a token is alphanumeric and add entities only if they are
        # proper noun/common noun/common noun plural.Ignore Cardinals(Numbers).
        if X.is_alpha and (str(X.tag_) != 'CD') and (str(X.tag_ == "NN") or
                                                     str(X.tag_ == "NNP")or
                                                     str(X.tag_ == "NNS")or
                                                     str(X.pos_) != "SPACE"):
            doc_ent.append(X)
    from functools import partial
    for col in col_name:
        try:
            Dlog.info(" Anonymizing column {} ".format(col))
            # Required to pass multiple args to apply function
            doc_list = partial(anonymize_data, doc_ent=doc_ent)
            file_name[col] = file_name[col].apply(doc_list)
        except KeyError:
            Dlog.info(" {} column is empty.Skipping.".format(col))

    Dlog.info(" Anonymization complete ")
    Dlog.info(" Creating anonymized csv ")
    try:
        print(" making dir @ ", dest_path+r'\test')
        os.mkdir(dest_path + r'\test')
    except FileExistsError:
        pass
    file_name.to_csv(dest_path + r'\test\Staffmember_modified.csv',index=False)
    Dlog.info(" Anonymization successful...CSV file copied to {} ".format(os.path.dirname(os.path.abspath(str(file_name)))))


def anonymize_data(col_data,doc_ent):
    """
    A preprocessing step to detect proper nouns/names
    and replace them with a pseudo data
    :param col_data: Each data in the column to be anonymized
    :param doc_ent: A list of entities with nouns excluding cardinals
    :return: anonymized data
    """
    if str(col_data) in str(doc_ent):
        hash_value = hashlib.sha3_512(col_data.encode()).hexdigest()
        df_db = pd.DataFrame({"Name":[str(col_data)],"Hashvalue":[hash_value]})
        df_db.to_sql('patients',con=ENGINE,if_exists="append",index=False)
        return hash_value

    return col_data


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Anonymization Tool")
    parser.add_argument("sp", type=str,help="csv file input path or directories with csv files")
    parser.add_argument("dp",type=str,help="csv destination path")
    parser.add_argument("--column",nargs="*",help="column names to be anonymized",
                         default=["abbreviation","mapcode","mapname","personid"])
    args = parser.parse_args()
    csv_path = args.sp
    dest_path = args.dp
    col_list = args.column
    read_file(csv_path,col_list)




