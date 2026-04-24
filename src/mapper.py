def map_row(row: dict) -> dict:
    return {
        "full_name": row.get("name"),
        "email_address": row.get("email"),
        "age": int(row.get("age")),
        "location": row.get("city")
    }