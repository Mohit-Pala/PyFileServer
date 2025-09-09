import pandas as pd


SAVE_FILE = 'files/database.csv'


def load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv(SAVE_FILE)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {SAVE_FILE} not found.")
    return df

@staticmethod
def get_all_data() -> pd.DataFrame:
    df = load_data()
    return df

@staticmethod
def get_data_By_id(id: int) -> pd.DataFrame:
    df = load_data()
    record = df[df['Id'] == id]
    if record.empty:
        raise ValueError(f"No record found with id {id}.")
    return record

@staticmethod
def get_all_data_by_Uploader(uploader: str) -> pd.DataFrame:
    df = load_data()
    records = df[df['UploadedBy'] == uploader]
    if records.empty:
        raise ValueError(f"No records found for uploader {uploader}.")
    return records

@staticmethod
def put_data(name: str, description: str, filepath: str, uploaded_by: str, status: str) -> None:
    df = load_data()
    new_id = df['Id'].max() + 1 if not df.empty else 1
    new_record = {
        'Id': new_id,
        'Name': name,
        'Description': description,
        'FilePath': filepath,
        'UploadedBy': uploaded_by,
        'Status': status
    }
    df = df.append(new_record, ignore_index=True)
    df.to_csv(SAVE_FILE, index=False)

@staticmethod
def delete_data_by_id(id: int) -> None:
    df = load_data()
    if id not in df['Id'].values:
        raise ValueError(f"No record found with id {id}.")
    df = df[df['Id'] != id]
    df.to_csv(SAVE_FILE, index=False)