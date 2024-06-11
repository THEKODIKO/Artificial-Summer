from threading import Thread


def run_in_background(func, *args, **kwargs):

    Thread(target= func, args= args, kwargs= kwargs).start()
