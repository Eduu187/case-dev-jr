import os
import pytest

os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ["AWS_DEFAULT_REGION"] = "sa-east-1"
os.environ["TABLE_NAME"] = "LawyerTasks"

@pytest.fixture(autouse=True)
def aws_credentials():
    yield