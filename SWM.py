import pandas as pd

# Create the data manually from the image
data = {
    "Sl. No": [1, 2, 3, 4, 5, 6, 7],
    "Name of ULB": [
        "Gangtok Municipal Corporation (GMC)",
        "Gyalsing Municipal Council (GyMC)",
        "Mangan Nagar Panchayat (MNP)",
        "Namchi Municipal Council (NMC)",
        "Rangpo Nagar Panchayat (RNP)",
        "Singtam Nagar Panchayat (SNP)",
        "Jorethang Municipal Council (JMC)"
    ],
    "Population (2011 census)": [100286, 6185, 4644, 15953, 10540, 5868, 11286],
    "Solid waste generated (TPD)": [50.00, 3.5, 0.60, 4.60, 10.00, 2.50, 3.50],
    "Solid waste collected (TPD)": [50.00, 3.5, 0.60, 4.50, 10.00, 2.50, 3.50],
    "Solid waste treated (TPD)": [11.00, 0.0, 0.06, 0.0, 0.0, 0.0, 1.5],
    "Solid waste landfilled/Disposed at dumping site (TPD)": [39.00, 3.5, 0.532, 4.5, 10.00, 2.50, 2.00]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_path = r"C:\Users\Vijol Lobo\OneDrive\Desktop\SMIT\SWM Assignment\SWM_2019-20.xlsx"
df.to_excel(excel_path, index=False)

excel_path
