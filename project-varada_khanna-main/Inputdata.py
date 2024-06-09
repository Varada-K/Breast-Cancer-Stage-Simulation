from enum import Enum
# simulation settings
POP_SIZE = 5000     # cohort population size
SIM_TIME_STEPS = 15    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ANNUAL_PROB_ALL_CAUSE_MORT = 19.6/ 100000 #
P_Metastasis_death = 1-0.13 # only 25% survival on a 10 year time period
Chance_of_Breast_Cancer_from_well = 0.13
P_EARLY_TO_LOCAL_ADVANCED = 0.46
P_LOCAL_ADVANCED_TO_METASTASIS = 0.70


class HealthStates(Enum):
    """ health states of patients """
    WELL = 0
    EARLY_STAGE = 1
    LOCALIZED_ADVANCED = 2
    METASTASIS = 3
    CANCER_DEATH = 4
    ALL_CAUSE_DEATH = 5


# transition probability matrix with temporary state Stroke
TRANS_MATRIX = [
    # Well
    [
        (1-Chance_of_Breast_Cancer_from_well)*(1-ANNUAL_PROB_ALL_CAUSE_MORT),  # Well
        Chance_of_Breast_Cancer_from_well,                                   # EARLY STAGE
        0,                                                            # LOCAL_ADVANCED
        0,                                                            # METASTASIS
        0,                                                            # CANCER Death
        ANNUAL_PROB_ALL_CAUSE_MORT                                    # All-cause mortality
    ],

    # EARLY_STAGE
    [
        0,                                                            # Well
        (1-P_EARLY_TO_LOCAL_ADVANCED)*(1-ANNUAL_PROB_ALL_CAUSE_MORT),# EARLY STAGE
        P_EARLY_TO_LOCAL_ADVANCED,                                   # LOCAL_ADVANCED
        0,                                                            # METASTASIS
        0,                                                            # CANCER Death
        ANNUAL_PROB_ALL_CAUSE_MORT                                    # All-cause mortality
    ],

    # LOCAL_ADVANCED
    [
        0,                                                            # Well
        0,                                                            # EARLY STAGE
        (1-P_LOCAL_ADVANCED_TO_METASTASIS)*(1-ANNUAL_PROB_ALL_CAUSE_MORT),  # LOCAL_ADVANCED
        P_LOCAL_ADVANCED_TO_METASTASIS,                              # METASTASIS
        0,                                                            # CANCER Death
        ANNUAL_PROB_ALL_CAUSE_MORT                                    # All-cause mortality
    ],

    # METASTASIS
    [
        0,                                                            # Well
        0,                                                            # EARLY STAGE
        0,                                                            # LOCAL_ADVANCED
        (1-P_Metastasis_death)*(1-ANNUAL_PROB_ALL_CAUSE_MORT),      # METASTASIS
        P_Metastasis_death,                                          # CANCER Death
        ANNUAL_PROB_ALL_CAUSE_MORT                                    # All-cause mortality
    ],

    # ALL_CAUSE_DEATH
    [
        0,                                                            # Well
        0,                                                            # EARLY STAGE
        0,                                                            # LOCAL_ADVANCED
        0,                                                            # METASTASIS
        1,                                                            # CANCER Death
        0                                                             # All-cause mortality
    ],

    # ALL_CAUSE_DEATH
    [
        0,                                                            # Well
        0,                                                            # EARLY STAGE
        0,                                                            # LOCAL_ADVANCED
        0,                                                            # METASTASIS
        0,                                                            # CANCER Death
        1                                                             # All-cause mortality
    ]
]

ANNUAL_STATE_COST = [
    0,     # Well
    0,     # EARLY STAGE
    600,   # LOCAL_ADVANCED
    1000,  # METASTASIS
    0,     # CANCER Death
    0      # All-cause mortality
]


print('Transition probability matrix:', TRANS_MATRIX)
print('')

# costs FOR SURGERY
COST_EARLY_STAGE_SURGERY = 8225
COST_LOCAL_ADVANCED_SURGERY = 63348

# costs for LA and surgery
COST_EARLY_STAGE_SURGERY_AND_RADIATION = 14963  ### COde changes now
COST_LOCAL_ADVANCED_SURGERY_AND_RADIATION = 84481

#RR
RR_SURGERY_RADIATION_EARLY_STAGE= 0.086  # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3068638/
RR_SURGERY_RADIATION_LA_STAGE= 0.33 # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244192/


# Original utility values
ANNUAL_STATE_UTILITY_1= [
    1,     # Well
    0.95,  # EARLY STAGE
    0.725, # LOCAL_ADVANCED
    0.691, # METASTASIS
    0,     # CANCER Death
    0      # All-cause mortality of utility
]


# Calculate adjusted utility for surgery alone
adjusted_utility_early_stage_surgery_alone = ANNUAL_STATE_UTILITY_1[1] * (1 - RR_SURGERY_RADIATION_EARLY_STAGE)

# No adjustment needed for surgery with radiation therapy
utility__early_stage_surgery_with_RT = ANNUAL_STATE_UTILITY_1[1]
# Calculate adjusted utility for surgery alone
adjusted_utility_LA_stage_surgery_alone = ANNUAL_STATE_UTILITY_1[2] * (1 - RR_SURGERY_RADIATION_LA_STAGE)

# No adjustment needed for surgery with radiation therapy
utility__LA_stage_surgery_with_RT = ANNUAL_STATE_UTILITY_1[2]

ANNUAL_STATE_UTILITY = [
    1,  # Well
    adjusted_utility_early_stage_surgery_alone,  # EARLY STAGE
    adjusted_utility_LA_stage_surgery_alone,  # LOCAL_ADVANCED
    0.691-0.1212,  # METASTASIS (without any treatment, but no adjustments, as this is out of the scope of this study)
    0,  # CANCER Death
    0  # All-cause mortality of utility
]
# #
# print (ANNUAL_STATE_UTILITY)

ANNUAL_STATE_UTILITY_2=[1, 0.8683, 0.48574999999999996, 0.5698, 0, 0]