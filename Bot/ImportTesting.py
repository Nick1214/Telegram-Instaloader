
try:
    import MainDirectory.Parser_For_Open_Profile
    print(MainDirectory.Parser_For_Open_Profile.get_profile_information(username="any instagram username"))
except ImportError:
    print("Can't Import this module")
