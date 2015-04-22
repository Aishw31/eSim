class TrackWidget:
    """
    This Class track the dynamically created widget of KicadtoNgSpice Window.
    """
    #Track widget list for Source details
    sourcelisttrack = {"ITEMS":"None"}
    source_entry_var = {"ITEMS":"None"}
    
    #Track widget for analysis inserter details
    AC_entry_var = {"ITEMS":"None"}
    AC_Parameter = {"ITEMS":"None"}
    DC_entry_var = {"ITEMS":"None"}
    DC_Parameter = {"ITEMS":"None"} 
    TRAN_entry_var = {"ITEMS":"None"} 
    TRAN_Parameter = {"ITEMS":"None"}
    set_CheckBox = {"ITEMS":"None"}
    AC_type = {"ITEMS":"None"}
    
    #Track widget for Model detail
    modelTrack = []
    model_entry_var = {}
    
    #Track Widget for Device Model detail
    deviceModelTrack = {}