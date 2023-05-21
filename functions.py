from datetime import datetime

def Log(message: str, level: str):
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S]")
    print(current_time + ' ' + level + ': ' + message)
    with open('mod-generator.log', 'a') as f:
        f.write(current_time + ' ' + level + ': ' + message + '\n')

def RunTask(task, taskName = 'Unnamed Task', isSubTask = False):
    exept = None
    Log('Started task \'' + taskName + '\'', 'INFO')
    try:
        task()
    except Exception as e:
        exept = e
    finally:
        if exept == None:
            if isSubTask:
                Log('Completed sub task \'' + taskName + '\'', 'INFO')
            else:
                Log('Completed task \'' + taskName + '\'', 'INFO')
        else:
            if isSubTask:
                Log('Completed task \'' + taskName + '\' with exception! ' + exept.__class__.__name__ + '\n' + str(exept), 'ERROR')
            else:
                Log('Completed sub task \'' + taskName + '\' with exception! ' + exept.__class__.__name__ + '\n' + str(exept), 'ERROR')
