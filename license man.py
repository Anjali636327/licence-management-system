# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:18:09 2024

@author: akhil
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Initialize cart
cart = {}

# Define LicenseApprovalSystem class
class LicenseApprovalSystem:
    def __init__(self):
        self.vehicle_codes = {}

    def add_vehicle(self, code):
        self.vehicle_codes[code] = False  

    def approve_license(self, code):
        if code in self.vehicle_codes:
            self.vehicle_codes[code] = True
            print(f"License approved for vehicle with code: {code}")
        else:
            print(f"Vehicle with code {code} not found in the system.")

    def check_approval_status(self, code):
        if code in self.vehicle_codes:
            if self.vehicle_codes[code]:
                print(f"License for vehicle with code {code} is approved.")
            else:
                print(f"License for vehicle with code {code} is not approved.")
        else:
            print(f"Vehicle with code {code} not found in the system.")

# Define LicenseManager class
class LicenseManager:
    def __init__(self):
        self.applications = []
        self.issued_licenses = []
        self.usage_data = {}

    def apply_for_medical_license(self, doctor_name, qualification):
        application = {'doctor_name': doctor_name, 'qualification': qualification, 'status': 'Pending'}
        self.applications.append(application)
        print(f"Application submitted successfully for Dr. {doctor_name}.")
        print(f"You have applied for a medical license with qualification: {qualification} - Cost: 5000")
        return 5000  # Return the cost of the medical license

    def review_applications(self):
        for application in self.applications:
            if application['status'] == 'Pending':
                print("Reviewing application for Dr. {}...".format(application['doctor_name']))
               
                if application['qualification'].lower() in ['mbbs', 'veterinary']:
                    application['status'] = 'Approved'
                    self.issued_licenses.append({'doctor_name': application['doctor_name'], 'license_number': len(self.issued_licenses) + 1})
                    print("Medical license approved for Dr. {}.".format(application['doctor_name']))
                else:
                    application['status'] = 'Rejected'
                    print("Medical license application rejected for Dr. {}. Invalid qualification.".format(application['doctor_name']))

    def get_issued_licenses(self):
        return self.issued_licenses

    def track_usage(self, license_id, usage_data):
        if license_id not in self.usage_data:
            self.usage_data[license_id] = []
        self.usage_data[license_id].append(usage_data)

    def send_renewal_alert(self, license_id):
        if license_id in self.usage_data and len(self.usage_data[license_id]) >= 5:
            print(f"Renewal alert sent for license ID {license_id}! Usage has reached the limit.")
        else:
            print(f"No renewal alert needed for license ID {license_id}.")

# Placeholder for GunLicenseApplication class
class GunLicenseApplication:
    def __init__(self, applicant_name, applicant_age, safety_training_completed):
        self.applicant_name = applicant_name
        self.applicant_age = applicant_age
        self.safety_training_completed = safety_training_completed

    def submit_application(self):
        # Check if the applicant is of legal age and has completed safety training
        if self.applicant_age >= 18 and self.safety_training_completed:
            print("Gun License application submitted successfully.")
            return True  # Application is valid
        else:
            if self.applicant_age < 18:
                print("Applicant is underage. Gun License application rejected.")
            if not self.safety_training_completed:
                print("Safety training not completed. Gun License application rejected.")
            return False  # Application is not valid

# Function for beautician license
def beauty_parlour_license():
    print("Welcome to the Beauty Parlour License Application!")

    # Display beautician degree courses and prices
    print("\nSelect your qualification:")
    qualifications = {
        "1": "Cosmetology - 2000",
        "2": "Esthetics - 1500",
        "3": "Hair Styling - 1800"
    }

    for key, value in qualifications.items():
        print(f"{key}. {value}")

    # Get user's qualification choice
    choice = input("Enter the number corresponding to your qualification choice: ")

    # Assign license based on the qualification choice
    if choice in qualifications:
        qualification = qualifications[choice].split(" - ")[0]
        price = int(qualifications[choice].split(" - ")[1])  # Extract price from string
    else:
        print("Invalid choice. Please enter a valid number.")
        return

    # Display license information
    print(f"\nCongratulations! You have been granted a Beauty Parlour License in {qualification}.")
    print(f"Price: {price}")

    # Add beautician license to the cart
    cart['Beautician License'] = {'qualification': qualification, 'price': price}

