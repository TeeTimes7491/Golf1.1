from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import json

load_dotenv()

USERNAME = os.getenv("GOLF_USERNAME")
PASSWORD = os.getenv("GOLF_PASSWORD")

with open("config.json") as f:
    config = json.load(f)

DESIRED_DATE = config["date"]
DESIRED_COURSE = config["course"]
DESIRED_TIME = config["time"]
NUM_PLAYERS = config["players"]

def book_tee_time():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://fox.tenfore.golf/mcggolf")

        page.click("text=Login")
        page.fill("input[name='email']", USERNAME)
        page.fill("input[name='password']", PASSWORD)
        page.click("text=Sign In")
        page.wait_for_timeout(3000)

        page.goto("https://fox.tenfore.golf/mcggolf/reservation")

        page.click("input[placeholder='Choose a date']")
        page.fill("input[placeholder='Choose a date']", DESIRED_DATE)
        page.keyboard.press("Enter")

        page.click("div[role='button']:has-text('Select Course')")
        page.click(f"text={DESIRED_COURSE}")

        page.click("div[role='button']:has-text('Players')")
        page.click(f"text={NUM_PLAYERS}")

        page.click("text=Search Tee Times")
        page.wait_for_selector("text=Available Times")

        page.click(f"text={DESIRED_TIME}")
        page.click("text=Continue")
        page.click("text=Book Now")

        print(f"✅ Tee time booked for {DESIRED_TIME} on {DESIRED_DATE} at {DESIRED_COURSE}")
        page.wait_for_timeout(3000)
        browser.close()
