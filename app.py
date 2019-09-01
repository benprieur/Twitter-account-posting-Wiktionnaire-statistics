import pywikibot
from pywikibot import pagegenerators
import tweepy
import datetime
import time

def GetWiktionaryData():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print (api.me().name)
    siteWiktionnaire = pywikibot.Site('fr', u'wiktionary')
    elapse = True
    while True:
        try:
            if elapse == True:

                str_end = siteWiktionnaire.getcurrenttimestamp()
                end = int(str_end)
                print(end)

                start = end - 300
                print(start)

                for page in pagegenerators.RecentChangesPageGenerator(end, start):
                    print(page.title())

                    ''' main '''
                    if str(page.title()).find(":") == -1:

                        ''' Créations '''
                        try:
                            if (page.exists() == True):
                                timestamprev = page.oldest_revision.timestamp
                                rev = str(timestamprev.year)
                                if int(timestamprev.month) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.month)
                                if int(timestamprev.day) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.day)
                                if int(timestamprev.hour) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.hour)
                                if int(timestamprev.minute) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.minute)
                                if int(timestamprev.second) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.second)

                                print (str(rev))
                                print(str(start))
                                if int(rev) > start:
                                    titre = str(page.title())
                                    url = str(page.full_url())
                                    msg = "[[ " + titre + " ]] " + url + " "
                                    print(msg)
                                    api.update_status(msg)
                        except ValueError:
                            print ("Oops!")

            str_mnt = siteWiktionnaire.getcurrenttimestamp()
            mnt = int(str_mnt) - 300
            print(mnt)

            if mnt > end:
                elapse = True
            else:
                elapse = False
        except ValueError:
            print("Oops!")

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'

if __name__ == '__main__':
    GetWiktionaryData()
    
