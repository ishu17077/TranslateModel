# TranslateModel

This repository contains the `TranslateModel` project. Follow the instructions below to set up the environment and run the model.

## Setup Instructions

1. **Create a virtual environment:**
   We recommend using `uv` to manage the environment. You can create the `.venv` folder by running:

   ```bash
   uv venv
   ```

   *(Alternatively, you can use `python -m venv .venv`)*

2. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   Sync and install the project dependencies using `uv`:

   ```bash
   uv sync
   ```

4. **Download Quantized Model from releases page**

5. **Run the model:**
   Once the environment is set up and activated, you can run the test script:
   
   ```bash
   python test_model.py
   ```
