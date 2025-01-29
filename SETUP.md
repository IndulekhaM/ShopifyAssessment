
# Setup Instructions for Shopify Store Automation & Testing

## Step 1: Create a Shopify Store

1. **Create a Shopify Partner Account**:  
   Go to [Shopify Partners](https://www.shopify.com/partners) and create a free account if you don’t have one.

2. **Create a New Store**:  
   After logging into your partner account, create a new Shopify store. This will be the environment where you will test and set up the Pumper app.

## Step 2: Install the Pumper App

1. **Visit the Shopify App Store**:  
   Go to the [Shopify App Store](https://apps.shopify.com/) and search for the **Pumper** app.

2. **Install the Pumper App**:  
   Click on the Pumper app and install it on your store.

## Step 3: Set Up Pumper Offers

1. **Set Up Offers in Pumper**:  
   After the app is installed, configure the offers as required by the task. Ensure that the offers are visible on your store.

2. **Test the Setup**:  
   Check if the offers appear correctly and are functional by browsing your store.

## Step 4: Share Store URL

- After the setup is complete, share the **URL of your Shopify store** showcasing the Pumper offers.

---

## Step 5: Install Dependencies for Automation Scripts

1. **Install Python**:  
   Ensure you have **Python 3.7+** installed. Check by running:
   ```sh
   python --version
   ```

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

---
