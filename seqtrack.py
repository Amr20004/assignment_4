from lib.test.utils import TrackerParams
import os
from lib.test.evaluation.environment import env_settings
from lib.config.seqtrack.config import cfg, update_config_from_file


# def parameters(yaml_name: str):
def parameters(yaml_name: str, run_id: int):
    params = TrackerParams()
    prj_dir = env_settings().prj_dir
    save_dir = env_settings().save_dir
    # update default config from yaml file
    yaml_file = os.path.join(prj_dir, 'experiments/seqtrack/%s.yaml' % yaml_name)
    update_config_from_file(yaml_file)
    params.cfg = cfg
    print("test config: ", cfg)

    params.yaml_name = yaml_name
    # template and search region
    params.template_factor = cfg.TEST.TEMPLATE_FACTOR
    params.template_size = cfg.TEST.TEMPLATE_SIZE
    params.search_factor = cfg.TEST.SEARCH_FACTOR
    params.search_size = cfg.TEST.SEARCH_SIZE

    # # Network checkpoint path
    # params.checkpoint = os.path.join(save_dir, "checkpoints/train/seqtrack/%s/SEQTRACK_ep%04d.pth.tar" %
    #                                  (yaml_name, cfg.TEST.EPOCH))

    # --- YOUR MODIFICATION STARTS HERE ---

    # Network checkpoint path
    # Check if a specific run_id (epoch number) was passed from test.py
    if run_id is not None:
        # Use the run_id as the epoch number
        epoch_to_load = run_id
    else:
        # Fallback to the epoch specified in the yaml config file
        epoch_to_load = cfg.TEST.EPOCH

    # This line now dynamically loads the epoch based on the --runid
    # It will build your exact path:
    # D:/.../output/checkpoints/train/seqtrack/my_lasot_2class_config/SEQTRACK_epXXXX.pth.tar
    # Manually add the 'output' folder, since save_dir is the project root
    output_save_dir = os.path.join(save_dir, "output")
    params.checkpoint = os.path.join(output_save_dir, "checkpoints/train/seqtrack/%s/SEQTRACK_ep%04d.pth.tar" %
                                     (yaml_name, epoch_to_load))

    # --- YOUR MODIFICATION ENDS HERE ---

    # whether to save boxes from all queries
    params.save_all_boxes = False

    return params
