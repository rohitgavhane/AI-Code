def expert_system(symptoms, symptom1):
    diagnosis = ""
    treatment = ""
    hospitals = ""

    if symptoms == "fever" and symptom1 == "cough":
        diagnosis = "Migraine"
        treatment = "Ibuprofen"
        hospitals = "Recommended Hospitals:\n 1. Life Care \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash"
    elif symptoms == "cough" and symptom1 == "headache":
        diagnosis = "Flu"
        treatment = "Acetaminophen"
        hospitals = "Recommended Hospitals:\n 1. Life Care \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash"
    elif symptoms == "chest_pain" and symptom1 == "fever":
        diagnosis = "Pneumonia"
        treatment = "Antibiotics and rest"
        hospitals = "Recommended Hospitals:\n 1. Ashoka \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. wokart  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash"
    elif symptoms == "shortness_of_breath" and symptom1 == "cough":
        diagnosis = "Asthma"
        treatment = "Bronchodilators and inhaled corticosteroids"
        hospitals = "Recommended Hospitals:\n 1. Six sigma \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. magna  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash"
    elif symptoms == "frequent_urination" and symptom1 == "fatigue":
        diagnosis = "Diabetes"
        treatment = "Insulin therapy and blood sugar monitoring"
        hospitals = "Recommended Hospitals:\n 1. cooper \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. leelavati Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash"

    return diagnosis, treatment, hospitals

def main():
    symptoms = input("Enter the symptoms: ")
    symptom1 = input("Enter the symptom: ")

    diagnosis, treatment, hospitals = expert_system(symptoms, symptom1)

    print("Diagnosis:", diagnosis)
    print("Treatment:", treatment)
    print(hospitals)

if __name__ == "__main__":
    main()
