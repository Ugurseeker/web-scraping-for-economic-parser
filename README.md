Financial Data Scraper Bot
This project is a Python-based automated bot designed to scrape real-time financial data from various online sources at predetermined intervals throughout the day. The bot uses Selenium to interact with websites and extract data such as currency exchange rates (USD/TRY, EUR/TRY, etc.), precious metals prices (e.g., gold, silver), cryptocurrency values (e.g., BTC/USDT, ETH/USD), and key financial indices (e.g., BIST-100, NASDAQ-100). Additionally, it retrieves Turkey's 5-year Credit Default Swap (CDS) data.

Key Features:
Scheduled Data Collection: The bot operates during specified working hours, collecting data at four target times (09:00, 12:00, 15:00, and 18:00). It automatically pauses outside of these hours, ensuring data is collected efficiently.
Data Storage: Each time the bot retrieves new data, it stores the results in an Excel file (financial_data.xlsx). If the file already exists, the new data is appended to the existing dataset, creating a continuous record of financial information.
Error Handling: The bot includes error-handling mechanisms to manage any issues that may arise during the web scraping process, ensuring robustness and reliability.
Headless Operation: The bot runs in headless mode, meaning it operates without opening a visible browser window, making it ideal for deployment on servers or continuous operation environments.

Use Cases:
This bot is particularly useful for financial analysts, traders, or anyone needing up-to-date financial data for analysis or decision-making. By automating the data collection process, it saves time and reduces the risk of manual errors.

How It Works:
Initialize Chrome Driver: The bot uses a headless Chrome browser to access financial websites.
Set Target Times: The bot calculates daily target times for data collection.
Scrape Data: At each target time, the bot visits specified websites, extracts relevant data, and stores it in an Excel file.
Wait Between Intervals: Between data collection intervals, the bot remains idle, reducing unnecessary resource usage.
Daily Operation Cycle: The bot runs daily within the set working hours, pausing during non-working hours and resuming the next day.
This project demonstrates the integration of web scraping with real-time data analysis, making it a valuable tool for anyone who needs to monitor financial markets regularly.
