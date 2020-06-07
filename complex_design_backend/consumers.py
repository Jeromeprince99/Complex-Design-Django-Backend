
import asyncio
import json
from channels.generic.websocket import WebsocketConsumer
import threading
import random
import time

#def send():
    

class wsconsumer(WebsocketConsumer):
    def websocket_connect(self,event):
        print("connected", event)
        self.accept()
        i = -1
        j=-1
        profile_name = [
            "Best bet",
            "Touch lap",
            "AI time",
            "Model lap",
            "Trending Apps",
            "Best Mobile",
            "Feature Phones",
            "Tablet World"
        ]
        content=[
            "Foldable phones brought new fashion in smart phone industry. Buyers showing more interest in these devices that fits their pockets",
            "Touch screen laptops are amazing. Art work and photoshop work became flexible after the arrival of these laptop. Although their price are high its worth buying them",
            "Halli Labs, a Bangaluru based AI firm was acquired by Google recently. This is the only company acquired by google based on India.",
            "The new 2019 model gets you an attractive, slim chassis, great performance and powerful speakers. New to the latest Envy are a fingerprint sensor and a webcam kill switch for those who value their privacy.  ",
            "Apps have started a revolution, in that they have completely changed the way we use our smartphones. Both Apple's App Store and the Google Play store have over one million apps available for download and purchase.",
            "The iPhone 7 is still the most popular smartphone, despite losing 0.97% share since the start of the year. Overall, the landscape remains rather static",
            "Buy Basic Mobile - List of all feature phones with updated prices from all top brands.Compare basic mobiles by prices and features and choose the best model ",
            "Galaxy Tab S6 seamlessly syncs your Galaxy Smartphone, so you never miss a call when it comes in. It also allows you to reply to urgent text messages, so you're never out of the loop.",
        ]
        data=["Hi, How are you?...",
        "I have scheduled you a...",
        "Nice to meet you...",
        "Urgent! Come in the main office",
        "Task assigned...",
        "Promotion applied...",
        "Amount credited...",
        "New challenges...",
        "Stay away from Corona...",
        "Wash your hands often..",
        "Task deadline reached...",
        "Welcome you onboard..."]
        imageurls=[
        "https://boygeniusreport.files.wordpress.com/2019/02/screen-shot-2019-02-11-at-12.11.04-pm.png",
        "https://cdn.pixabay.com/photo/2014/05/02/21/49/home-office-336373_1280.jpg",
        "https://www.un.org/sites/un2.un.org/files/styles/large-article-image-style-16-9/public/field/image/azoulay.jpg?itok=9kVglYrd",
        "https://assets.pcmag.com/media/images/677293-hp-elitebook-dragonfly-01.jpg?thumb=y&width=600&height=600",
        "https://img.etimg.com/thumb/width-640,height-480,imgsize-268807,resizemode-1,msid-70533809/why-mobile-apps-require-access-to-your-dataand-device-tools.jpg",
        "https://www.askifa.ng/wp-content/uploads/2020/02/iphonexr.jpg",
        "https://www.beeindia.in/wp-content/uploads/2019/01/Best-Keypad-Phone-In-India-800x385.jpg",
        "https://sm.pcmag.com/t/pcmag_in/photo/k/keyboard/keyboard_qfm1.1080.jpg"]
        while True:
            n = random.randint(1,24)
            i = i+1
            i = i%12
            j = j+1
            j = j%8
            notifData = {
                         "number":n,
                         "data":data[i]   
                        }   
            storyData = { 
                         "profile_name":profile_name[j],
                         "time":str(n)+' hrs',
                         "content":content[j],
                         "image":imageurls[j]
                        }
            self.send(json.dumps({
                'message': notifData,
                'story': storyData
            }))
            time.sleep(5)
       

    def websocket_receive(self, event):
        print("receive", event)

    def websocket_disconnect(self,event):
        print("disconnected",event)