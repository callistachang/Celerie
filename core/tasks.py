from celery import shared_task


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task
def sample_task():
    print("The sample task just ran.")
