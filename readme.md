# Setting Up a Python Virtual Environment

### macOS/Linux/Windows

1. **Open Terminal**.
2. Navigate to your project directory.
3. Run the following command to create a virtual environment:
   ```bash
   python -m venv .venv
   ```

# Activating Virtual Environment

1. Navigate to your project directory.
2. Run the following command to activate a virtual environment:

For macOS & Linux
```
source env/bin/activate 
```
For Windows
```
.\env\Scripts\activate
```

# To install packages (if any)
```
pip install -r requirements.txt
```