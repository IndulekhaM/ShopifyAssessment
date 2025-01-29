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
Automated tests have been written for two key functionalities of the Pumper Bundle Quantity application:

- **`BundleOffer.py`**: Automates the testing of the bundle offer feature, validating that the bundle quantity logic works correctly within the app.
- **`QuantityBreaks.py`**: Automates the testing of the quantity breaks feature, ensuring that the discounts and offers apply correctly based on quantity selections.

Both tests use **Selenium** for web automation with the **Chrome** browser and validate that the automated tests perform correctly and give expected results.

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

To run the automated tests, execute the following commands:

- For testing the bundle offer functionality:
  ```sh
  pytest BundleOffer.py
  ```
- For testing the quantity breaks functionality:
  ```sh
  pytest QuantityBreaks.py
  ```

Both scripts will run the automated tests using **Selenium**. 

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
