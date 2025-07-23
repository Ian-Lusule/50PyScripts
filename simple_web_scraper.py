```python
# python-mini-projects/simple_web_scraper.py

"""
A simple web scraper that extracts specific information from a website.

This script demonstrates basic web scraping using the `requests` and `BeautifulSoup` libraries.  
It's crucial to respect the website's `robots.txt` and terms of service before scraping.  
This example is for educational purposes only.  Inappropriate use can lead to legal issues.
"""

import requests
from bs4 import BeautifulSoup
import logging

# Configure logging for better error handling
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_website(url, target_element, target_attribute=None):
    """
    Scrapes a website for specific information.

    Args:
        url: The URL of the website to scrape.
        target_element: The HTML tag to search for (e.g., "h1", "p", "a").
        target_attribute: (Optional) The attribute of the target element to extract (e.g., "href", "src", "text"). 
                           If None, the text content of the element is extracted.

    Returns:
        A list of extracted information, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")
        elements = soup.find_all(target_element)

        extracted_data = []
        for element in elements:
            if target_attribute:
                data = element.get(target_attribute)
                if data:
                    extracted_data.append(data)
            else:
                extracted_data.append(element.text.strip())

        return extracted_data

    except requests.exceptions.RequestException as e:
        logging.error(f"Error during request: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage:  Scrape titles from a website (replace with your target website and elements)
    url = "https://www.example.com"  # Replace with the actual URL you want to scrape
    titles = scrape_website(url, "h1") # Extract all h1 tags

    if titles:
        print("Extracted Titles:")
        for title in titles:
            print(title)
    else:
        print("Scraping failed.")


    #Example usage: Scrape links from a website
    links = scrape_website(url, "a", "href") #Extract all href attributes from <a> tags
    if links:
        print("\nExtracted Links:")
        for link in links:
            print(link)
    else:
        print("Scraping failed.")

```


To use this code:

1. **Install required libraries:**
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Replace placeholders:** Change  `"https://www.example.com"`, `"h1"`, and `"a"` with the actual URL, target element, and attribute you want to scrape from your chosen website.  Make sure the website allows scraping.

3. **Run the script:**
   ```bash
   python simple_web_scraper.py
   ```

Remember to always check a website's `robots.txt` file (e.g., `https://www.example.com/robots.txt`) before scraping to ensure you're not violating any rules.  Excessive scraping can overload a website's server, so be mindful of the frequency of your requests.  Always handle potential errors gracefully, as shown in the example's error handling.
