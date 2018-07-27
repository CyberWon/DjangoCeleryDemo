from celery import task
import time


@task(bind = True)
def long_time_def(self):
    i = 0
    while i < 100:
        i+= 1
        self.update_state(state='PROGRESS',meta={'i':i})
        # self.update_state(meta={'i':i})
        time.sleep(0.2)
    return 'finished'