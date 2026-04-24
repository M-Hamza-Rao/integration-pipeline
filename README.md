# Integration Pipeline Simulation

## Overview

This project simulates a real-world data integration pipeline where messy customer data is processed and sent to an external system.

The pipeline performs the following steps:

1. Load raw CSV data
2. Clean and validate the data
3. Transform it into a required schema
4. Send it to an external API
5. Log success and failure events

---

## Project Goal

The goal of this project is to demonstrate how customer data is onboarded into a system while handling:

* inconsistent and incomplete input data
* schema differences between systems
* unreliable external APIs
* logging and debugging requirements

---

## Architecture

```
CSV (raw data)
    ↓
Cleaner (validation and normalization)
    ↓
Mapper (schema transformation)
    ↓
API Client (data transmission)
    ↓
Retry Logic (failure handling)
    ↓
Logging (tracking and observability)
```

---

## Features

### Data Cleaning

* Removes rows with missing or invalid email addresses
* Converts and validates numeric fields such as age
* Normalizes string fields

### Data Mapping

* Transforms internal data structure into API-compatible format
* Example:

  * `name` → `full_name`
  * `email` → `email_address`

### API Integration

* Sends data to an external API (JSONPlaceholder)
* Handles request failures and response validation

### Retry Logic

* Retries failed API requests up to three times
* Simulates real-world API unreliability

### Logging

* Logs successful and failed operations
* Records retry attempts for traceability

---

## Tech Stack

* Python
* Pandas
* Requests

---

## How to Run

```bash
python src/main.py
```

Logs are written to:

```
logs/pipeline.log
```

---

## Example Data Issues Handled

* Missing email addresses
* Invalid email formats
* Non-numeric or missing age values

---

## AI Usage

AI tools were used to assist with debugging, designing data validation logic, improving code structure, and validating outputs during development.

---

## Key Learnings

* Handling and validating real-world data
* Designing data transformation pipelines
* Integrating with external APIs
* Implementing retry and logging mechanisms

---

## Interview Explanation

I built a small integration pipeline that takes messy CSV data, cleans and validates it, maps it to a required schema, and sends it to an API. It also includes retry logic and logging to handle failures. This simulates how customer data is onboarded into real systems where data quality and reliability are critical.

---
