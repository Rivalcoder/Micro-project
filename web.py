from datetime import datetime
import time
import random

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def __len__(self):
        return len(self.stack)


class Manager:
    def __init__(self):
        self.shipments = Stack()
        self.distributed_shipments = []

    def receive_shipment(self, name, quantity):
        entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(random.randint(0, 5))
        new_shipment = {"Name": name, "Quantity": quantity, "Date": entry_date}
        self.shipments.push(new_shipment)
        print(f"\nShipment received: {new_shipment}")

    def distribute_latest(self):
        shipment = self.shipments.pop()
        if shipment:
            self.distributed_shipments.append(shipment)
            print(f"Distributing shipment: {shipment}")
        else:
            print("No shipments left to distribute.")

    def latest_shipment_info(self):
        latest_shipment = self.shipments.peek()
        if latest_shipment:
            print(f"Most recent shipment ready for distribution: {latest_shipment}")
        else:
            print("No shipments in the stack.")

    def total_shipments(self):
        return len(self.shipments)

    def save_shipments_to_file(self):
        with open("details.txt", "w") as file:
            file.write("Stock Last Registered Shipment Details:\n\n")
            for i, shipment in enumerate(self.shipments.stack, start=1):
                file.write(f"\t{i}. {shipment}\n")
            file.write("\nDistributed Orders:\n\n")
            for i, shipment in enumerate(self.distributed_shipments, start=1):
                file.write(f"\t{i}. {shipment}\n")
        print("Shipment details saved to details.txt")

    def view_total_shipments(self):
        print(f"\nTotal shipments left: {self.total_shipments()}")


def main():
    manager = Manager()
    while True:
        print("\n--- Menu ---")
        print("1. Received New Shipment")
        print("2. Distribute Latest Shipment")
        print("3. View Latest Shipment(Last Entered)")
        print("4. Get Details of shipments and  distributed orders")
        print("5. View Total Shipments (NOW)")
        print("6. Exit \n")
        
        choice = input("Choose an option (1-6): ")
        print()
        
        if choice == '1':
            name = input("Enter the shipment name: ")
            quantity = int(input("Enter the quantity: "))
            manager.receive_shipment(name, quantity)
        
        elif choice == '2':
            manager.distribute_latest()
        
        elif choice == '3':
            manager.latest_shipment_info()
        
        elif choice == '4':
            manager.save_shipments_to_file()
        
        elif choice == '5':
            manager.view_total_shipments()
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid option, please choose a valid option.")


if __name__ == "__main__":
    main()
