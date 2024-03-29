import pandas as pd

print("reading")
raw_data = pd.read_json("opendata.jsonl", lines=True)

print("processing")
dataset = raw_data.loc[(raw_data["schema_version"] == "v4") & raw_data["data"].str[0].str["blender_version"].str["version"].str.contains("4.0.\d"), "data"]

bench_1 = pd.json_normalize(dataset.str[0])
bench_2 = pd.json_normalize(dataset.str[1])
bench_3 = pd.json_normalize(dataset.str[2])

print()
print(bench_1["scene.label"].value_counts())
print()
print(bench_2["scene.label"].value_counts())
print()
print(bench_3["scene.label"].value_counts())

monster_dataset = pd.concat([bench_1.loc[bench_1["scene.label"] == "monster"], bench_2.loc[bench_2["scene.label"] == "monster"], bench_3.loc[bench_3["scene.label"] == "monster"]], ignore_index=True)
junkshop_dataset = pd.concat([bench_1.loc[bench_1["scene.label"] == "junkshop"], bench_2.loc[bench_2["scene.label"] == "junkshop"], bench_3.loc[bench_3["scene.label"] == "junkshop"]], ignore_index=True)
classroom_dataset = pd.concat([bench_1.loc[bench_1["scene.label"] == "classroom"], bench_2.loc[bench_2["scene.label"] == "classroom"], bench_3.loc[bench_3["scene.label"] == "classroom"]], ignore_index=True)



print("saving")
towrite = monster_dataset.to_json()

myfile = open("monster_dataset.json", "w")
myfile.write(towrite)
myfile.close()

towrite = junkshop_dataset.to_json()

myfile = open("junkshop_dataset.json", "w")
myfile.write(towrite)
myfile.close()

towrite = classroom_dataset.to_json()

myfile = open("classroom_dataset.json", "w")
myfile.write(towrite)
myfile.close()