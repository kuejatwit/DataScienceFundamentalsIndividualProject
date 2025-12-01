from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import ast


def parse_analog(cell):
	if pd.isna(cell):
		return None
	if isinstance(cell, (list, tuple, np.ndarray)):
		return [float(x) if x is not None else np.nan for x in list(cell)]
	if isinstance(cell, str):
		try:
			val = ast.literal_eval(cell)
			if isinstance(val, (list, tuple)):
				return [float(x) if x is not None else np.nan for x in val]
		except Exception:
			s = cell.strip()
			if s.startswith('[') and s.endswith(']'):
				s = s[1:-1]
			parts = [p.strip() for p in s.split(',') if p.strip() != '']
			try:
				return [float(p) for p in parts]
			except Exception:
				return None
	try:
		return [float(cell)]
	except Exception:
		return None


def main():
	model = KNN()
	dataSet = pd.read_csv("data/combined_data.csv")

	# Parse analog_reading into lists of floats
	parsed = dataSet['analog_reading'].apply(parse_analog)
	# Keep only rows where parsed succeeded
	valid = parsed.dropna()
	if valid.empty:
		raise RuntimeError('No valid analog_reading rows after parsing')

	lengths = valid.map(len)
	common_len = lengths.mode().iloc[0]
	valid = valid[lengths == common_len]

	# Ensure corresponding muscle_state values are present and drop NaNs
	y_series = dataSet.loc[valid.index, 'muscle_state']
	non_na_mask = y_series.notna()
	valid = valid[non_na_mask]
	y_series = y_series[non_na_mask]

	X = np.vstack(valid.values).astype(float)
	y = y_series.astype(int).values

	# Train/test split
	trainX, testX, trainY, testY = train_test_split(X, y, random_state=42)

	# Diagnostics
	print('DEBUG: X shape', X.shape, 'y shape', y.shape)

	model.fit(trainX, trainY)
	score = model.score(testX, testY)
	print(f'The model accuracy is: {score}')


if __name__ == '__main__':
	main()