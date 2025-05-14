{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs26 \cf0 def show_settings():\
    while True:\
        print("\\n--- Settings Menu ---")\
        print("1. Adjust Volume")\
        print("2. Change Difficulty")\
        print("3. Back to Main Menu")\
\
        choice = input("Select an option (1-3): ").strip()\
\
        if choice == "1":\
            print("Volume settings coming soon...")\
        elif choice == "2":\
            print("Difficulty settings coming soon...")\
        elif choice == "3":\
            break\
        else:\
            print("Invalid input. Please choose 1, 2, or 3.")\
\
def show_menu():\
    while True:\
        print("\\n--- Main Menu ---")\
        print("1. Start")\
        print("2. Settings")\
        print("3. Quit")\
\
        choice = input("Select an option (1-3): ").strip()\
\
        if choice == "1":\
            print("START")\
            # You could start your game logic here\
        elif choice == "2":\
            show_settings()  # Go to settings screen\
        elif choice == "3":\
            print("Exiting program...")\
            break\
        else:\
            print("Invalid input. Please choose 1, 2, or 3.")\
\
# Run the menu\
show_menu()\
}