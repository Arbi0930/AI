#  Bayesian network
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.plots import DAG
model = BayesianModel([('C', 'S'), ('R', 'S'), ('S', 'W'), ('S', 'D')])


cpd_c = TabularCPD('C', 2, [[0.7], [0.3]])
cpd_r = TabularCPD('R', 2, [[0.8], [0.2]])
cpd_s = TabularCPD('S', 2, [[0.9, 0.6, 0.4, 0.1], [0.1, 0.4, 0.6, 0.9]],
                   evidence=['C', 'R'], evidence_card=[2, 2])
cpd_w = TabularCPD('W', 2, [[0.9, 0.2], [0.1, 0.8]], evidence=['S'], evidence_card=[2])
cpd_d = TabularCPD('D', 2, [[0.8, 0.1], [0.2, 0.9]], evidence=['S'], evidence_card=[2])


model.add_cpds(cpd_c, cpd_r, cpd_s, cpd_w, cpd_d)
DAG().plot(model)