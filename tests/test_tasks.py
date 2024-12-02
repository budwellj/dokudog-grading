from grading.tasks import grade_work

def test_grade_work(mocker):
    work_title = 'Dune'

    mocker.patch('grading.tasks.call_chatgpt_api',return_value={'difficulty': 2.0})

    mocker.patch('grading.tasks.parse_response',return_value=2.0)

    difficulty = grade_work(work_title)

    assert isinstance(difficulty, float)

    assert 0 <= difficulty <= 10  # Assuming difficulty is a value between 0 and 10
    assert difficulty == 2.0 # Confirm that the expected value matches the input above (of 2.0)
