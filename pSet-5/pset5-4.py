def decrypt_story():
    story_string = CiphertextMessage(get_story_string())
    return story_string.decrypt_message()
