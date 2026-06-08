import pytest
from survey import AnonymousSurvey as AnSu

@pytest.fixture
def language_survey():
    """survey that will be available to all functions"""
    question = "What language did you first learn to speak"
    language_survey = AnSu(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single question is store properly"""
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    """Test that a single question is store properly"""
    responses = ["English", "Italian", "Twi"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses