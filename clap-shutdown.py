import slowclap as sc
import os

feed = sc.MicrophoneFeed()
detector = sc.AmplitudeDetector(feed, threshold=30000000)
i = 1
for clap in detector:
    # do something
    if i == 50:
        i = 1
        os.system("thunar")
    print(i, clap.time)
    #print("CLAP_BOT: Opening thunar File Explorer.")
    #os.system("thunar")
    i += 1
