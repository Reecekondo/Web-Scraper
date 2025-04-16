**VacancyMail Job Scraper**

Ever wondered if robots could steal your job? Well, *this one helps you find one instead!*
This Python-powered web scraper hunts job listings like a caffeine-fueled recruiter, pulling data from VacancyMail and stuffing it neatly into a CSV file.
And the best part? It works every day at 9 AM so you don’t have to. 💼

**FEATURES**
- Scrapes real job listings (not those suspicious "work-from-home millionaire" scams)
- Extracts job title, company, location, and expiry date—because nobody wants expired jobs
- Saves results in scraped_jobs.csv 
- Logs errors in scraper.log (so you know when things go horribly wrong)
- Runs automatically every day at 9 AM while you sleep like a responsible adult

**Setup Instructions**

1. Install Required Dependencies

Before running the script, summon Python's package management powers:
pip install requests beautifulsoup4 pandas schedule

2. Run the script 

python web_scraper.py

If all goes well, you'll see "Data saved successfully!". If not, check scraper.log, yell at the screen, and troubleshoot like a pro.

**Usage Guide**

Manual Execution

Need instant results? Run:

python web_scraper.py


Your CSV file will appear—unless it doesn’t. In that case, check the error log.

Scheduled Execution
The script runs itself every day at 9 AM. No intervention required!
Want it to run every hour instead? Modify this line:
schedule.every().day.at("09:00").do(scrape_jobs)


Change it to:
schedule.every().hour.do(scrape_jobs)


Boom. Hourly scraping.

Stopping the Scheduler

Just press Ctrl + C

**Error Handling & Logging**

Things will go wrong. That’s life. Fortunately, all errors get logged in scraper.log so you can pinpoint the problem (or blame the universe).

Common failures & solutions:

| Error Type | Cause | Solution | 
| Request failed | Website is down or blocking requests | Pretend you’re a human by adding headers={"User-Agent": "Mozilla/5.0"} | 
| No job listings found | Website changed its structure | Inspect the HTML with print(soup.prettify()) | 
| Unexpected error | Python hates you | Debug using traceback.format_exc() | 



**Future Enhancements**

1. Email alerts for failed scrapes (because not checking logs is a mood).
2. Extract salary details (so you know which job pays more than "exposure").
3. Store job listings in a database for easy querying.

**Final Thoughts**

This script works hard so you don’t have to. It’s basically your personal assistant, minus the awkward small talk.








