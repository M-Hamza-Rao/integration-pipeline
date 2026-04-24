import pandas as pd
from cleaner import clean_data
from mapper import map_row
from api_client import send_with_retry
from logger import log_success, log_failure

def run_pipeline():
    df = pd.read_csv("data/raw_data.csv")

    clean_df = clean_data(df)

    for _, row in clean_df.iterrows():
        mapped = map_row(row)

        success = send_with_retry(mapped)

        email = mapped.get("email_address")

        if success:
            log_success(email)
            print(f"Sent: {email}")
        else:
            log_failure(email)
            print(f"Failed: {email}")

if __name__ == "__main__":
    run_pipeline()