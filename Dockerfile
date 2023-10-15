FROM python:3.10.0-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update \
    && apt-get install g++ -y \
    && apt-get install gcc -y \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get clean

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY . app/
EXPOSE 8501

WORKDIR /app

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]