from discogs_pypi import __version__
from discogs_pypi import discogs_module

# Test function to determine if app creation was successful
def test_create_app():
    try:
        discogs_module.create_app(username = discogs_env.discogs_user(), password = discogs_env.discogs_pw())
    except:
        print("App creation failed")
        
# Test function to determine if app creation was successful
def test_create_app():
    try:
        discogs_module.create_app(username = discogs_env.discogs_user(), password = discogs_env.discogs_pw())
    except:
        print("App creation failed")

# Test function to determine if credentials work on authenticated requests for data
def test_requests():
    try:
        username = discogs_env.discogs_user()
        password = discogs_env.discogs_pw()
        user_agent = "camilla/1.0"
        consumer_key = discogs_env.consumer_key
        consumer_secret = discogs_env.consumer_secret
        discogs_module.get_tokens(user_agent, consumer_key, consumer_secret)
    except:
        print("Getting tokens failed")
