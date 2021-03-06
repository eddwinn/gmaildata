__author__ = 'ed'

from IPython.display import Image

Image('http://i.imgur.com/SYija2N.png')


import mailbox


from email.utils import parsedate
from dateutil.parser import parse
import itertools


import plotly.plotly as py
from plotly.graph_objs import *

import plotly
plotly.tools.set_credentials_file(username='eddwinn', api_key='u0svj9kpb2', stream_ids=['fxrj4m028s', '63d4pvq8x3'])

# enter path to mbox file.  Download from google under your dashboard.
#  Go to Account/ then DashBard/ then download Gmail data.
#  Put the path to your .mbox data below


path = '/home/ed/Development/Python/gmaildata/All mail Including Spam and Trash.mbox'

# open the mailbox
mbox = mailbox.mbox(path)

def extract_date(email):
    date = email.get('Date')
    return parsedate(date)

sorted_mails = sorted(mbox, key=extract_date)
mbox.update(enumerate(sorted_mails))
mbox.flush()
# turn dates of emails into a list per day

all_dates = []
mbox = mailbox.mbox(path)
try:
    for message in mbox:
        all_dates.append( str( parse( message['date'] ) ).split(' ')[0] )

except Exception as e:
    print(str(e))
# Count mail per day

email_count = [(g[0], len(list(g[1]))) for g in itertools.groupby(all_dates)]
email_count[0]

#  Graph it

x = []
y = []
for date, count in email_count:
    y.append(date)
    x.append(count)
"""
data = Data([x, y])
plot_url = py.iplot(Data, filename='line-scatter' )

"""
py.iplot( Data([ Scatter( x=x, y=y ) ]) )