# coding:utf-8

ENV_NAME = 'Breakout-v0'
NUM_THREADS = 8
FRAME_WIDTH = 84
FRAME_HEIGHT = 84
STATE_LENGTH = 4
GLOBAL_T_MAX = 100000000
LOCAL_T_MAX = 5
GAMMA = 0.99
ENTROPY_BETA = 0.01
INITIAL_LEARNING_RATE = 0.0007
RMSP_ALPHA = 0.99
RMSP_EPSILON = 0.1
NO_OP_STEPS = 30
CLIP_NORM = 40
SAVE_INTERVAL = 500000
LOG_INTERVAL = 10000
SAVE_NETWORK_PATH = 'saved_networks/' + ENV_NAME
SAVE_SUMMARY_PATH = 'summary/' + ENV_NAME
LOAD_NETWORK = False
DISPLAY = False
