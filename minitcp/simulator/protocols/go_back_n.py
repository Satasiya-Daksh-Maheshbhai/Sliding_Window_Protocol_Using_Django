def run_go_back_n(total_packets, window_size, loss_prob):

    lost_packets = round(total_packets * loss_prob)

    # In Go-Back-N, one loss causes retransmission of ~window_size packets
    retransmissions = lost_packets * window_size

    total_transmissions = total_packets + retransmissions

    success_rate = (total_packets / total_transmissions) * 100
    throughput = total_packets / total_transmissions
    efficiency = success_rate

    return {
        "protocol": "Go-Back-N",
        "success": round(success_rate, 2),
        "retransmissions": retransmissions,
        "throughput": round(throughput, 2),
        "efficiency": round(efficiency, 2)
    }
