from . import app

def grade_work(work):
    # Placeholder implementation
    # In reality, this would call the ChatGPT API
    # For now, return a fixed value for testing
    response = call_chatgpt_api(work)
    difficulty = parse_response(response)
    return difficulty

def call_chatgpt_api(book_title):
    # TODO 
    # Make an API call (to be mocked in tests)
    pass

def parse_response(response):
    # expect an iput that is in the form of {'difficulty': 2.0}
    # Parse the response and extract difficulty
    difficulty = response[1]
    return difficulty

@app.task
def grade_work_task(work_title):
    difficulty = grade_work(work_title)
    return difficulty