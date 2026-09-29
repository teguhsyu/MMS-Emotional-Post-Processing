# Documentation

# Overview

The emotional post-processing layer modifies an existing MMS instance
based on continuous valence and/or arousal values.

Valence is mainly used to modulate selected body-related MMS parameters,
while arousal is used to modulate duration and transition. Expressiveness
`k` controls the strength of the applied modulation.

# Valence Modulation

Valence is represented in the range `[-1, 1]`.

The selected MMS parameters are modulated using:

    x_new = clip(x + m * k * v * Vmax, L, U)

where:

- `x` = original inflection value
- `v` = valence
- `k` = expressiveness
- `m` = whether the parameter is active
- `Vmax` = maximum modulation
- `L`, `U` = lower and upper limits

The final parameter configuration is stored in `modulation_limits.py`.

Each dataset feature was mapped to the MMS parameter representing the
same or closest corresponding body movement. In cases where there is no
direct MMS equivalent, the closest available parameter is used as a proxy.

# Arousal Modulation

Arousal is represented in the range `[-1, 1]` and is applied to
`duration` and `transition`.

    duration_new = duration * (1 - 0.30 * a)

    transition_new = transition * (1 - 0.25 * a)

Higher arousal therefore results in shorter durations and transitions,
while lower arousal results in longer ones.

The values `0.30` and `0.25` are proposed scaling values for the current
prototype.

# Output

The original MMS instance is kept unchanged. The program creates a new
modulated MMS instance inside `MMS-modulated/`, which can then be rendered
using the DFKI MMS Player.

For the available MMS parameters and their coordinate conventions, see
the official MMS Player documentation:
https://github.com/DFKI-SignLanguage/MMS-Player/blob/main/Docs/MMS.md
