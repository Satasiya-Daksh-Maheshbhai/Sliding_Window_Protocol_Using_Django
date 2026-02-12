import random

def is_packet_lost(loss_probability):
    return random.random() < loss_probability
