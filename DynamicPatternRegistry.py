# This file serves as a registry for the dynamic patterns.
# When creating a new dynamic pattern, import it to this file and add it to the list of dynamic_pattern_classes.
# Do not otherwise alter this file.

# Modify here

import DynamicPatternOutsideInRemix
import DynamicPatternElection

dynamic_pattern_classes = [DynamicPatternOutsideInRemix.OutsideInRemix(), DynamicPatternElection.Election()]


# Do not modify

dynamic_pattern_mapping = {dynamic_pattern_class.get_name(): dynamic_pattern_class for dynamic_pattern_class in dynamic_pattern_classes}

def get_dynamic_pattern_names():
	return dynamic_pattern_mapping.keys()

def dynamic_pattern_class_for_name(name):
	dnyamic_pattern_class = dynamic_pattern_mapping[name].__class__
	return dnyamic_pattern_class()