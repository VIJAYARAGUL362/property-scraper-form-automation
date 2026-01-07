# Property Listing Scraper & Form Automation Bot

A Python automation tool that scrapes property listings from a Zillow clone website and automatically submits the data (address, price, and link) to a Google Form using Selenium and BeautifulSoup.

**Part of Day 53 - 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu**

## 🎯 Project Overview

This capstone project demonstrates web scraping and browser automation skills by combining BeautifulSoup for data extraction and Selenium for automated form submission. The bot scrapes rental property data and populates a Google Form, which can then be exported to a spreadsheet for analysis.

## 🎓 Learning Objectives

This project covers:
- Web scraping with BeautifulSoup4
- Browser automation with Selenium WebDriver
- CSS selector usage for element targeting
- Data cleaning and processing
- Environment variable management
- Chrome WebDriver configuration
- Automated form filling and submission

## ✨ Features

- **Web Scraping**: Extracts property details (addresses, prices, links) from a Zillow clone website
- **Data Cleaning**: Removes unnecessary characters and formats prices consistently
- **Form Automation**: Automatically fills and submits Google Forms with scraped data
- **Persistent Browser Session**: Maintains Chrome profile for consistent behavior
- **Error Prevention**: Includes timing delays to ensure proper page loading

## 🛠️ Technologies Used

- **Python 3.x**
- **BeautifulSoup4**: HTML parsing and web scraping
- **Selenium**: Browser automation for form submission
- **Requests**: HTTP requests to fetch webpage content
- **python-dotenv**: Environment variable management
- **ChromeDriver**: WebDriver for Chrome browser automation

## 📋 Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Internet connection
- A Google Form with three short answer fields (Address, Price, Link)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/zillow-scraper-form-bot.git
   cd zillow-scraper-form-bot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver**
   - Visit [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/)
   - Download the version matching your Chrome browser
   - Extract and note the path

5. **Set up your Google Form**
   - Create a new Google Form
   - Add three short answer questions:
     1. What's the address of the property?
     2. What's the price per month?
     3. What's the link to the property?
   - Get the form URL

6. **Configure environment variables**
   - Create a `.env` file in the project root:
   ```env
   GOOGLE_FORM_URL=your_google_form_url_here
   ZILLOW_CLONE_URL=https://appbrewery.github.io/Zillow-Clone/
   ```

7. **Update ChromeDriver path**
   - Open `main.py`
   - Update `CHROME_DRIVER_PATH` with your ChromeDriver location

## 📖 Usage

Run the script:
```bash
python main.py
```

**What happens:**
1. Script fetches the Zillow clone website
2. BeautifulSoup parses the HTML and extracts property data
3. Data is cleaned and formatted
4. Chrome browser opens automatically
5. For each property:
   - Opens the Google Form
   - Fills in address, price, and link
   - Clicks submit
   - Waits and repeats for next property
6. All data is now in your Google Form responses (exportable to Sheets)

## 📂 Project Structure

```
zillow-scraper-form-bot/
│
├── main.py                 # Main script with scraping and automation logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Files to ignore in git
├── README.md              # Project documentation
└── chrome_profile/        # Chrome user data (auto-created)
```

## 🔍 How It Works

### 1. Web Scraping Phase
```python
# Fetch webpage with requests
response = requests.get(WEBSITE_URL)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data using CSS selectors
links = soup.select("a[data-test='property-card-link']")
addresses = soup.select("address[data-test='property-card-addr']")
prices = soup.select("span[data-test='property-card-price']")
```

### 2. Data Cleaning Phase
- Removes `/mo` suffix from prices
- Strips `$` prefix from prices
- Normalizes whitespace in addresses
- Extracts href attributes from links

### 3. Form Automation Phase
```python
# Create bot instance
bot = FormFillerBot()

# Loop through all properties
for address, price, link in zip(addresses, prices, links):
    bot.get_form()
    bot.fill_details(address, price, link)
    bot.press_submit()
```

## 🎨 Customization

### Different Website
To scrape a different property website, update the CSS selectors in `main.py`:
```python
links_soup = soup.select("your-link-selector")
address_soup = soup.select("your-address-selector")
prices_soup = soup.select("your-price-selector")
```

### Different Form Structure
If your Google Form has different field order, modify the `fill_details` method in the `FormFillerBot` class.

## ⚠️ Important Notes

- **Google Form Structure**: Form must have exactly 3 short answer fields in order (Address, Price, Link)
- **Class Names**: Script uses Google Forms' standard class names (`whsOnd` for inputs, `uArJ5e` for submit)
- **Rate Limiting**: 1-second delays prevent overwhelming the form
- **Browser Profile**: Chrome profile directory maintains session state
- **Ethical Scraping**: Always respect robots.txt and terms of service

## 🐛 Troubleshooting

**ChromeDriver Issues:**
- Ensure ChromeDriver version matches Chrome browser version
- Update `CHROME_DRIVER_PATH` to correct location

**Element Not Found:**
- Google Forms may have updated their HTML structure
- Inspect form elements and update class names if needed

**Form Not Submitting:**
- Check internet connection
- Verify Google Form URL is correct
- Ensure form is set to accept responses

## 🔮 Possible Enhancements

- [ ] Add error handling with try-except blocks
- [ ] Implement headless browser mode
- [ ] Export data to CSV before form submission
- [ ] Add command-line arguments for flexibility
- [ ] Support multiple property websites
- [ ] Add logging for debugging
- [ ] Implement data validation
- [ ] Create a GUI interface

## 📚 Resources

- [100 Days of Code - Python Bootcamp](https://www.udemy.com/course/100-days-of-code/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.php)

## 👤 Author

**Vijayaragul.s**
- 100 Days of Code - Day 53 Capstone Project
- Course by Dr. Angela Yu

## 🙏 Acknowledgments

- Dr. Angela Yu for the excellent Python bootcamp
- [App Brewery](https://www.appbrewery.co/) for providing the Zillow clone website
- The Python community for amazing libraries

## 📝 License

This project is open source and available under the MIT License.

---

**Day 53/100** - Web Scraping & Browser Automation Capstone 🎯

*Part of my journey through 100 Days of Code! Follow along as I build projects and master Python.*

⭐ If this helped you with your own Day 53 project, please star the repo!
