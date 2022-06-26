#Used to calculate system status for the nodes
import socket



def evaluate_wifi():
    try:
        sock = socket.create_connection(("1.1.1.1",80))
        if sock is not None:
            #Connection occured, wifi is up
            sock.close()
            return True
    except OSError:
        pass
    return False


def evaluate_bluetooth():
    pass


def evaluate_audio():
    pass


def evaluate_camera():
    pass


def full_evaluation():
    '''Performs full diagnostics with the above functions and returns a dict with all info'''
    return {}




if __name__ == "__main__":
    print(evaluate_wifi())

