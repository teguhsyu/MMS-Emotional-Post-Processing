# instance_modulator.py

from pathlib import Path
import pandas as pd

from modulation_limits import MODULATION_LIMITS


INPUT_FOLDER = Path("MMS-examples")
OUTPUT_FOLDER = Path("MMS-modulated")


def modulate_mms(input_path, output_path, v, a, k, use_valence, use_arousal):
    """
    Reads an MMS CSV file, modulates selected columns based on continuous valence
    and/or arousal, and saves the result to a new CSV file.
    """

    # Check if inputs ar valid.
    if v < -1 or v > 1:
        print("Error: Valence takes a value [-1, 1]")
        exit()

    if a < -1 or a > 1:
        print("Error: Arousal takes a value [-1, 1]")
        exit()

    if k < 0 or k > 1:
        print("Error: Expressiveness takes a value [0, 1]")
        exit()

    # Places mms instance of interest into a dataframe.
    df = pd.read_csv(input_path, keep_default_na=False)
    changed_columns = []

    for column in df.columns:
        column_name = column.lower() # To prevent case sensitivity

        # ==================================================
        # Valence modulated 
        # ==================================================

        # Alter only columns based on inflection groups, if it exists in the MMS instances.
        if use_valence and column_name in MODULATION_LIMITS:
        
            # Collect all required parameters.
            rule = MODULATION_LIMITS[column_name]
            m = rule["m"]
            vmax = rule["vmax"]
            L = rule["L"]
            U = rule["U"]

            inf = pd.to_numeric(df[column], errors="coerce")

            # x_new = clip(x + m * k * v * vmax, L, U)
            inf_new = inf + m * k * v * vmax
            inf_new = inf_new.clip(L, U)

            # Replaces inflections with new ones in the same cell of the dataframe.
            df[column] = inf_new.where(inf.notna(), df[column])

            # Collect all changed columns here.
            changed_columns.append(column)

        # ==================================================
        # Arousal modulated
        # ==================================================

        if use_arousal:

            values = pd.to_numeric(df[column], errors="coerce")

            # ---------------------------------------------
            # Duration
            # Higher arousal -> shorter duration
            # Lower arousal -> longer duration
            # ---------------------------------------------

            if column_name == "duration":

                new_values = values * (1 - a * 0.30)

                df[column] = new_values.where(
                    values.notna(), df[column]
                )

                changed_columns.append(column)

            # ---------------------------------------------
            # Transition
            # Higher arousal -> snappier transitions
            # Lower arousal -> smoother transitions
            # ---------------------------------------------

            elif column_name == "transition":

                new_values = values * (1 - a * 0.25)

                df[column] = new_values.where(
                    values.notna(), df[column]
                )

                changed_columns.append(column)

    # Gets output folder path, if it exists, then convert modulated dataframe to csv and save in corresponding file.
    Path(output_path).parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    return changed_columns


# Get input from user
file_name = input("Enter MMS .csv filename/path: ").strip()

mode = input(
    "Mode (valence / arousal / both): "
).strip().lower()

v = 0.0
a = 0.0

if mode in ("valence", "both"):
    v = float(input("Enter valence [-1, 1]: "))

if mode in ("arousal", "both"):
    a = float(input("Enter arousal [-1, 1]: "))

k = float(input("Enter expresiveness [0, 1]: "))

use_valence = mode in ("valence", "both")
use_arousal = mode in ("arousal", "both")

input_path = Path(file_name)

# If the user only gives a file name, look inside MMS-examples folder
if not input_path.exists():
    input_path = INPUT_FOLDER / file_name

# If not found in MMS-examples folder, throw error.
if not input_path.exists():
    print("Error: file not found:", input_path)
    exit()

# Create output file name
suffix = ""

if use_valence:
    suffix += f"_v{v}"

if use_arousal:
    suffix += f"_a{a}"

suffix += f"_k{k}"

if input_path.name.endswith(".mms.csv"):
    output_name = input_path.name.replace(
        ".mms.csv",
        suffix + ".mms.csv"
    )
else:
    output_name = input_path.stem + suffix + input_path.suffix

# Gets complete path of for outputted file
output_path = OUTPUT_FOLDER / output_name

changed_columns = modulate_mms(
    input_path,
    output_path,
    v,
    a,
    k,
    use_valence,
    use_arousal
)

print("Modulated MMS .csv file", output_path)
