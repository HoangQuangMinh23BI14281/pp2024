import curses
from domains.school import School

def main(stdscr):
    # Initialize school and load data if exists
    school = School()
    school.load_data()
    
    # Main loop
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "1. Them hoc sinh")
        stdscr.addstr(1, 0, "2. Them mon hoc")
        stdscr.addstr(2, 0, "3. Xem diem hoc sinh")
        stdscr.addstr(3, 0, "4. Xep diem hoc sinh theo GPA")
        stdscr.addstr(4, 0, "5. Xem thong tin hoc sinh")
        stdscr.addstr(5, 0, "6. Xem thong tin mon hoc")
        stdscr.addstr(6, 0, "7. Thoat")
        stdscr.addstr(7, 0, "Your choice: ")
        stdscr.refresh()

        choice = stdscr.getch()

        if choice == ord('1'):
            school.input_students(stdscr)
        elif choice == ord('2'):
            school.input_courses(stdscr)
        elif choice == ord('3'):
            school.display_marks(stdscr)
        elif choice == ord('4'):
            school.sort_GPA(stdscr)
        elif choice == ord('5'):
            school.display_students(stdscr)
        elif choice == ord('6'):
            school.display_courses(stdscr)
        elif choice == ord('7'):
            school.save_data()
            break

if __name__ == "__main__":
    curses.wrapper(main)
