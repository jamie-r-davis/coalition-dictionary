# Coalition Dictionary

A semi-automated process to parse the complete Coalition data dictionary, including member questions.


## Installation

To use this script, clone or download the repository onto your computer. Then install the dependencies by running inside the project folder:

```bash
pip install -r requirements.txt
```

## Usage

In your browser, log into Coalition in order to establish an active session. Then paste the following url into your browser:

https://www.mycoalition.org/external/api/admin/admit/api/v1/attr?activity=false&secure=false

This will return a complete JSON representation of the data dictionary. Save this response.

Once you have the raw json saved to your machine, run the script. It takes two parameters: `json_file`, which is the path to your raw json, and `destination_file` which is the path where the output file should go.

```bash
python app.py raw.json CoalitionDataDictionary.xlsx
```
