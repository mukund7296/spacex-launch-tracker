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
git clone <your-repo-url>
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

### 8. Contributing

Feel free to open issues or create pull requests.
Keep your changes clear and add tests for new features.

---

### 9. License

This project is open-source. Use it freely for learning or personal projects.

---

If you want, I can also **rewrite this README to be super friendly, like “a human teaching another human step by step”**, with emojis and really conversational instructions—it will feel like a mini tutorial.

Do you want me to do that version too?
