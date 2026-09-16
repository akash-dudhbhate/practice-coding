"""
Selenium + Brave Browser 151.1.93.134 + Selenium IDE extension v3.17.2

Usage:
    python3 brave_selenium.py

This script:
    1. Launches Brave with remote debugging enabled
    2. Connects ChromeDriver to the running instance
    3. Demonstrates basic navigation + screenshot
"""

import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- Paths ---
BRAVE_BINARY = os.path.expanduser("~/Downloads/brave-extracted/opt/brave.com/brave/brave")
BRAVE_WRAPPER = os.path.expanduser("~/Downloads/brave-extracted/opt/brave.com/brave/brave-browser")
CHROMEDRIVER_PATH = os.path.expanduser("~/Downloads/chromedriver/chromedriver-linux64/chromedriver")
EXTENSION_PATH = os.path.expanduser("~/Downloads/brave/selenium-ide-extension/3.17.2_0")
PROFILE_DIR = os.path.expanduser("~/.brave-profile")

# --- Environment ---
os.environ["CHROME_WRAPPER"] = BRAVE_WRAPPER
os.environ["CHROME_VERSION_EXTRA"] = "stable"
os.environ["GNOME_DISABLE_CRASH_DIALOG"] = "SET_BY_GOOGLE_CHROME"

# --- Launch Brave with remote debugging ---
print("Launching Brave Browser 151.1.93.134...")
brave_process = subprocess.Popen([
    BRAVE_BINARY,
    "--no-sandbox",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    f"--user-data-dir={PROFILE_DIR}",
    f"--load-extension={EXTENSION_PATH}",
    "--no-first-run",
    "--no-default-browser-check",
    "about:blank",
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Wait for DevTools to be ready
import urllib.request
import json as _json
for _ in range(30):
    try:
        resp = urllib.request.urlopen("http://localhost:9222/json/version", timeout=1)
        data = _json.loads(resp.read())
        print(f"Browser ready: {data['Browser']}")
        break
    except Exception:
        time.sleep(0.5)
else:
    print("Failed to start Brave")
    brave_process.kill()
    exit(1)

# --- Connect ChromeDriver ---
options = Options()
options.binary_location = BRAVE_BINARY
options.debugger_address = "127.0.0.1:9222"

service = Service(executable_path=CHROMEDRIVER_PATH)
print("Connecting ChromeDriver...")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")
    print(f"Page title: {driver.title}")
    print(f"Current URL: {driver.current_url}")
    print(f"Browser version: {driver.capabilities.get('browserVersion', 'unknown')}")
    print(f"ChromeDriver version: {driver.capabilities.get('chrome', {}).get('chromedriverVersion', 'unknown')}")

    driver.get("chrome://extensions/")
    time.sleep(1)
    print("\nExtension page loaded.")

    driver.save_screenshot("brave_selenium_test.png")
    print("\nScreenshot saved to brave_selenium_test.png")

    print("\nBrowser will stay open for 10 seconds...")
    time.sleep(10)

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
    brave_process.terminate()
    print("Browser closed.")
