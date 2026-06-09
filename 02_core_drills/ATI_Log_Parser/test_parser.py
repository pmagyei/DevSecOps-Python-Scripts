from ati_log_parser import CloudtrailAnalyzer
import pytest


def test_extract_ip_success():
    mock_log = "UNAUTHORIZED: Failed SSH attempt from 203.0.113.42"
    result = analyze(mock_log)

    assert result == "203.0.113.42"

