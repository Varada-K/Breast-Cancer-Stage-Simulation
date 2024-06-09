import Inputdata as data
import model_classes as model
import LA_Stage_param_classes as param
import LA_Stage_Support as support

# simulating no therapy
# create a cohort
cohort_no = model.Cohort(id=0,
                           pop_size=data.POP_SIZE,
                           parameters=param.Parameters(therapy=param.Therapies.MONO))
# simulate the cohort
cohort_no.simulate(n_time_steps=data.SIM_TIME_STEPS)

# simulating therapy
# create a cohort
cohort_therapy = model.Cohort(id=1,
                            pop_size=data.POP_SIZE,
                            parameters=param.Parameters(therapy=param.Therapies.COMBO))
# simulate the cohort
cohort_therapy.simulate(n_time_steps=data.SIM_TIME_STEPS)

# print the estimates for the mean survival time and mean time to AIDS
support.print_outcomes(sim_outcomes=cohort_no.cohortOutcomes,
                       therapy_name=param.Therapies.MONO)
support.print_outcomes(sim_outcomes=cohort_therapy.cohortOutcomes,
                       therapy_name=param.Therapies.COMBO)

# plot survival curves and histograms
support.plot_survival_curves_and_histograms(sim_outcomes_mono=cohort_no.cohortOutcomes,
                                            sim_outcomes_combo=cohort_therapy.cohortOutcomes)


# print comparative outcomes
support.print_comparative_outcomes(sim_outcomes_mono=cohort_no.cohortOutcomes,
                                   sim_outcomes_combo=cohort_therapy.cohortOutcomes)

# report the CEA results
support.report_CEA_CBA(sim_outcomes_mono=cohort_no.cohortOutcomes,
                       sim_outcomes_combo=cohort_therapy.cohortOutcomes)



