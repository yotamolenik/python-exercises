import pytest
import smtplib


@pytest.fixture(scope="function") # if scope is session or module then test_module will use a single connection for both tests
def smtp_connection():
    connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5) # fhfhv <-> smtp.gmail.com
    try:
        yield connection
    finally:
        smtplib.SMTP.close(connection)


