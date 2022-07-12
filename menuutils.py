from typing import List

class MenuUtils(object):

    @staticmethod
    def menu_choice(prompt: str, choices: List[str]) -> int:
        """
        Display menu and return user's choice
        :param prompt: Prompt
        :param choice: List of choices
        :return: Correct choice
        """

        # Display menu
        num_of_choices = len(choices)
        print(prompt)
        for idx in range(num_of_choices):
            print(idx + 1, ".", choices[idx])

        return MenuUtils.choose_menu_item(num_of_choices)

    @staticmethod
    def choose_menu_item(num_of_choices):
        # Print number of car model
        print ("Please choose from 1 to", num_of_choices)

        # Select proper choice
        choice = 1
        done = False
        while not done:
            try:
                choice = int(input("Your choice -> "))
                if 1 <= choice <= num_of_choices:
                    done = True
                else:
                    print("ERROR: Please choose from 1 to", num_of_choices)

            except ValueError:
                print("ERROR: Please choose from 1 to", num_of_choices)
        return choice

    @staticmethod
    def menu_choice_nolist(prompt: str, num_of_choices: int) -> int:
        """
        Display prompt and return choice
        :param prompt: Prompt
        :param num_of_choices: Max num of choice
        :return: Proper choice
        """
        # Display menu
        print(prompt)
        return MenuUtils.choose_menu_item(num_of_choices)