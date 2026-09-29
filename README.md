# MMS-Emotional-Post-Processing

This repository contains the emotional post-processing layer developed during our seminar project.

The program takes an existing MMS instance and modulates it based on valence and/or arousal. 
The resulting MMS instance can then be rendered using the original 
[DFKI MMS Player](https://github.com/DFKI-SignLanguage/MMS-Player).

# Files

- `instance_modulator.py` – applies valence and arousal modulation
- `modulation_limits.py` – contains the parameters and limits for valence modulation
- `MMS-examples/` – example MMS instances
- `DOCUMENTATION.md` – further explanation of the implementation

# Usage

The program requires Python and pandas:

    pip install pandas

Run:

    python instance_modulator.py

The terminal will guide the user through the required inputs. The
modulated MMS instance is saved in `MMS-modulated/`.

For further information, see [DOCUMENTATION.md](DOCUMENTATION.md).