# Main license management function
def print_license():
    global cart  # To modify the global cart variable
    medical_license_manager = LicenseManager()
    
    while True:
        print("\n--- License Management Menu ---")
        print("1. Software License")
        print("2. Hardware License")
        print("3. Other License")
        print("4. Exit")
        try:
            ch = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == 1:
            def print_license_dashboard_Software():
                a = {
                    1: {'id': '1', 'item': 'C', 'price': 10000, 'Validation': 1, 'code': 'c'},
                    2: {'id': '2', 'item': 'Java', 'price': 25000, 'Validation': 1, 'code': 'Java'},
                    3: {'id': '3', 'item': 'Python', 'price': 30000, 'Validation': 1, 'code': 'Python'}
                }
                while True:
                    print("\nAvailable Software Licenses:")
                    print("{:<10}{:<15}{:<10}".format("SlNo", "Languages", "Price"))
                    
                    for key, value in a.items():
                        SlNo, Languages, price = key, value['item'], value['price']
                        print("{:<10}{:<15}{:<10}".format(SlNo, Languages, price))
                    
                    try:
                        c = int(input("Enter the SlNo of your Language choice (or 0 to go back): "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                        
                    if c == 0:
                        break
                    if 1 <= c <= 3:
                        item = a[c]['item']
                        price = a[c]['price']
                        validation = a[c]['Validation']
                        print(f"License chosen: {item} - Price: {price}, Validation: {validation}")
                        license_id = f"{item}_{len(medical_license_manager.issued_licenses) + 1}"
                        cart[item] = {'price': price, 'validation': validation, 'license_id': license_id}
                        
                        if item == 'C':
                            print('''
#include <string.h>

int isPalindrome(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;

    while (left < right) {
        if (str[left] != str[right]) {
            return 0; // Not a palindrome
        }
        left++;
        right--;
    }

    return 1; // Palindrome
}

int main() {
    char input[100];

    printf("Enter a string: ");
    scanf("%s", input);

    if (isPalindrome(input)) {
        printf("The string is a palindrome.\\n");
    } else {
        printf("The string is not a palindrome.\\n");
    }

    return 0;
}
''')
                        
                        elif item == 'Java':
                            print('''
public class BinarySearch {
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (array[mid] == target) {
                return mid; // Element found at index mid
            } else if (array[mid] < target) {
                left = mid + 1; // Discard left half
            } else {
                right = mid - 1; // Discard right half
            }
        }

        return -1; // Element not found
    }

    public static void main(String[] args) {
        int[] sortedArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int targetElement = 7;

        int result = binarySearch(sortedArray, targetElement);

        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}
''')
                        elif item == 'Python':
                            print('''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted list:", my_list)
''')
                        
                        break
                    else:
                        print("Invalid choice. Please choose a valid language or enter 0 to go back.")

            # Call the inner function if ch == 1
            print_license_dashboard_Software()
        
        elif ch == 2:
            print("\nHardware License Options:")
            print("1. Gun License")
            print("2. Vehicle License")

            try:
                hardware_choice = int(input("Enter your Hardware License choice (or 0 to go back): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if hardware_choice == 0:
                continue

            if hardware_choice == 1:
                print("Gun License selected. Price: 100000, Validation: 1")
                cart['Gun License'] = {'price': 100000, 'validation': 1}

                # Collect information for Gun License application
                applicant_name = input("Enter your name: ")
                try:
                    applicant_age = int(input("Enter your age: "))
                except ValueError:
                    print("Invalid age input. Please enter a number.")
                    del cart['Gun License']
                    continue
                safety_input = input("Have you completed safety training? (yes/no): ").lower()
                safety_training_completed = safety_input == "yes"

                gun_applicant = GunLicenseApplication(applicant_name, applicant_age, safety_training_completed)

                # Skip verification and billing if the applicant is underage or safety training is not completed
                if not gun_applicant.submit_application():
                    del cart['Gun License']  # Remove from cart if application failed
                    continue  # Go back to the main menu

            elif hardware_choice == 2:
                print("Vehicle License selected. Price: 10000, Validation: 2")

                # Integrate LicenseApprovalSystem for vehicle license
                license_system = LicenseApprovalSystem()

                # Add 3 vehicles
                for i in range(3):
                    code = input(f"Enter vehicle code {i+1}: ")
                    license_system.add_vehicle(code)

                # Display available vehicles
                print("Available vehicles:")
                for code in license_system.vehicle_codes:
                    print(code)

                # User selects a vehicle
                selected_code = input("Select a vehicle code: ")
                if selected_code in license_system.vehicle_codes:
                    print(f"Chosen vehicle code: {selected_code}")
                    license_system.approve_license(selected_code)
                    cart['Vehicle License'] = {'price': 10000, 'validation': 2, 'license_id': selected_code}
                else:
                    print(f"Vehicle with code {selected_code} not found in the system.")
                    continue  # Go back to the main menu if the selected vehicle code is not found

            else:
                print("Invalid choice. Please choose a valid hardware license option.")

        elif ch == 3:
            print("\nOther License Options:")
            print("1. Doctor License")
            print("2. Beautician License")

            try:
                other_choice = int(input("Enter your Other License choice (or 0 to go back): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if other_choice == 0:
                continue

            if other_choice == 1:
                doctor_name = input("Enter your name: ")

                print("Choose your qualification:")
                print("1. MBBS")
                print("2. Veterinary")
                qualification_choice = input("Enter the number corresponding to your qualification: ")

                if qualification_choice == "1":
                    qualification = "MBBS"
                elif qualification_choice == "2":
                    qualification = "Veterinary"
                else:
                    print("Invalid choice. Please choose a valid qualification.")
                    continue  # Go back to the main menu

                cost = medical_license_manager.apply_for_medical_license(doctor_name, qualification)
                medical_license_manager.review_applications()

                issued_medical_licenses = medical_license_manager.get_issued_licenses()

                if issued_medical_licenses:
                    print("\nIssued Medical Licenses:")
                    for license in issued_medical_licenses:
                        print("Doctor: {}, License Number: {}".format(license['doctor_name'], license['license_number']))
                    license_id = f"MedicalLicense_{len(medical_license_manager.issued_licenses)}"
                    cart['Doctor License'] = {'price': cost, 'qualification': qualification, 'license_id': license_id}
                else:
                    print("\nNo medical licenses have been issued.")

            elif other_choice == 2:
                beauty_parlour_license()

                # Check if Beautician License was added to the cart
                if 'Beautician License' not in cart:
                    print("No Beautician License purchased.")

            else:
                print("Invalid choice. Please choose a valid other license option.")

        elif ch == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        print("-----------------xxxxxxxxx-------------")

        # Function to handle billing
        def print_billing(total):
            global cart  # To modify the global cart
            if total > 0:  # Check if there are items in the cart for billing
                print("\n--- Billing ---")
                print(f"Total amount to be paid: {total}")
                try:
                    payment = int(input("Enter the payment amount: "))
                except ValueError:
                    print("Invalid payment input. Please enter a number.")
                    return
                if payment >= total:
                    change = payment - total
                    print(f"Payment successful! Your change: {change}")
                    # Clear the cart after successful payment
                    cart.clear()
                else:
                    print("Insufficient payment. Please pay the correct amount.")
            else:
                print("No items in the cart for billing.")

        # Function to handle verification
        def print_verification():
            global cart
            total = sum(item.get('price', 0) for item in cart.values())
            if total > 0:  # Check if there are items in the cart for verification
                print("\n--- Verification ---")
                print(f"Total amount to be billed: {total}")
                print("-----------------xxxxxxxxx-------------")
                return total
            else:
                print("No items in the cart for verification.")
                return 0

        verification_total = print_verification()
        print_billing(verification_total)

        # Track usage and send renewal alerts
        for item_key, item in list(cart.items()):  # Use list(cart.items()) to create a copy of the items
            if 'license_id' in item:
                license_id = item['license_id']
                usage_data = {'action': 'Usage data recorded'}
                medical_license_manager.track_usage(license_id, usage_data)
                medical_license_manager.send_renewal_alert(license_id)

    # Display existing licenses after all operations
    print("Displaying existing licenses...")
    for license_type, license_info in cart.items():
        print(f"{license_type}: {license_info}")

def delete_license(license_type):
    global cart  # To modify the global cart variable
    if license_type in cart:
        del cart[license_type]
        print(f"{license_type} has been deleted.")
    else:
        print(f"{license_type} not found in the cart.")

def print_license_management():
    global cart
    medical_license_manager = LicenseManager()  # Initialize LicenseManager here
    while True:
        print("\n--- License Management Dashboard ---")
        print("1. Create License")
        print("2. Display Licenses")
        print("3. Update License")
        print("4. Delete License")
        print("5. Exit")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Add new license creation logic here
            print("Creating a new license...")
            print_license()

        elif choice == 2:
            # Display existing licenses
            print("Displaying existing licenses...")
            if not cart:
                print("No licenses in the cart.")
            for license_type, license_info in cart.items():
                print(f"{license_type}: {license_info}")

        elif choice == 3:
            # Update existing license
            print("Updating a license...")
            print_license()

        elif choice == 4:
            # Delete existing license
            license_type_to_delete = input("Enter the type of license to delete: ")
            delete_license(license_type_to_delete)

        elif choice == 5:
            print("Exiting program.")
            print("-----------------Thank you------------------")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    # Display existing licenses after all operations
    print("Displaying existing licenses...")
    for license_type, license_info in cart.items():
        print(f"{license_type}: {license_info}")

if __name__ == "__main__":
    print("-------Welcome to License Management Dashboard-------")
    print_license_management()
