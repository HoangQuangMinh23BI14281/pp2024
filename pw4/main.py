import curses
from domains.school import School
from input import get_input
from output import show_menu

def main(stdscr):
    school = School()
    while True:
        show_menu(stdscr)

        choice = stdscr.getch()

        if choice == ord('1'):
            school.input_students(stdscr, get_input)
        elif choice == ord('2'):
            school.input_courses(stdscr, get_input)
        elif choice == ord('3'):
            school.display_marks(stdscr, get_input)
        elif choice == ord('4'):
            school.sort_GPA(stdscr)
        elif choice == ord('5'):
            school.display_students(stdscr)
        elif choice == ord('6'):
            school.display_courses(stdscr)
        elif choice == ord('7'):
            break
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
