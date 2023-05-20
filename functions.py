def RunTask(task, taskName: str):
    exept = None
    print('Started task \'' + taskName + '\'')
    try:
        task()
    except Exception as e:
        exept = e
    finally:
        if exept == None:
            print('Completed task \'' + taskName + '\'')
        else:
            print('Completed task \'' + taskName + '\' with exception! ' + exept.__class__.__name__ + '\n' + str(exept))
            pass
        exept = None
