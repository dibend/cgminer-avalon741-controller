# cgminer_web_app

## Demo images:

<img src="https://njweb.solutions/img/Screen3.jpg" alt="demo screenshot">
<img src="https://njweb.solutions/img/Screen2.jpg" alt="demo screenshot">
<img src="https://njweb.solutions/img/Screen1.jpg" alt="demo screenshot">
This is a web-based interface for interacting with CGMiner. It allows you to send commands to CGMiner (`summary`, `pools`, `restart`) and view the parsed JSON responses in a user-friendly format.

## Project Structure

The following files and folders are part of this project:

- `cgminer_web_app.py`: The main FastAPI application file.
- `templates/`: Contains HTML templates for the web UI.
  - `index.html`: The main page where commands can be submitted.
  - `result.html`: Displays the parsed JSON output in a clean format.
    
## How to Use

### 1. Clone the Repository
First, clone the repository and navigate to the `cgminer_web_app` directory:
```bash
git clone https://github.com/dibend/cgminer-avalon741-controller.git
cd cgminer-avalon741-controller/cgminer_web_app
```

### 2. Install Dependencies
Ensure you have Python 3.8 or later installed. Install the required Python packages:
```bash
pip install fastapi uvicorn
```

### 3. Run the Application
Use **Uvicorn** to start the FastAPI application:
```bash
uvicorn cgminer_web_app:app --reload --host 0.0.0.0 --port 8000
```

### 4. Access the Web App
Open your browser and go to:
```
http://server-ip-or-hostname:8000
```

### 5. Interact with the CGMiner API
- Use the web interface to send the following commands:
  - **`summary`**: Displays mining performance statistics.
  - **`pools`**: Lists all configured mining pools.
  - **`restart`**: Restarts the CGMiner software.
- Results from the CGMiner API will be parsed and displayed in a user-friendly UI.

## Notes

- Make sure that CGMiner is running and accessible via the API before using this web app.
- Ensure that the configuration matches the expected API host and port in `cgminer_web_app.py`.
