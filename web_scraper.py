import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import logging
import traceback

# Configure logging
logging.basicConfig(
    filename="scraper.log",
    level=logging.DEBUG,  # Changed to DEBUG for detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# URL of the job listings page
URL = "https://vacancymail.co.zw/jobs/"

def scrape_jobs():
    logging.info("Starting job scraping process...")

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(URL, headers=headers, timeout=10)

        if response.status_code == 200:
            logging.info("Successfully fetched webpage.")
            soup = BeautifulSoup(response.text, "html.parser")
            job_listings = soup.find_all("div", class_="job-listing-details")

            if not job_listings:
                logging.warning("No job listings found on the page.")
                return

            jobs = []
            for job in job_listings:
                try:
                    title = job.find("h3", class_="job-listing-title").text.strip() if job.find("h3", class_="job-listing-title") else "N/A"
                    company = "N/A"

                    company_tag = job.find("i", class_="icon-material-outline-business")
                    if company_tag:
                        company_li = company_tag.find_parent("li")
                        company = company_li.text.strip() if company_li else "N/A"
                    else:
                        company_logo = job.find("div", class_="job-listing-company-logo")
                        if company_logo and company_logo.img:
                            company = company_logo.img.get("alt", "N/A").strip()

                    location = "N/A"
                    location_tag = job.find("i", class_="icon-material-outline-location-on")
                    if location_tag:
                        location_li = location_tag.find_parent("li")
                        location = location_li.text.strip() if location_li else "N/A"

                    expiry_date = "N/A"
                    expiry_tag = job.find("i", class_="icon-material-outline-access-time")
                    if expiry_tag:
                        expiry_li = expiry_tag.find_parent("li")
                        expiry_date = expiry_li.text.strip().replace("Expires: ", "") if expiry_li else "N/A"

                    jobs.append({
                        "Job Title": title,
                        "Company": company,
                        "Location": location,
                        "Expiry Date": expiry_date
                    })

                    logging.debug(f"Extracted job: {title} | {company} | {location} | {expiry_date}")

                except Exception as e:
                    logging.error(f"Error extracting job details: {e}\n{traceback.format_exc()}")

            df = pd.DataFrame(jobs)

            if not df.empty:
                df.to_csv("scraped_jobs.csv", index=False, encoding="utf-8")
                logging.info("Data successfully saved to scraped_jobs.csv.")
            else:
                logging.warning("No job listings found. CSV file not created.")

        else:
            logging.error(f"Failed to fetch webpage. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}\n{traceback.format_exc()}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}\n{traceback.format_exc()}")

# Schedule the scraper to run every day at 9 AM
schedule.every().day.at("09:00").do(scrape_jobs)

print("Scheduler started. Press Ctrl+C to stop.")
try:
    while True:
        schedule.run_pending()
        time.sleep(60)
except KeyboardInterrupt:
    print("Script stopped by user. Exiting gracefully...")
    logging.info("Scheduler stopped manually by the user.")