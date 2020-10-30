import subprocess,os


def run_server():

    """
    Script to navigate to the app and execute
    python manage.py runserver command from
    command line
    :return:
    """

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    nav =  os.path.join(curr_dir,"reflekt_emp")
    subprocess.Popen("cd " + nav ,shell=True)
    os.chdir("reflekt_emp")
    subprocess.Popen("python manage.py runserver 8888",shell=True)



if __name__ == "__main__":

    run_server()