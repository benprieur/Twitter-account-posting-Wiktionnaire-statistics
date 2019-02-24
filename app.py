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
            nbedit = 0
            nbeditPrincipal = 0
            nbcreation = 0

            if elapse == True:

                str_end = siteWiktionnaire.getcurrenttimestamp()
                end = int(str_end)
                print(end)

                start = end - 600
                print(start)

                for page in pagegenerators.RecentChangesPageGenerator(end, start):
                    print(page.title)

                    ''' nombre edits '''
                    nbedit = nbedit + 1

                    ''' main '''
                    if str(page.title).find(":") == -1:
                        nbeditPrincipal = nbeditPrincipal + 1

                        ''' Créations '''
                        try:
                            if (page.exists() == True):
                                timestamprev = page.oldest_revision.timestamp
                                rev = str(timestamprev.year)
                                if int(page.editTime().month) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.month)
                                if int(page.editTime().day) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.day)
                                if int(page.editTime().hour) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.hour)
                                if int(page.editTime().minute) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.minute)
                                if int(page.editTime().second) < 10:
                                    rev = rev + "0"
                                rev = rev + str(timestamprev.second)

                                print (str(rev))
                                print(str(start))
                                if int(rev) > start:
                                    print("*** CREATION ***")
                                    nbcreation = nbcreation + 1
                        except ValueError:
                            print ("Oops!")

                MESSAGE = "Au cours des 10 dernières minutes : " + str(nbedit) + " edit(s) sur le #Wiktionnaire"
                MESSAGE = MESSAGE + ", dont " + str(nbeditPrincipal) + " edit(s) d'entrées"
                '''MESSAGE = MESSAGE + ", dont " + str(nbcreation) + " création(s) d'entrées"'''
                MESSAGE = MESSAGE + ", https://fr.wiktionary.org/wiki/Sp%C3%A9cial:Modifications_r%C3%A9centes"
                print(MESSAGE)
                api.update_status(MESSAGE)

            str_mnt = siteWiktionnaire.getcurrenttimestamp()
            mnt = int(str_mnt) - 600
            print(mnt)

            if mnt > end:
                elapse = True
            else:
                elapse = False
        except ValueError:
            print("Oops!")

consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX-XXX'
access_token_secret = 'XXX'

if __name__ == '__main__':
    GetWiktionaryData()




