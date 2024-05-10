# To install pandas, open cmd, enter 'python -m pip install pandas', and restart VS Code
# Import pandas
import pandas as pd

# Read csv file
dforiginal = pd.read_csv('G:\My Drive\Deepak\Just IT\Data Tech Bootcamp\GitHub\Portfoilio\mxmh.csv')

# Show original data
print(dforiginal)

# Show data types (checklist: dtypes, null count) (object=str, float64=decimal)
dforiginal.info()

# Remove all rows with null values
df = dforiginal.dropna()
df.info()

# Reset index to be sequential numbers
df.reset_index(drop=True,inplace=True)
print(df)

# Show list of cols
list(df)

# Change data type for multiple cols
df = df.astype({
    "Age":int,
    "BPM":int,
    "Anxiety":int,
    "Depression":int,
    "Insomnia":int,
    "OCD":int
})
df.info()

#Check Timestamp col format
print(df.Timestamp)

# Separate date and time into 2 different cols
df[['Date', 'Time']] = df['Timestamp'].str.split(' ', n=1, expand=True)
print(df)

# Check date col format
print(df.Date)

# Convert date column from object to yyyy-mm-dd format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y', errors='coerce').combine_first(pd.to_datetime(df['Date'], format='%m/%d/%y', errors='coerce'))
print(df.Date)

# Convert time col from strings to hh:mm:ss format
# Alternatively: df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').combine_first(pd.to_datetime(df['Time'],format='%H:%M',errors='coerce')).dt.time
time_hms = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.time
time_hm = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.time
df['Time'] = time_hms.combine_first(time_hm)

print(df.Time)

# Final view of data
print(df)

# Export cleaned data as a new csv file (change all backslash to forwardslash ?que?)
file_path = 'G:/My Drive/Deepak/Just IT/Data Tech Bootcamp/GitHub/Portfoilio/mxmh_pythoncleaned.csv'
df.to_csv(file_path,index=False)