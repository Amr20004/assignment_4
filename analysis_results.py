import _init_paths
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 8]

from lib.test.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from lib.test.evaluation import get_dataset, trackerlist

trackers = []
dataset_name = 'lasot' # choosen from 'uav', 'nfs', 'lasot_extension_subset', 'lasot'

# trackers.extend(trackerlist(name='seqtrack', parameter_name='seqtrack_b256', dataset_name=dataset_name,
#                             run_ids=None, display_name='seqtrack_b256'))
trackers.extend(trackerlist(name='seqtrack', parameter_name='my_lasot_2class_config', dataset_name=dataset_name,
                            run_ids=list(range(1, 21)), display_name='my_lasot_2class_config'))

dataset = get_dataset(dataset_name)

# print_results(trackers, dataset, dataset_name, merge_results=True, plot_types=('success', 'prec', 'norm_prec'),
#               force_evaluation=True)
print_results(trackers, dataset, dataset_name, merge_results=False, plot_types=('success', 'prec', 'norm_prec'),
              force_evaluation=True)
