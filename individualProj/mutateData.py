import pandas as pd

openFist = pd.read_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/openFist.csv")
closedFist = pd.read_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/closedFist.csv")
# Turn every 5 rows in analog_reading into one list of integers for both openFist and closedFist
def mutate_data(df):
    mutated_rows = []
    for i in range(0, len(df), 5):
        chunk = df.iloc[i:i+5]
        if len(chunk) == 5:
            # Convert analog readings to ints (drop/keep None for NaN)
            analog_readings_raw = chunk['analog_reading'].tolist()
            analog_readings = []
            for v in analog_readings_raw:
                if pd.isna(v):
                    analog_readings.append(None)
                else:
                    try:
                        analog_readings.append(int(v))
                    except Exception:
                        # fallback: convert via float then int
                        analog_readings.append(int(float(v)))

            mutated_rows.append({
                'analog_reading': analog_readings,
                'muscle_state': int(chunk['muscle_state'].iloc[0])
            })
    return pd.DataFrame(mutated_rows)
openFist_mutated = mutate_data(openFist)
closedFist_mutated = mutate_data(closedFist)
# Save mutated data
openFist_mutated.to_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/openFist_mutated.csv", index=False)
closedFist_mutated.to_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/closedFist_mutated.csv", index=False)
# Verify in-memory that each element in analog_reading is a list of ints
if len(openFist_mutated) > 0:
    first = openFist_mutated['analog_reading'].iloc[0]
    print('openFist_mutated first analog_reading:', first)
    print('type of column element:', type(first))
    if isinstance(first, list):
        print('element types:', [type(x) for x in first])

if len(closedFist_mutated) > 0:
    first = closedFist_mutated['analog_reading'].iloc[0]
    print('closedFist_mutated first analog_reading:', first)
    print('type of column element:', type(first))
    if isinstance(first, list):
        print('element types:', [type(x) for x in first])