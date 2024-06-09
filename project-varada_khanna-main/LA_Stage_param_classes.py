from enum import Enum

import numpy as np

import Inputdata as data

class Therapies(Enum):
    """ Yes vs No therapy"""
    MONO = 0
    COMBO = 1   ##Therapy is given


class Parameters:
    def __init__(self, therapy):

        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = data.HealthStates.WELL

        # annual treatment cost
        if self.therapy == Therapies.COMBO: #####################
            self.annualTreatmentCost = data.COST_LOCAL_ADVANCED_SURGERY_AND_RADIATION
            self.annualUtilities= data.utility__LA_stage_surgery_with_RT
        else:
            self.annualTreatmentCost = data.COST_LOCAL_ADVANCED_SURGERY

        # transition probability matrix of the selected therapy
        self.probMatrix = []

        # calculate transition probabilities between cancer states
        if self.therapy == Therapies.MONO:
            # calculate transition probability matrix for the no therapy
            self.probMatrix = get_prob_matrix_mono(trans_matrix=data.TRANS_MATRIX)

        elif self.therapy == Therapies.COMBO:
            # calculate transition probability matrix for the  therapy
            self.probMatrix = get_prob_matrix_combo(
                prob_matrix_mono=get_prob_matrix_mono(trans_matrix=data.TRANS_MATRIX),
                therapy_rr=data.RR_SURGERY_RADIATION_LA_STAGE)

        # annual state costs and utilities
        self.annualStateCosts = data.ANNUAL_STATE_COST

        # # Debug statement: Print the value and type of annualStateCosts
        # print("Debug: annualStateCosts -", self.annualStateCosts, type(self.annualStateCosts))

        self.annualStateUtilities = data.ANNUAL_STATE_UTILITY

        # cost
        # if self.therapy == Therapies.MONO:
        #     self.annualStateCosts[2] += data.COST_LOCAL_ADVANCED_SURGERY
        # else:
        #     self.annualStateCosts[2] += data.COST_LOCAL_ADVANCED_SURGERY_AND_RADIATION chnage
        if self.therapy == Therapies.COMBO:
            self.annualStateCosts[2] = data.COST_LOCAL_ADVANCED_SURGERY_AND_RADIATION
            self.annualStateUtilities[2] = data.utility__LA_stage_surgery_with_RT
        else:
            self.annualStateCosts[2] = data.COST_LOCAL_ADVANCED_SURGERY





        # discount rate
        self.discountRate = data.DISCOUNT
        print("Annual State Cost:", self.annualStateCosts)


def get_prob_matrix_mono(trans_matrix):
    """
    :param trans_matrix: transition matrix containing counts of transitions between states
    :return: transition probability matrix
    """

    # initialize transition probability matrix
    trans_prob_matrix = []

    # for each row in the transition matrix
    for row in trans_matrix:
        # calculate the transition probabilities
        prob_row = np.array(row)/sum(row)
        # add this row of transition probabilities to the transition probability matrix
        trans_prob_matrix.append(prob_row)

    return trans_prob_matrix


def get_prob_matrix_combo(prob_matrix_mono, therapy_rr):
    """
    :param prob_matrix_mono: (list of lists) transition probability matrix under no therapy
    :param therapy_rr: relative risk of the combination treatment
    :returns (list of lists) transition probability matrix under combination therapy """

    # create an empty list of lists
    matrix_therapy = []
    for row in prob_matrix_mono:
        matrix_therapy.append(np.zeros(len(row)))  # adding a row [0, 0, 0, 0]

    # populate the therapy matrix
    # calculate the effect of therapy on non-diagonal elements
    for s in range(len(matrix_therapy)):
        for next_s in range(s + 1, len(prob_matrix_mono[s])):
            if s == 2 and next_s == 3:
                matrix_therapy[s][next_s] = therapy_rr * prob_matrix_mono[s][next_s]
            else:
                matrix_therapy[s][next_s] = prob_matrix_mono[s][next_s]

    # diagonal elements are calculated to make sure the sum of each row is 1
    for s in range(len(matrix_therapy)):
        matrix_therapy[s][s] = 1 - sum(matrix_therapy[s][s+1:])

    return matrix_therapy


# tests
if __name__ == '__main__':
    matrix_mono = get_prob_matrix_mono(data.TRANS_MATRIX)
    matrix_combo= get_prob_matrix_combo(matrix_mono, data.RR_SURGERY_RADIATION_LA_STAGE)

    print(np.round(matrix_mono, decimals=6))
    print(np.round(matrix_combo, decimals=6))
## addition of each row is 1