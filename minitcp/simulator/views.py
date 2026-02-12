# from django.shortcuts import render
# from .protocols.stop_wait import run_stop_and_wait
# from .protocols.go_back_n import run_go_back_n
# from .protocols.selective_repeat import run_selective_repeat

# def index(request):
#     results = []

#     if request.method == "POST":
#         packets = int(request.POST.get("packets"))
#         loss = float(request.POST.get("loss")) / 100
#         window = int(request.POST.get("window"))

#         results.append(run_stop_and_wait(packets, loss))
#         results.append(run_go_back_n(packets, window, loss))
#         results.append(run_selective_repeat(packets, window, loss))

#     return render(request, "index.html", {"results": results})


from django.shortcuts import render
from .protocols.stop_wait import run_stop_and_wait
from .protocols.go_back_n import run_go_back_n
from .protocols.selective_repeat import run_selective_repeat


def index(request):

    context = {}

    if request.method == "POST":
        packets = int(request.POST.get("packets"))
        loss_input = float(request.POST.get("loss"))
        loss = loss_input / 100
        window = int(request.POST.get("window"))

        results = []

        results.append(run_stop_and_wait(packets, loss))
        results.append(run_go_back_n(packets, window, loss))
        results.append(run_selective_repeat(packets, window, loss))

        # Sort by efficiency (highest first)
        results = sorted(results, key=lambda x: x["efficiency"], reverse=True)

        context = {
            "packets": packets,
            "window": window,
            "loss": loss_input,
            "results": results
        }

    return render(request, "index.html", context)
