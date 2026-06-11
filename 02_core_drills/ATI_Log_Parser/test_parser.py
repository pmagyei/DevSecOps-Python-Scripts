from ati_log_parser import CloudtrailAnalyzer as CtAn
#import pytest

# CDD
# Test 1 will return the IP address
# assertion to match the IP address extracted

# Test 2 should return an empty list
# assertion will pass the test matching no ip address

# Test 3 should return an empty list
# ipv4 ranges from 0 to 255, assertion to follow the same rule

def test_parser():
    analyzer = CtAn("")
    mock_log = "UNAUTHORIZED: Failed SSH attempt from 203.0.113.42"
    extracted_ip = analyzer.extract_ip(mock_log)
    assert extracted_ip == ["203.0.113.42"]

def test_no_ip():
    analyzer = CtAn("")
    mock_log = "UNAUTHORIZED: Access denied due to bad credentials"
    extracted_ip = analyzer.extract_ip(mock_log)
    assert extracted_ip == []

def test_invalid_ip_range():
    analyzer = CtAn("")
    mock_log = "UNAUTHORIZED: Ping from 999.999.999.999"
    extracted_ip = analyzer.extract_ip(mock_log)
    assert extracted_ip == []
