from django.apps import AppConfig


class CallsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'call'

    def ready(self):
        from .jobs import updater
        updater.start()

    # def ready(self):
    #     from redis import Redis
    #     from rq import Queue
    #     from rq_scheduler import Scheduler
    #     from datetime import datetime
    #     from .utils import parse_active_calls
    #
    #     # scheduler = Scheduler(connection=Redis())  # Get a scheduler for the "default" queue
    #     # scheduler = Scheduler('foo', connection=Redis())  # Get a scheduler for the "foo" queue
    #
    #     # You can also instantiate a Scheduler using an RQ Queue
    #     queue = Queue(connection=Redis())
    #     scheduler = Scheduler(queue=queue)
    #     scheduler.schedule(
    #         scheduled_time=datetime.utcnow(),  # Time for first execution, in UTC timezone
    #         func=parse_active_calls,  # Function to be queued
    #         # args=[arg1, arg2],  # Arguments passed into function when executed
    #         # kwargs={'foo': 'bar'},  # Keyword arguments passed into function when executed
    #         interval=60,  # Time before the function is called again, in seconds
    #         repeat=10,  # Repeat this number of times (None means repeat forever)
    #         # meta={'foo': 'bar'}  # Arbitrary pickleable data on the job itself
    #     )
    #
    #     # # Puts a job into the scheduler. The API is similar to RQ except that it
    #     # # takes a datetime object as first argument. So for example to schedule a
    #     # # job to run on Jan 1st 2020 we do:
    #     # scheduler.enqueue_at(datetime(2020, 1, 1), func)  # Date time should be in UTC
    #     #
    #     # # Here's another example scheduling a job to run at a specific date and time (in UTC),
    #     # # complete with args and kwargs.
    #     # scheduler.enqueue_at(datetime(2020, 1, 1, 3, 4), func, foo, bar=baz)
    #     #
    #     # # You can choose the queue type where jobs will be enqueued by passing the name of the type to the scheduler
    #     # # used to enqueue
    #     # scheduler = Scheduler('foo', queue_class="rq.Queue")
    #     # scheduler.enqueue_at(datetime(2020, 1, 1),
    #     #                      func)  # The job will be enqueued at the queue named "foo" using the queue type "rq.Queue"
