FROM selenium/standalone-chrome:latest

USER root

ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false

EXPOSE 8501

WORKDIR courtdata/

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
COPY init.sql .
COPY .env .

CMD ["streamlit", "run", "app/app.py"]
