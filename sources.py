DATA_SOURCES={
    "source1":"lastDP(ADIFM_B2, TOTAL)",
    "source2":"getDP(ADIFM_B2, TOTAL, 2023-02-02 00:55:00)",
    "source3":"consumption(ADIFM_B2, TOTAL,06:00,1)",
    "source4":"wconsumption(ADIFM_B2, TOTAL,06:00,0,Mo)",
    "source5":"mconsumption(ADIFM_B2,1)",
    "source6":"qconsumption(ADIFM_B2, TOTAL,06:00,1)",
    "source7":"hyconsumption(ADIFM_B2, TOTAL,06:00,0)",
    "source8":"yconsumption(ADIFM_B2, TOTAL,06:00,0)",
    # "source9":"consumptionInterval(ADIFM_B2, TOTAL, 2024-01-01 00:00:00, 2024-01-12 00:00:00)",
    # "source10":"consumptionLoadEntity(LOAD_ENTITY, 2023-02-02 00:55:00, 2023-04-09 23:35:20)",
    # "source11":"ifTrueInterval(APRPLC_A1,D3, 2023-02-02, 2023-02-12, ><, [1|10], time, sum)",
    # "source12":"runtime(ADIFM_B2, TOTAL, >, [0], 2024-01-01 00:00:00, 2024-01-31 23:59:59)",
    # "source13":"onSetTime(ADIFM_B2,TOTAL, >, [0], 2024-01-01 00:00:00, 2024-01-31 23:59:59)",
    # "source14":"offSetTime(ADIFM_B2,TOTAL, >, [0], 2024-01-01 00:00:00, 2024-01-31 23:59:59)",
    # "source15":"AVG(getRollingData(ADIFM_B2, TOTAL, M, 00:00, 0))",
    # "source16":"AVG(getRollingData(ADIFM_B2, TOTAL, 5D, 00:00, 0))",
    # "source17":"AVG(getRollingData(ADIFM_B2, TOTAL, M, 00:00, 0))",
    # "source18":"AVG(getRollingData(ADIFM_B2, TOTAL, 2W, 00:00, 0))",
    # "source19":"AVG(getSampledData(ADIFM_B2, TOTAL, 2023-08-01 06:30:00, 2023-08-10 06:30:00, H, last))",
    # "source20":"AVG(getSampledData(ADIFM_B2, TOTAL, 2023-08-01 06:30:00, 2023-08-10 06:30:00, H, last))",
    # "source21":"AVG(getRollingSampledData(ADIFM_B2, TOTAL, D, 00:00, 1, H, last))",
    # "source22":"IF(lastDP(APRPLC_B3,D20)/ 10,><,[consumption(APRPLC_B3, D20,06:00,10) | 11111],Yes, No)",
    # "source23":"IF(AND(lastDP(APRPLC_B3,D20)/ 10,><,[consumption(APRPLC_B3, D20,06:00,10) | 11111],lastDP(APRPLC_B3,D20)/ 10,><,[consumption(APRPLC_B3, D20,06:00,10) | 11111],lastDP(APRPLC_B3,D20)/ 10,><,[consumption(APRPLC_B3, D20,06:00,10) | 11111]),YES,No)"
}          