FROM python:3.10.0-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

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