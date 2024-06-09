import Inputdata as data
import model_classes as model
import Early_Stage_param_classes as param
import Early_Stage_Support as support

# simulating mono therapy
# create a cohort
cohort_mono = model.Cohort(id=0,
                           pop_size=data.POP_SIZE,
                           parameters=param.Parameters(therapy=param.Therapies.MONO))
# simulate the cohort
cohort_mono.simulate(n_time_steps=data.SIM_TIME_STEPS)

# simulating therapy
# create a cohort
cohort_combo = model.Cohort(id=1,
                            pop_size=data.POP_SIZE,
                            parameters=param.Parameters(therapy=param.Therapies.COMBO))
# simulate the cohort
cohort_combo.simulate(n_time_steps=data.SIM_TIME_STEPS)

# print the estimates for the mean survival time
support.print_outcomes(sim_outcomes=cohort_mono.cohortOutcomes,
                       therapy_name=param.Therapies.MONO)
support.print_outcomes(sim_outcomes=cohort_combo.cohortOutcomes,
                       therapy_name=param.Therapies.COMBO)

# plot survival curves and histograms
support.plot_survival_curves_and_histograms(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                                            sim_outcomes_combo=cohort_combo.cohortOutcomes)


# print comparative outcomes
support.print_comparative_outcomes(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                                   sim_outcomes_combo=cohort_combo.cohortOutcomes)

# report the CEA results
support.report_CEA_CBA(sim_outcomes_mono=cohort_mono.cohortOutcomes,
                       sim_outcomes_combo=cohort_combo.cohortOutcomes)







#
# Transition probability matrix: [[0.5343634800000001, 0.46, 0, 0, 0, 0.010438], [0, 0.5343634800000001, 0.46, 0, 0, 0.010438], [0, 0, 0.28697298000000004, 0.71, 0, 0.010438], [0, 0, 0, 0.9892350142956522, 0.0003304347826086957, 0.010438], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
#
# Annual State Cost: [0, 16909, 600, 1000, 0, 0]
# Annual State Cost: [0, 48272, 600, 1000, 0, 0]
# Therapies.MONO
#   Estimate of mean survival time and 99% confidence interval: 22.88 (22.82, 22.94)
#   Estimate of discounted cost and 99% confidence interval: 49,621 (49,560, 49,681)
#   Estimate of discounted utility and 99% confidence interval: 15.90 (15.89, 15.91)
#
# Therapies.COMBO
#   Estimate of mean survival time and 99% confidence interval: 22.91 (22.85, 22.96)
#   Estimate of discounted cost and 99% confidence interval: 567,916 (566,984, 568,849)
#   Estimate of discounted utility and 99% confidence interval: 18.82 (18.81, 18.84)
#
# Increase in mean survival time and 99% confidence interval: 0.03 (-0.09, 0.15)
# Increase in mean discounted cost and 99% confidence interval: 518,295.75 (516,884.26, 519,707.25)
# Increase in mean discounted utility and 99% confidence interval: 2.92 (2.89, 2.95)Transition probability matrix: [[0.5343634800000001, 0.46, 0, 0, 0, 0.010438], [0, 0.5343634800000001, 0.46, 0, 0, 0.010438], [0, 0, 0.28697298000000004, 0.71, 0, 0.010438], [0, 0, 0, 0.9892350142956522, 0.0003304347826086957, 0.010438], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
#
# Annual State Cost: [0, 16909, 600, 1000, 0, 0]
# Annual State Cost: [0, 48272, 600, 1000, 0, 0]
# Therapies.MONO
#   Estimate of mean survival time and 99% confidence interval: 22.88 (22.82, 22.94)
#   Estimate of discounted cost and 99% confidence interval: 49,621 (49,560, 49,681)
#   Estimate of discounted utility and 99% confidence interval: 15.90 (15.89, 15.91)
#
# Therapies.COMBO
#   Estimate of mean survival time and 99% confidence interval: 22.91 (22.85, 22.96)
#   Estimate of discounted cost and 99% confidence interval: 567,916 (566,984, 568,849)
#   Estimate of discounted utility and 99% confidence interval: 18.82 (18.81, 18.84)
#
# Increase in mean survival time and 99% confidence interval: 0.03 (-0.09, 0.15)
# Increase in mean discounted cost and 99% confidence interval: 518,295.75 (516,884.26, 519,707.25)
# Increase in mean discounted utility and 99% confidence interval: 2.92 (2.89, 2.95)