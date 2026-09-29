MODULATION_LIMITS = {
    # Torso relocation
    # Torso acts as center of signing space. Anchors body according to where the speaking partner is -> Modulation is minimum.
    "torsorelocx": {"vmax": 0.0, "L": -1, "U": 1, "m": 0},
    "torsorelocy": {"vmax": 0.5, "L": -1, "U": 1, "m": 0}, 
    "torsorelocz": {"vmax": 3, "L": -8, "U": 8, "m": 0}, 

    # Torso rotation
    # Pitch maps to az; yaw maps to ay.
    "torsorelocax": {"vmax": 0.0, "L": -0.5, "U": 0.5, "m": 0},
    "torsorelocay": {"vmax": 0.0, "L": -0.7, "U": 0.7, "m": 0},  # torso_yaw_mean exists, but no consistent valence direction from literature
    "torsorelocaz": {"vmax": -0.14, "L": -0.5, "U": 0.5, "m": 1},  

    # Shoulders
    "domshoulderrelocx": {"vmax": 0.0, "L": -1.0, "U": 1.0, "m": 0},
    "ndomshoulderrelocx": {"vmax": 0.0, "L": -1.0, "U": 1.0, "m": 0},

    "domshoulderrelocy": {"vmax": 3.0, "L": -6.0, "U": 6.0, "m": 0},  
    "ndomshoulderrelocy": {"vmax": 3.0, "L": -6.0, "U": 6.0, "m": 0},  

    "domshoulderrelocz": {"vmax": 2.5, "L": -5.0, "U": 5.0, "m": 0},  
    "ndomshoulderrelocz": {"vmax": 2.5, "L": -5.0, "U": 5.0, "m": 0},  

    # Hand relocation
    # Hand y is used as a proxy for the retained left/right arm_angle_mean features (since theres no exact match).
    # +y is upward. Literature supports more upward hand/arm movement for positive valence.
    "domhandrelocx": {"vmax": 7, "L": -40.0, "U": 40.0, "m": 0},
    "ndomhandrelocx": {"vmax": 7, "L": -50.0, "U": 50.0, "m": 0},

    "domhandrelocy": {"vmax": 10.10, "L": -40.0, "U": 40.0, "m": 1},  
    "ndomhandrelocy": {"vmax": 5.35, "L": -50.0, "U": 50.0, "m": 1}, 

    "domhandrelocz": {"vmax": 18.0, "L": -50.0, "U": 50.0, "m": 0}, 
    "ndomhandrelocz": {"vmax": 18.0, "L": -50.0, "U": 50.0, "m": 0},  

    "domhandrelocax": {"vmax": 0.15, "L": -1.0, "U": 1.0, "m": 0},  
    "domhandrelocay": {"vmax": 0.15, "L": -1.0, "U": 1.0, "m": 0},  
    "domhandrelocaz": {"vmax": 0.15, "L": -1.0, "U": 1.0, "m": 0},  

    #Non dominant
    "ndomhandrelocax": {"vmax": 0.2, "L": -1.0, "U": 1.0, "m": 0},  
    "ndomhandrelocay": {"vmax": 0.2, "L": -1.0, "U": 1.0, "m": 0},  
    "ndomhandrelocaz": {"vmax": 0.2, "L": -1.0, "U": 1.0, "m": 0},  

    # Hand scale
    # Dominant
    "domhandrelocsx": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0},  
    "domhandrelocsy": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0},  
    "domhandrelocsz": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0},  

    #Non dominant
    "ndomhandrelocsx": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0}, 
    "ndomhandrelocsy": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0}, 
    "ndomhandrelocsz": {"vmax": 0.10, "L": 0.75, "U": 1.25, "m": 0}, 

    # Wrist / hand rotation
    #Dominant
    "domhandrotx": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  
    "domhandroty": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  
    "domhandrotz": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  

    #Non dominant
    "ndomhandrotx": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  
    "ndomhandroty": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  
    "ndomhandrotz": {"vmax": 0.15, "L": -1.20, "U": 1.20, "m": 0},  

    # Head rotation
    # z is pitch(up and down)and y is yaw (side-to-side).
    # Positive valence: raised head. Negative valence: lowered head.
    "headrotx": {"vmax": 0.0, "L": -0.90, "U": 0.90, "m": 0},  
    "headroty": {"vmax": 0.0, "L": -0.90, "U": 0.90, "m": 0},  
    "headrotz": {"vmax": -0.18, "L": -0.60, "U": 0.80, "m": 1},  
}