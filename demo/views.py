from django.shortcuts import render
from django.http.response import JsonResponse
from demo.tasks import long_time_def


# Create your views here.
def index(req):
    return render(req, 'demo.html')


def run(req):
    task = long_time_def.apply_async()
    return JsonResponse({'task_id': task.id})


def task_status(req, task_id):
    # 获取celery之中 task_id的状态信息
    the_task = long_time_def.AsyncResult(task_id)  # 获取状态信息
    print("任务：{0} 当前的 state 为：{1}".format(task_id, the_task.state))
    if the_task.state == 'PROGRESS':
        resp = {'state': 'progress', 'progress': the_task.info.get('i', 0)}
    elif the_task.state == 'SUCCESS':
        resp = {'state': "success", 'progress': 100}
    elif the_task.state == 'PENDING':  # 任务处于排队之中
        resp = {'state': 'waitting', 'progress': 0}
    else:
        resp = {'state': the_task.state, 'progress': the_task.info.get('i', 0)}
    return JsonResponse(resp)
