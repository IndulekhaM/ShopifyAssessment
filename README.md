
# Shopify Store Automation & Testing

This repository contains the implementation of the Shopify store setup, automation scripts, and detailed reports. The task consists of three parts:

1. **Setup Store**: Creating a Shopify store, installing necessary apps, and setting up offers.
2. **Perform Comprehensive Testing**: Writing automation scripts to test specific functionalities.
3. **Prepare a Detailed Report**: Documenting the process and results of the tests.

## Task Overview

### 1. Setup Store
- Created a Shopify store via Shopify Partners (free).
- Installed the Pumper app from the Shopify app store.
- Set up Pumper offers on the store.
- Shared the URL showcasing the Pumper offers.

### 2. Perform Comprehensive Testing
- Automated tests for two functional events of the Pumper Bundle Quantity application.
- Used **Selenium** for web automation with the **Chrome** browser.
- Validated that the automated tests perform correctly and give expected results.

### 3. Prepare a Detailed Report
- Documented the testing process, setup, and results of the automated tests.

---

## Steps to Run the Automation Scripts

### Prerequisites
- **Python 3.7+** or higher installed
- **Chrome** browser installed

### Step 1: Install Dependencies

Run the following command to install the necessary Python dependencies:

```sh
pip install -r requirements.txt
```

### Step 2: Set Up the WebDriver

Make sure **ChromeDriver** is installed and accessible in your system’s PATH. If not, download the appropriate version of **ChromeDriver** from [here](https://chromedriver.chromium.org/downloads) and place it in a known directory.

### Step 3: Execute the Automation Scripts

Run the following command to start the tests:

```sh
pytest test_script.py
```

This will run the automated tests using **Selenium**.

### Test Results

If the tests are successful, the results will be displayed in the terminal. You can also use `pytest -v` for detailed logs or `pytest -s` to see the `print()` outputs.

---

## Troubleshooting

- **"NoSuchDriverException: Unable to obtain driver for chrome"**
  - Ensure that **Chrome** and **ChromeDriver** are installed correctly.
  - Update **Selenium** to the latest version:
    ```sh
    pip install --upgrade selenium
    ```

- **Test Failures**
  - Ensure that the Pumper app is correctly installed on the store and that the functional events are set up as expected.
  - Adjust the `WebDriverWait` in the scripts if the page elements are loading slowly.

---

2. **Set Up a Virtual Environment** (Optional):  
   To create an isolated environment, run the following command:
   ```sh
   python -m venv .venv
   ```

   Activate the virtual environment:
   - **Windows**:
     ```sh
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```sh
     source .venv/bin/activate
     ```

3. **Install Dependencies**:  
   Run the following command to install the necessary dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Step 6: Set Up ChromeDriver

1. **Install Chrome Browser**:  
   Ensure that **Chrome** is installed on your system.

2. **Install ChromeDriver**:  
   Download the appropriate version of **ChromeDriver** from [here](https://chromedriver.chromium.org/downloads) based on your installed Chrome version. 

3. **Add ChromeDriver to System Path**:  
   Place the **ChromeDriver** in a known directory and add it to your system’s PATH.

---

## Step 7: Run the Automation Tests

1. **Navigate to Your Project Directory**:  
   Go to the folder where your project files are located.

2. **Run the Tests**:  
   Execute the test script with the following command:
   ```sh
   pytest test_script.py
   ```

   This will run the automated tests for the Pumper app's functionality.

---

## Additional Notes

- **Selenium** will handle the browser automation, and it will automatically download the **ChromeDriver** if it's not present.
- The automation scripts are written using **Selenium** and will test the Pumper app's core functionality.
