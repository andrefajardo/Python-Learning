def actions(chosen_option):
    if chosen_option == 1:
        from . import list_people
        list_people.list_people()
    elif chosen_option == 2:
        from . import register_person
        register_person.register_person()
    elif chosen_option == 3:
        from . import exit_program
        exit_program.exit_program()