from prac_07.project import Project
import datetime

MENU = "Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update project\nQ - Quit"
FILENAME = 'projects.txt'


def main():
    """ Main function to manage the project management software. """
    print("Custom-built project management software - Created by Your Name")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_new_project_menu(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects)  # Save updated projects back to the 'projects.txt' file
    print(f"{len(projects)} projects saved\nThank you for using custom-built project management software :)")


def load_projects():
    """Prompt the user for a filename to load projects from and load them"""
    projects = []
    with open(FILENAME, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header line
        for line in lines:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1].strip(), "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    print("Projects:")
    print("Incomplete projects:")
    count=0
    projects.sort()
    for project in projects:
        if project.is_complete()==False:
            print(f"  {project}")
        elif count==0:
            print("Completed projects: ")
            print(f"  {project}")
        else:
            print(f"  {project}")

def update_project(projects):
    """Choose a project, then modify the completion % and/or priority - leave blank to retain existing values"""
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    new_completion_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion_percentage:
        project.completion_percentage = int(new_completion_percentage)
    if new_priority:
        project.priority = int(new_priority)
    print("Project updated.")

def add_new_project_menu(projects):
    """Ask the user for the inputs and add a new project to memory"""


def filter_projects(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date"""



def save_projects(projects):
    """Prompt the user for a filename to save projects to and save them"""

main()
