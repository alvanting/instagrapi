from instagrapi import Client
import time
import random

cl = Client()
cl.login(username=input("Please enter your username: "), password=input("Please enter your password: "))


class LikePost:
    def __init__(self, client):
        self.cl = client
        self.tags = ['婚禮', '婚紗']
        self.liked_medias = []
        self.elapsed_time = 0

    def get_post_id(self):
        try:
            medias = cl.hashtag_medias_recent(random.choice(self.tags))
            media_dict = medias[0].dict()
            return str(media_dict['id'])
        except KeyboardInterrupt:
            print("Program has been manually interrupted")
            exit()

    def wait_time(self, delay):
        try:
            time.sleep(delay)
        except KeyboardInterrupt:
            print("Program has been manually interrupted")
            exit()

    def like_post(self, amount):
        for i in range(amount):
            random_post = self.get_post_id()
            if random_post in self.liked_medias:
                pass
            else:
                self.cl.media_like(media_id=random_post)
                self.liked_medias.append(random_post)
                random_delay = random.randint(1, 5)
                self.elapsed_time += random_delay
                print(f"Liked {len(self.liked_medias)} posts, time elapsed {self.elapsed_time / 60} minutes. "
                      f"Now waiting for {random_delay} seconds.")
                self.wait_time(random_delay)


start = LikePost(cl)
start.like_post(600)


# username = input("请输入目标用户的用户名: ")
# user_id = client.user_id_from_username(username)
#
# medias = client.user_medias(user_id, amount=1)

# medias = client.hashtag_medias_recent('婚禮', amount=10)
#
# for media in medias:
#     print(media.dict())
#     client.media_like(media.id)
#     time.sleep(10)