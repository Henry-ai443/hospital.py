class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name:{self.name}, Age:{self.age}, Gender:{self.gender}, Disease:{self.disease}"
    
class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully!")

    def display_patients(self):
        if len(self.patients) == 0:
            print("No patients to display.")
        else:
            print("Patient list")
            for patient in self.patients:
                print(patient)

def main():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1.Add Patient")
        print("2.Vie Patient")
        print("3.Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            disease = input("Enter patient's disease: ")

            patient = Patient(patient_id, name, age, gender, disease)
            hospital.add_patient(patient)

        elif choice == '2':
            hospital.display_patients()

        elif choice == '3':
            print("Exiting the system")
            break
        else:
            print("Invalid choice, please Try again.")

main()