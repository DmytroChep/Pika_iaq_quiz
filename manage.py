import Project

def main():
    try:
        Project.execute()  
        Project.DATABASE.create_all()
        Project.project.run(port = 8000 ,debug = True)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    # from Project.settings import socketio, project
    # socketio.run(project, host="0.0.0.0", port=8000)
    main()
    