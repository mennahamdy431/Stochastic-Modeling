import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# mean arrival time can't be less than or equal mean service time
mean_of_arrival = float(input("Please enter the mean arrival time: "))
mean_of_service = float(input("Please enter the mean service time: "))


while(mean_of_arrival <= mean_of_service):
    print("mean arrival time can't be less than or equal mean service time\nplease re-enter")
    mean_of_arrival = float(input("Please enter the mean arrival time: "))
    mean_of_service = float(input("Please enter the mean service time: "))


arrivals = [np.random.poisson(mean_of_arrival) for i in range(1000000)]
service_time = [np.random.exponential(mean_of_service) for i in range(1000000)]
sns.histplot(x=arrivals, binwidth=1, color="lightsteelblue")
plt.title("Poisson distribution with mean "+str(mean_of_arrival), fontweight="bold",
          color="lightsteelblue", fontsize=24)
plt.show()
sns.histplot(x=service_time, color="lightsteelblue")
plt.title("Exponential distribution with mean "+str(mean_of_service), fontweight="bold",
          color="lightsteelblue", fontsize=24)
plt.show()
arrival_time = list(np.cumsum(arrivals))
waiting_time = []
start_time = []
completion_time = []
time_in_system = []
##################################################
waiting_time.append(0)
start_time.append(arrival_time[0])
completion_time.append(arrival_time[0]+service_time[0])
time_in_system.append(service_time[0])
##################################################
for i in range(1, 1000000):
    start_time.append(max(completion_time[i-1], arrival_time[i]))
    waiting_time.append(start_time[i] - arrival_time[i])
    completion_time.append(arrival_time[i] + waiting_time[i] + service_time[i])
    time_in_system.append(completion_time[i] - arrival_time[i])
##################################################
queue_lengths = []
for i in range(1000000):
    queue_len = 0
    for j in range(i+1, 1000000):
        if completion_time[i] > (arrival_time[j]):
            queue_len += 1
        else:
            queue_lengths.append(queue_len)
            break
##################################################
MM1 = pd.DataFrame({"IAT": arrivals, "arrival time": arrival_time, "waiting time": waiting_time,
                    "start time": start_time, "service time": service_time,
                    "completion time": completion_time, "time in system": time_in_system})
print("\n\n")
print(MM1.head(20))
print("\n\n")
print("average waiting time for an MM1 queue with:\naverage arrival time = "+str(
    mean_of_arrival)+"\naverage service time = "+str(mean_of_service)+"\nis "+str(
        np.mean(waiting_time)
))
print("\n")
print("average time in system for an MM1 queue with:\naverage arrival time = "+str(
    mean_of_arrival)+"\naverage service time = "+str(mean_of_service)+"\nis "+str(
        np.mean(time_in_system)
))
print("\n")
print("average queue length for an MM1 queue with:\naverage arrival time = "+str(
    mean_of_arrival)+"\naverage service time = "+str(mean_of_service)+"\nis "+str(
        np.mean(queue_lengths)
))
