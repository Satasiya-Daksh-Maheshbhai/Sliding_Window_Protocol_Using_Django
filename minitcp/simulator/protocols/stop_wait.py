def run_stop_and_wait(total_packets, loss_prob):

    lost_packets = round(total_packets * loss_prob)

    # Stop-and-Wait retransmits exactly the lost packets
    retransmissions = lost_packets

    total_transmissions = total_packets + retransmissions

    success_rate = (total_packets / total_transmissions) * 100
    throughput = total_packets / total_transmissions
    efficiency = success_rate

    return {
        "protocol": "Stop-and-Wait",
        "success": round(success_rate, 2),
        "retransmissions": retransmissions,
        "throughput": round(throughput, 2),
        "efficiency": round(efficiency, 2)
    }
