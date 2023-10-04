
from fastapi import FastAPI, UploadFile, Response, status

import pandas as pd
from io import BytesIO


app = FastAPI()

#
@app.get("/health/")
def read_health():
    return {"OK"}


@app.post(
    "/stats/",
    description="""
Send a CSV-File and calculate mean and sum of the give column

column - name of the column for the calculation

sep - separator for the CSV

csv_file - CSV-File for calculation

""",
)
def upload(column: str, sep: str, csv_file: UploadFile, resp: Response):

    # load the csv into IO Buffer
    try:
        contents = csv_file.file.read()
        buffer = BytesIO(contents)
    except TypeError as e:
        resp.status_code = status.HTTP_400_BAD_REQUEST
        return("Error while reading file: " + str(e))

    # this column must exist in the csv, values are grouped by this column
    idx = "Zeitindex"

    try:
        # encoding="cp1252" is windows encoding, this is the encoding of the system the file was send from
        data = pd.read_csv(buffer, sep=sep, encoding="cp1252")

        # calculation part

        # 'O' is for Object, the type if column is a string and needs to be converted
        if data[column].dtype == 'O':
            # clean column from € sign
            data[column] = data[column].str.replace('€', '')
            # convert column to float
            data[column] = data[column].astype(float)

        # calculate sum and mean values
        sums = data[[column, idx]].groupby(idx).sum()
        means = data[[column, idx]].groupby(idx).mean()

    except ValueError as e:
        resp.status_code = status.HTTP_400_BAD_REQUEST
        return ("ValueError while processing csv file: " + str(e))
    except KeyError as e:
        resp.status_code = status.HTTP_400_BAD_REQUEST
        return ("KeyError while processing csv file: " + str(e))
    except TypeError as e:
        resp.status_code = status.HTTP_400_BAD_REQUEST
        return ("TypeError while processing csv file: " + str(e))

    buffer.close()
    csv_file.file.close()
    return ("Summen", sums.to_dict()), ("Durchschnitt", means.to_dict())
