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

- Docker and Docker Compose installed on your system
- A `.env` file for environment variables

### `.env` File

The `.env` file is used to store sensitive information like database credentials. Create a `.env` file in the root directory of the project with the following content:

```env
MYSQL_DATABASE=courtdb
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_USER=user
MYSQL_PASSWORD=userpass
```

Ensure the `.env` file is not committed to version control by adding it to `.gitignore`.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ommudgal/Court-Case-Finder--Delhi-High-Court-
   cd Court-Case-Finder--Delhi-High-Court-
   ```

2. Create a `.env` file in the root directory as described above.

3. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

   - This will:
     - Start a MySQL database container with the schema initialized using [`init.sql`](init.sql ).
     - Start the Streamlit application container.

4. Access the application in your browser at `http://localhost:8501`.

## Project Structure

```
.
├── app/
│   ├── app.py                # Main Streamlit application
│   ├── web_functions.py      # Helper functions for web scraping
├── docker-compose.yaml       # Docker Compose configuration
├── Dockerfile                # Dockerfile for the Streamlit application
├── init.sql                  # SQL script to initialize the database
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not included in version control)
└── README.md                 # Project documentation
```

## Usage

1. Open the application in your browser at `http://localhost:8501`.

2. Use the form to search for case details by selecting the case type, entering the case number, and selecting the year.

3. The database is accessible via the MySQL container. Use the credentials from the [`.env`](.env ) file to connect.

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

## Stopping the Application

To stop the application and remove the containers, run:
```bash
docker-compose down
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web application framework.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Selenium](https://www.selenium.dev/) for web scraping.
- [MySQL](https://www.mysql.com/) for the database.
