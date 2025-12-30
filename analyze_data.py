import pandas as pd

def main():
    # Read the data
    df = pd.read_csv('patient_cohort.csv')
    
    # Calculate change in heart rate
    df['HeartRate_Change'] = df['HeartRate_FollowUp'] - df['HeartRate_Initial']
    
    # Identify patients with bradycardia (follow-up HR < 60 bpm)
    bradycardia_patients = df[df['HeartRate_FollowUp'] < 60]
    
    print("Total patients:", len(df))
    print("Patients with bradycardia:", len(bradycardia_patients))
    print("Bradycardia rate: {:.1f}%".format(len(bradycardia_patients) / len(df) * 100))
    
    # Optionally list the patients
    print("\nBradycardia patients:")
    print(bradycardia_patients[['PatientID', 'BetaBlocker', 'HeartRate_Initial', 'HeartRate_FollowUp']])

if __name__ == "__main__":
    main()