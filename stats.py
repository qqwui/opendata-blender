import pandas as pd

classroom_dataset = pd.read_json("classroom_dataset.json")

print(classroom_dataset.info())
print()

print("Number of Devices per Computer")
print(pd.Series(len(x) for x in classroom_dataset["system_info.devices"] if type(x) == list).value_counts())
print()

print("Device counts")
print(classroom_dataset["device_info.compute_devices"].str[0].str["name"].value_counts().head())
print()

print("NVIDIA GeForce RTX 4090 stats")
print(classroom_dataset.loc[classroom_dataset["device_info.compute_devices"].str[0].str["name"] == "NVIDIA GeForce RTX 4090", "stats.samples_per_minute"].describe())
print()

print("AMD Ryzen 9 7950X 16-Core Processor stats")
print(classroom_dataset.loc[classroom_dataset["device_info.compute_devices"].str[0].str["name"] == "AMD Ryzen 9 7950X 16-Core Processor", "stats.samples_per_minute"].describe())
print()