# AI Web Scraper

Effortless AI-Powered Web Scraping Tool

This project is an AI-powered web scraper that allows users to scrape content from any website and parse it using AI for further analysis. Built using **Streamlit**, the tool makes web scraping accessible and easy to use for non-technical users.

## Features

- **Web Scraping**: Enter a website URL, and using ** Scraper API** the application will scrape the content of the webpage.
- **Content Cleaning**: Once scraped, the content is cleaned up using **Beautiful Soup** 
- **View DOM Content**: The cleaned content is displayed in an expandable section, allowing you to review the raw data.
- **User Input**: Provide descriptions of the data you want to extract, and Ollama LLM is used to parse the content accordingly.
- **Streamlit Interface**: The tool is built with an intuitive and responsive web interface using Streamlit.

## How It Works

1. **Input URL**: Users input the URL of the website they want to scrape.
2. **Scrape the Website**: The tool uses an API key (e.g., ScraperAPI) to retrieve the content of the webpage.
3. **View Scraped DOM**: The scraped DOM content is cleaned and displayed.
4. **Describe Parsing Task**: Users provide a description of what they want to parse from the scraped data.
5. **AI-Powered Parsing**: The AI processes the content based on the user's description and returns the parsed results.

## Requirements

- Python 3.8+
- Selenium
- Streamlit
- ScraperAPI (or another scraping service)
- Beautiful Soup
- Ollama (or another AI parsing service)
