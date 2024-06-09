import numpy as np
import deampy.econ_eval as econ
import deampy.statistics as stat
from deampy.markov import MarkovJumpProcess
from deampy.plots.sample_paths import PrevalencePathBatchUpdate
from Inputdata import HealthStates
class Patient:
    def __init__(self, id, parameters):
        """ initiates a patient
        :param id: ID of the patient
        :param parameters: an instance of the parameters class
        """
        self.id = id
        self.params = parameters
        self.stateMonitor = PatientStateMonitor(parameters=parameters)

    def simulate(self, n_time_steps):
        """ simulate the patient over the specified simulation length """

        # random number generator
        rng = np.random.RandomState(seed=self.id)
        # Markov jump process
        markov_jump = MarkovJumpProcess(transition_prob_matrix=self.params.probMatrix)

        k = 0  # simulation time step

        # while the patient is alive and simulation length is not yet reached
        while self.stateMonitor.get_if_alive() and k < n_time_steps:
            # sample from the Markov jump process to get a new state
            # (returns an integer from {0, 1, 2, ...})
            new_state_index = markov_jump.get_next_state(
                current_state_index=self.stateMonitor.currentState.value,
                rng=rng)

            # update health state
            self.stateMonitor.update(time_step=k, new_state=HealthStates(new_state_index))

            # increment time
            k += 1

class PatientStateMonitor:
    def __init__(self, parameters):

        self.currentState = parameters.initialHealthState  # initial health state  ############ have to add code next file
        self.currentState = HealthStates.WELL    # assuming everyone starts in "Well"
        self.survivalTime = None
        self.nStrokes = 0
        # patient's cost and utility monitor
        self.costUtilityMonitor = PatientCostUtilityMonitor(parameters=parameters)

    def update(self, time_step, new_state):

        if self.currentState in (HealthStates.CANCER_DEATH, HealthStates.ALL_CAUSE_DEATH):
            return

        if new_state in (HealthStates.CANCER_DEATH, HealthStates.ALL_CAUSE_DEATH):
            self.survivalTime = time_step + 0.5  # correct for half cycle effect


        # update cost and utility
        self.costUtilityMonitor.update(k=time_step,
                                     current_state=self.currentState,
                                     next_state=new_state)

        self.currentState = new_state

    def get_if_alive(self):
        if self.currentState in (HealthStates.CANCER_DEATH, HealthStates.ALL_CAUSE_DEATH):
            return False
        else:
            return True

class PatientCostUtilityMonitor:

    def __init__(self, parameters):

        # model parameters for this patient
        self.params = parameters

        # total cost and utility
        self.totalDiscountedCost = 0
        self.totalDiscountedUtility = 0

    def update(self, k, current_state, next_state):
        """ updates the discounted total cost and health utility
        :param k: simulation time step
        :param current_state: current health state
        :param next_state: next health state
        """
        # # Debug statement: Print the value and type of annualStateCosts
        # print("Debug: annualStateCosts -", self.params.annualStateCosts, type(self.params.annualStateCosts))

        # update cost
        cost = 0.5 * (self.params.annualStateCosts[current_state.value] +
                      self.params.annualStateCosts[next_state.value])
        # update utility
        utility = 0.5 * (self.params.annualStateUtilities[current_state.value] +
                         self.params.annualStateUtilities[next_state.value])


        # update total discounted cost and utility (corrected for the half-cycle effect)
        self.totalDiscountedCost += econ.pv_single_payment(payment=cost,
                                                           discount_rate=self.params.discountRate / 2,
                                                           discount_period=2 * k + 1)
        self.totalDiscountedUtility += econ.pv_single_payment(payment=utility,
                                                              discount_rate=self.params.discountRate / 2,
                                                              discount_period=2 * k + 1)

class Cohort:
    def __init__(self, id, pop_size, parameters):
        """ create a cohort of patients
        :param id: cohort ID
        :param pop_size: population size of this cohort
        :param parameters: parameters
        """
        self.id = id
        self.popSize = pop_size
        self.params = parameters
        self.cohortOutcomes = CohortOutcomes()  # outcomes of this simulated cohort

    def simulate(self, n_time_steps):
        """ simulate the cohort of patients over the specified number of time-steps
        :param n_time_steps: number of time steps to simulate the cohort
        """

        # populate and simulate the cohort
        for i in range(self.popSize):
            # create a new patient (use id * pop_size + n as patient id)
            patient = Patient(id=self.id * self.popSize + i,
                              parameters=self.params)
            # simulate
            patient.simulate(n_time_steps)

            # store outputs of this simulation
            self.cohortOutcomes.extract_outcome(simulated_patient=patient)

        # calculate cohort outcomes
        self.cohortOutcomes.calculate_cohort_outcomes(initial_pop_size=self.popSize)


class CohortOutcomes:
    def __init__(self):

        self.survivalTimes = []
        self.costs = []  # patients' discounted costs
        self.utilities = []  # patients' discounted utilities
        self.nLivingPatients = None
        self.meanSurvivalTime = None
        self.statCost = None  # summary statistics for discounted cost
        self.statUtility = None  # summary statistics for discounted utility

    def extract_outcome(self, simulated_patient):

        if simulated_patient.stateMonitor.survivalTime is not None:
            self.survivalTimes.append(simulated_patient.stateMonitor.survivalTime)

        # discounted cost and discounted utility
        self.costs.append(simulated_patient.stateMonitor.costUtilityMonitor.totalDiscountedCost)
        self.utilities.append(simulated_patient.stateMonitor.costUtilityMonitor.totalDiscountedUtility)

    def calculate_cohort_outcomes(self, initial_pop_size):
        """ calculates the cohort outcomes
        :param initial_pop_size: initial population size
        """
        # summary statistics
        self.statSurvivalTime = stat.SummaryStat(
            name='Survival time', data=self.survivalTimes)
        self.statCost = stat.SummaryStat(
            name='Discounted cost', data=self.costs)
        self.statUtility = stat.SummaryStat(
            name='Discounted utility', data=self.utilities)
        # calculate mean survival time
        self.meanSurvivalTime = sum(self.survivalTimes) / len(self.survivalTimes)

        # survival curve
        self.nLivingPatients = PrevalencePathBatchUpdate(
            name='# of living patients',
            initial_size=initial_pop_size,
            times_of_changes=self.survivalTimes,
            increments=[-1]*len(self.survivalTimes)
        )
