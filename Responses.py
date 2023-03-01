
def sample_response(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi"):
        return "Hey, I'm Hong Dang's Chat bot!"
    return "I don't understand you!"