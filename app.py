import pywikibot
from pywikibot import pagegenerators
import tweepy
from datetime import date

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
                print(end, " (END)")

                start = end - 120
                print(start, " (START)")

                print(end - start, "DIFF")
                for page in pagegenerators.RecentChangesPageGenerator(end, start):

                    if str(page.title).find(":") == -1:

                        try:
                            if (page.exists() == True):

                                print(page.title(), "AVANT TEST")
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
                                irev = int(rev)

                                print(start, " start")
                                print(irev, " irev")

                                if irev >= start and len(rev) == 14:
                                    print(page.title(), "APRES TEST")
                                    MESSAGE = "[[ " + page.title() + " ]] https://fr.wiktionary.org/wiki/" + page.title()
                                    api.update_status(MESSAGE)

                        except ValueError:
                            print ("Oops!")

            str_mnt = siteWiktionnaire.getcurrenttimestamp()
            MAINTENANT = int(str_mnt) - 120

            if MAINTENANT >= end:
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




