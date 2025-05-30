BINARY_FILE_HEADER_FORMAT = {
    # [length, name, mandatory]
    'ACQUISITION_DATE': [4,  False],
    'ACQUISITION_TIME': [4,  False],
    'CLIENT': [4,  False],
    'COMPANY': [2,  False],
    'GENERAL_CONSTANT': [2,  False],
    'INSTRUMENT': [2,  False],
    'JOB_ID': [2,  False],
    'OBSERVER': [2,  False],
    'PROCESSING_DATE': [2,  False],
    'PROCESSING_TIME': [2,  False],
    'TRACE_SORT': [2,  True],
    'UNITS': [2,  True],
    'NOTE': [2,  False]}

TRACE_HEADER_FORMAT = {
    # [length, name, special_type, start_byte]
    
    'ALIAS_FILTER': [4,  False, 0],
    'AMPLITUDE_RECOVERY': [4,  False, 4],
    'BAND_REJECT_FILTER': [4,  False, 8],
    'CDP_NUMBER': [4,  False, 12],
    'CDP_TRACE': [4,  False, 16],
    'CHANNEL_NUMBER': [4,  False, 20],
    'DATUM': [4,  False, 24],
    'DELAY': [2,  True, 28],
    'DESCALING_FACTOR': [2,  False, 30],
    'DIGITAL_BAND_REJECT_FILTER': [2,  False, 32],
    'DIGITAL_HIGH_CUT_FILTER': [2,  False, 34],
    'DIGITAL_LOW_CUT_FILTER': [4,  False, 36],
    'END_OF_GROUP': [4,  False, 40],
    'FIXED_GAIN': [4,  False, 44],
    'HIGH_CUT_FILTER': [4,  False, 48],    
    'LINE_ID': [4,  False, 52],
    'LOW_CUT_FILTER' : [4,  False, 48],
    'NOTCH_FREQUENCY': [4,  False, 56],
    'POLARITY': [4,  False, 60],
    'RAW_RECORD': [4,  False, 64],
    'RECEIVER': [2,  False, 68],
    'RECEIVER_GEOMETRY': [2,  False, 70],
    'RECEIVER_LOCATION': [4,  True, 72],
    'RECEIVER_SPECS': [4,  False, 76],
    'RECEIVER_STATION_NUMBER': [4,  False, 80],
    'SAMPLE_INTERVAL': [4,  True, 84],
    'SHOT_SEQUENCE_NUMBER': [2,  False, 88],
    'SKEW': [2,  False, 90],
    'SOURCE': [2,  False, 92],
    'SOURCE_GEOMETRY': [2,  False, 94],
    'SOURCE_LOCATION': [2,  False, 96],
    'SOURCE_STATION_NUMBER': [2,  False, 98],
    'STACK': [2,  False, 100],
    'STATIC_CORRECTIONS': [2,  False, 102],
    'TRACE_TYPE': [2,  False, 104],
    'NOTE': [2,  False, 106]}

MONTHLIST = [
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", 
    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"  
]
DEFAULTVALUES = {
    'date' : '01/JAN/1990',
    'time' : '09:30:00',
    'anystring' : ' ',
    'instrument' : '    0000',
    'observer' : 'Observer'    
    
}
DEFAULT_FH_VALUES ={
    'trace_sequence_number_within_segy_file': 0,
    'ensemble_number': 0,
    'trace_number_within_the_ensemble': 0,
    'trace_identification_code': 1,
    'number_of_horizontally_stacked_traces_yielding_this_trace': 0,
    'datum_elevation_at_receiver_group': 0,
    'source_coordinate_x': 0,
    'source_coordinate_y': 0,
    'group_coordinate_x': 0,
    'group_coordinate_y': 0,
    'source_static_correction_in_ms': 0,
    'group_static_correction_in_ms': 0,
    'total_static_applied_in_ms': 0,
    'delay_recording_time': 0,
    'sample_interval_in_ms_for_this_trace': 0,
    'gain_type_of_field_instruments': 0,
    'instrument_early_or_initial_gain': 0,
    'sweep_frequency_at_end': 0,
    'alias_filter_frequency': 0,
    'alias_filter_slope': 0,
    'notch_filter_frequency': 0,
    'low_cut_frequency': 0,
    'high_cut_frequency': 0,
    'low_cut_slope': 0,
    'high_cut_slope': 0,
    'source_type_orientation': 0
}
