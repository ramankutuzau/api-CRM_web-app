from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import parse_active_calls
from .exchange import parse_exchange_rates

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(parse_active_calls, 'interval', seconds=3)
    # scheduler.add_job(parse_exchange_rates, 'interval', seconds=60)
    scheduler.start()
