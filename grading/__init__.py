from celery import Celery

app = Celery('grading', broker='pyamqp://guest@localhost//')

app.conf.update(
    result_backend='rpc://',
)

app.autodiscover_tasks(['grading'])
