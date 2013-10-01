from django.shortcuts import render
from datetime import datetime
from snapp.models import Snap
import time

def index(request):
    fmt = '%Y-%m-%d %H:%M:%S'
    now   = datetime.now()
    start = datetime.strptime('2013-10-01 12:00:00', fmt)
    end   = datetime.strptime('2013-10-07 12:00:00', fmt)

    now   = time.mktime(now.timetuple())
    start = time.mktime(start.timetuple())
    end   = time.mktime(end.timetuple())

    snaps = Snap.objects.order_by('-downloaded')

    return render(request, 'landingpage/index.html', {
        'progress': 100 * (1 - (end - now) / (end - start)),
        'snaps': snaps,
        })

