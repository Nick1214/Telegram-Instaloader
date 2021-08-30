
try:
    import MainDirectory.Parser_For_Open_Profile
    print(MainDirectory.Parser_For_Open_Profile.get_profile_information(username="neochiter22"))
except ImportError:
    print("Can't Import this module")