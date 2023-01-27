import pickle
import numpy as np
import matplotlib.pyplot as plt


TASK = 4
FOLDER_RESULTS = f"Result/Task{TASK}/electra_base-fl/"

def _compute_mean_and_standard_deviation(values):
        mean = np.mean(values)
        standard_deviation = np.sqrt(np.sum((values-mean)**2)/len(values))
        return mean, standard_deviation
            
if __name__=='__main__':
    print(f"{FOLDER_RESULTS}")    
    with open(FOLDER_RESULTS + r"result_prob.pkl", "rb") as input_file:
        probs = pickle.load(input_file)

    with open(FOLDER_RESULTS + r"result_score.pkl", "rb") as input_file:
        scores = pickle.load(input_file)

    ece_scores = {s: t for s,t in [(k,v)  for k, v in scores.items()][:-1] if "ECE" in s}
    for conf, score in ece_scores.items():
        mean, std = _compute_mean_and_standard_deviation(np.array(score))
        print(f"{'/'.join(conf):>40}: {mean:2.4f} +- {std:2.4f}")
