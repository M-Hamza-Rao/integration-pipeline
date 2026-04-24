import pandas as pd

def is_valid_email(email: str) -> bool:
    return isinstance(email, str) and "@" in email and "." in email

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print(f"Initial rows: {len(df)}")

    # Drop missing emails
    df = df.dropna(subset=["email"])

    # Removing invalid emails
    df = df[df["email"].apply(is_valid_email)]

    # Converting age to number
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Drop invalid ages
    df = df.dropna(subset=["age"])

    # Cleaning names
    df["name"] = df["name"].str.strip()

    print(f"Cleaned rows: {len(df)}")

    return df