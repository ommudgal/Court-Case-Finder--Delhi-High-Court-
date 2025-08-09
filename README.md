# Court Data Retrieval Application

This project is a web-based application designed to retrieve case details from the Delhi High Court website. It allows users to search for case information by providing the case type, number, and year.

## Features

- **Case Search**: Retrieve case details by selecting the case type, entering the case number, and selecting the year.
- **Case Details**: View case details in a tabular format.
- **Order & Documents**: Access links to related orders and documents.

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Database**: MySQL (via Docker)
- **Web Scraping**: Selenium, BeautifulSoup

## Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose
- A `.env` file for environment variables (if required)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ommudgal/Court-Case-Finder--Delhi-High-Court-
   cd Court-Case-Finder--Delhi-High-Court-
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up .env file

4. Set up the database:
   - Ensure Docker is installed and running.
   - Start the MySQL service using Docker Compose:
     ```bash
     docker-compose up -d
     ```

5. Initialize the database:
   - The `init.sql` file will automatically set up the database schema and initial data when the MySQL container starts.

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app/app.py
   ```

2. Open the application in your browser at `http://localhost:8501`.

3. Use the form to search for case details by selecting the case type, entering the case number, and selecting the year.

## Project Structure

```
.
├── app/
│   ├── app.py                # Main Streamlit application
│   ├── web_functions.py      # Helper functions for web scraping
├── docker-compose.yaml       # Docker Compose configuration
├── init.sql                  # SQL script to initialize the database
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Dependencies

The project uses the following Python libraries:

- `streamlit==1.32.0`
- `pandas==2.2.0`
- `selenium==4.18.1`
- `beautifulsoup4==4.12.3`
- `mysql-connector-python==8.3.0`
- `urlextract==1.9.0`
- `lxml==5.1.0`
- `python-dotenv==1.0.1`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web application framework.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Selenium](https://www.selenium.dev/) for web scraping.
- [MySQL](https://www.mysql.com/) for the database.
