from datetime import datetime

def RunTask(task, taskName = 'Unnamed Task', isSubTask = False):
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S]")

    exept = None
    print(current_time + ' Started task \'' + taskName + '\'')
    try:
        task()
    except Exception as e:
        exept = e
    finally:
        now = datetime.now()
        current_time = now.strftime("[%H:%M:%S]")
        
        if exept == None:
            if isSubTask:
                print(current_time + ' Completed sub task \'' + taskName + '\'')
            else:
                print(current_time + ' Completed task \'' + taskName + '\'')
        else:
            if isSubTask:
                print(current_time + ' Completed task \'' + taskName + '\' with exception! ' + exept.__class__.__name__ + '\n' + str(exept))
            else:
                print(current_time + ' Completed sub task \'' + taskName + '\' with exception! ' + exept.__class__.__name__ + '\n' + str(exept))
