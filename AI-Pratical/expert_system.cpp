#include <iostream>
#include <string>
using namespace std;

void expert_system(string symptoms, string symptom1, string& diagnosis, string& treatment, string& hospitals) {
    if (symptoms == "fever" && symptom1 == "cough") {
        diagnosis = "Migraine";
        treatment = "Ibuprofen";
        hospitals = "Recommended Hospitals:\n 1. Life Care \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash";
    }
    else if (symptoms == "cough" && symptom1 == "headache") {
        diagnosis = "Flu";
        treatment = "Acetaminophen";
        hospitals = "Recommended Hospitals:\n 1. Life Care \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash";
    }
    else if (symptoms == "chest_pain" && symptom1 == "fever") {
        diagnosis = "Pneumonia";
        treatment = "Antibiotics and rest";
        hospitals = "Recommended Hospitals:\n 1. Ashoka \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. wokart  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash";
    }
    else if (symptoms == "shortness_of_breadth" && symptom1 == "cough") {
        diagnosis = "Asthma";
        treatment = "Bronchodilators and inhaled corticosteroids";
        hospitals = "Recommended Hospitals:\n 1. Six sigma \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. magna  Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash";
    }
    else if (symptoms == "frequent_urination" && symptom1 == "fatigue") {
        diagnosis = "Diabetes";
        treatment = "Insulin therapy and blood sugar monitoring";
        hospitals = "Recommended Hospitals:\n 1. cooper \n Facilities: \n1. X-ray 2. Blood Test . cash payment\n2. leelavati Hospital:\nFacilities: 1. MRI 2. CT-Scan online as well as cash";
    }
    else {
        diagnosis = "No diagnosis";
        treatment = "No treatment";
        hospitals = "";
    }
}

int main() {
    string symptoms, symptom1;
    cout << "Enter the symptoms: ";
    getline(cin, symptoms);
    cout << "Enter the symptom: ";
    getline(cin, symptom1);

    string diagnosis, treatment, hospitals;
    expert_system(symptoms, symptom1, diagnosis, treatment, hospitals);

    cout << "Diagnosis: " << diagnosis << endl;
    cout << "Treatment: " << treatment << endl;
    cout << hospitals << endl;

    return 0;
}



