# .

This directory contains a web-based application for interacting with CGMiner.

## Project Structure

### Files
- `kernel-ac2de4ac-4240-4d86-bcd8-e86d0e40dcfc.json`
- `kernel-15b86bfb-91a6-4039-a4c5-afab776d48cc.json`
- `kernel-863448b6-12e5-4fb6-b96c-64ed529b3260.json`
- `.bashrc`
- `.bash_logout`
- `.profile`
- `README`

### Directories
- `.ipython`
- `.local`
- `.openai_internal`
- `.cache`
- `.config`


## Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn app:app --reload
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000`.

## Features

- Sends commands to the CGMiner API.
- Parses JSON responses into a user-friendly UI.
- Bitcoin-themed web design with Bootstrap.

## Dependencies

- Python 3.x
- FastAPI
- Uvicorn
- Bootstrap (via CDN)
    