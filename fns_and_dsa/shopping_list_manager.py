# shopping_list_manager.py
def display_menu():
    print(f("Shopping List Manager"))
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Please choose an option (1-4): "))
        if choice == '1':
            item = input("Enter the item name to add: ").strip()
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == '2':
            item = input("Enter the item name to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"Error: {item} not found in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please choose a valid option (1-4).")
if __name__ == "__main__":
    main()
