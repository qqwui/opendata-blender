# Blender Benchmark Data parser
A messy way of parsing blender benchmark data using the Pandas python library.

To use this, get the latest [Blender benchmark database dump](https://opendata.blender.org/download/), rename the opendata-*.jsonl file to opendata.jsonl and run `python 3 process_2.0.py`.

The resulting files should be the datasets for the monster, junkshop, and classroom scenes in normalised json.

## Limitations
- The current method of processing only gets the data for Blender 4.0
- Only supports version 4 of the data format. 
- Python and Pandas may not be the best or fastest platform for this project.

## Todos/Improvements
In no particular order:
- Output data in a more easily parsed format. Currently individual scenes are extracted from the master dataset and dumped to JSON.
- Support all data versions to get historical data.
