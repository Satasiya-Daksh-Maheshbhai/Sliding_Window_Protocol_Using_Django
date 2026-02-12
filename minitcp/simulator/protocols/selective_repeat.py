def run_selective_repeat(total_packets, window_size, loss_prob):

    lost_packets = round(total_packets * loss_prob)

    # Selective Repeat retransmits ONLY lost packets
    retransmissions = lost_packets

    total_transmissions = total_packets + retransmissions

    success_rate = (total_packets / total_transmissions) * 100
    throughput = total_packets / total_transmissions
    efficiency = success_rate

    return {
        "protocol": "Selective Repeat",
        "success": round(success_rate, 2),
        "retransmissions": retransmissions,
        "throughput": round(throughput, 2),
        "efficiency": round(efficiency, 2)
    }
