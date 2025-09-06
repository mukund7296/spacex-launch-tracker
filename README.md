# SpaceX Launch Tracker 

A simple Python project to fetch and analyze SpaceX launch data. Get launch statistics, filter launches and visualize them in a clear, human-readable format.

---

## Features

* Fetch live SpaceX launch data
* Filter launches by rocket, site or date
* Calculate success rates
* Show monthly launch frequencies
* Pretty print results using tables

---

## Requirements

* Python 3.10 or higher
* pip (Python package manager)
* Virtual environment recommended

---

## Step-by-Step Guide

### 1. Clone the Project

```bash
git clone https://github.com/mukund7296/spacex-launch-tracker.git
cd spacex-launch-tracker
```

### 2. Set Up a Virtual Environment

It's a good practice to isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
# OR
venv\Scripts\activate      # On Windows
```

<img width="652" height="156" alt="image" src="https://github.com/user-attachments/assets/1bdf3a8d-7cd7-42fa-917f-513d395f1194" />


### 3. Install Dependencies

All required Python packages are listed in `pyproject.toml`:

```bash
pip install -e .
pip install tabulate
```

> `-e .` installs your package in editable mode, so changes you make are applied immediately.
> `tabulate` is used for pretty tables in output.

### 4. Run the Project

#### Show Launch Statistics

```bash
python main.py --stats
```

You will see:

* Successful Falcon 1 launches
* Success rate by rocket
* Launches by site
* Monthly launch frequency

#### List All Launches

```bash
python main.py --list
```

This prints all SpaceX launches retrieved from the API.

---
Ouptput : 
<img width="687" height="890" alt="image" src="https://github.com/user-attachments/assets/44235ca0-74f7-457b-9305-8bb4b83e3c57" />


### 5. Run Tests

Ensure everything works correctly with pytest:

```bash
pytest tests/
```

You should see something like:

```
6 passed in 0.70s
```

---
Output : 
<img width="1440" height="422" alt="image" src="https://github.com/user-attachments/assets/cf159b1b-e2f5-45fe-98ea-d930860e14fa" />


### 6. Filter Launches (Optional)

You can modify `main.py` to filter launches by date, rocket, or success status. For example:

```python
from spacex_tracker.launches import filter_launches

filtered = filter_launches(launches, rocket_id="5e9d0d95eda69955f709d1eb", success=True)
```

---

### 7. Troubleshooting

* If you see `ModuleNotFoundError`, make sure your virtual environment is activated.
* If `tabulate` is missing, install it with:

```bash
pip install tabulate
```

* If tests fail, ensure your system timezone matches the project expectations or adjust `datetime` handling.

---

