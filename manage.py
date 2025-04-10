import Project

def main():
    try:
        Project.project.run(port = 8000 ,debug = True)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()