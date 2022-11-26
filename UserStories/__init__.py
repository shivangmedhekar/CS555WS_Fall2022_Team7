import os

files = os.listdir("UserStories/")
user_story_files = [file for file in files if "us" in file]
user_story_files = [file_name.replace(".py", "") for file_name in user_story_files]

__all__ = user_story_files