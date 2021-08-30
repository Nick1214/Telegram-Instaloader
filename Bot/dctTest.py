import instaloader


def get_info(username):
    insta = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(insta.context, username)

    Fullname = profile.full_name
    Get_followers = profile.followers
    GetFollowings = profile.followees
    Biography = profile.biography
    AccountClosed = profile.is_private
    print(f"Полное имя: {Fullname}")
    print(f"Количество подписчиокв: {Get_followers}")
    print(f"Количество подписок: {GetFollowings}")
    if Biography is None:
        print("Доп информация отстуствует")
    else:
        print(f"Доп Информация: {Biography}")
    if AccountClosed is False:
        print("Аккаунт не закрыт")
    else:
        print("Аккаунт закрыт...")
    posts = profile.get_posts()
    count = 0
    dct = {}

    for post in posts:
        count += 1
        post_username = post.profile
        post_date = post.date
        post_likes = post.likes
        post_url = post.url
        post_comments = post.comments
        # print(f"Username: {post_username}, Date: {post_date}, Likes: {post_likes}, URL: {post_url}")
        dct = {
            "post_date": post_date,
            "post_likes": post_likes,
            "post_url": post_url,
            "The number of post": count,
        }
        for key, value in dct.items():
            print(f"{key} -> {value}")


def download_profile(username):
    insta = instaloader.Instaloader()
    insta.download_profile(username, profile_pic_only=True)


download_profile("")
