# name=str(input("Enter a name : "))
# print(name.replace("t","m"))
import instaloader
L=instaloader.Instaloader()
profile=input("Enter the profile name : ")
L.download_stories(profile,download_stories_only=True)
L.download_profile(profile,profile_pic_only=True)
