import math


# Mohamed Emad Mahmoud Hassan - 20190467
# Omnia Ehab Mohamed Ali - 20190108
# Nour eldin Raafat Foad - 20190588
# Menna-Allah Hamdy Mahmoud - 20190558

def MM1(arrival_rate, service_rate, npop):
    lmda = arrival_rate
    mue = service_rate
    P0 = 1-(lmda/mue)
    Pn = (1-(lmda/mue))*(lmda/mue) ** npop
    L = lmda*(mue-lmda)
    Lq = lmda ** 2/(mue*(mue-lmda))
    W = 1/(mue-lmda)
    Wq = lmda/(mue*(mue-lmda))
    Pw = lmda/mue
    utilization = lmda/mue
    print("Queuing Model: M/M/1")
    print("Lambda =", lmda)
    print("Mu =", mue)
    print("L =", L)
    print("Lq =", Lq)
    print("W =", W)
    print("Wq =", Wq)
    print("Pw =", Pw)
    print("p =", utilization)
    print("P0 =", P0)
    print("Pk =", Pn)


def MM_infinity(arrival_rate, service_rate, npop):
    lmda = arrival_rate
    mue = service_rate * npop
    L = lmda/mue
    W = 1/mue
    r = lmda/mue
    P0 = math.e ** (-r)
    Pn = ((r ** npop) * (math.e ** (-r)))/(math.factorial(npop))
    print("Queuing Model: M/M/∞")
    print("Lambda =", lmda)
    print("Mu =", mue)
    print("L =", L)
    print("W =", W)
    print("P0 =", P0)
    print("Pk =", Pn)


def MMC(lambda_, mu, c, n):
    summation = 0
    for i in range(c):
        summation += (1 / math.factorial(n)) * (lambda_ / mu) ** n
    P0 = 1 / (summation + (1 / math.factorial(c)) * ((lambda_ / mu) ** c) * (c * mu / (c * mu - lambda_)))
    if n <= c:
        Pn = (((lambda_ / mu) ** n) / math.factorial(n)) * P0
    else:
        Pn = (((lambda_ / mu) ** n) / (math.factorial(c) * c ** (n - c))) * P0
    L = ((((lambda_ / mu) ** c) * lambda_ * mu) / (math.factorial(c - 1) * (c * mu - lambda_) ** 2)) * P0 + (
                lambda_ / mu)
    Lq = ((((lambda_ / mu) ** c) * lambda_ * mu) / (math.factorial(c - 1) * (c * mu - lambda_) ** 2)) * P0
    W = ((((lambda_ / mu) ** c) * mu) / (math.factorial(c - 1) * (c * mu - lambda_) ** 2)) * P0 + (1 / mu)
    Wq = ((((lambda_ / mu) ** c) * mu) / (math.factorial(c - 1) * (c * mu - lambda_) ** 2)) * P0
    Pw = (1 / math.factorial(c)) * ((lambda_ / mu) ** c) * ((c * mu) / (c * mu - lambda_)) * P0
    p = lambda_ / (c * mu)
    print("Queuing Model: M/M/C")
    print("Lambda =", lambda_)
    print("Mu =", mu)
    print("L =", L)
    print("Lq =", Lq)
    print("W =", W)
    print("Wq =", Wq)
    print("Pw =", Pw)
    print("p =", p)
    print("P0 =", P0)
    print("Pk =", Pn)


def MM1K(lambda_, mu, k, n):
    if lambda_ == mu:
        P0 = 1 / (k + 1)
        Pn = 1 / (k + 1)
        L = k / 2
    else:
        P0 = (1 - (lambda_ / mu)) / (1 - (lambda_ / mu) ** (k + 1))
        Pn = P0 * (lambda_ / mu) ** n
        L = ((lambda_ / mu) / (1 - (lambda_ / mu))) - (
                    ((k + 1) * (lambda_ / mu) ** (k + 1)) / (1 - (lambda_ / mu) ** (k + 1)))
    Lq = L - (1 - P0)
    W = L / (lambda_ * (1 - (P0 * (lambda_ / mu) ** k)))
    Wq = Lq / (lambda_ * (1 - (P0 * (lambda_ / mu) ** k)))
    Pw = 1 - P0
    p = 1 - P0
    print("Queuing Model: M/M/1/k")
    print("Lambda =", lambda_)
    print("Mu =", mu)
    print("L =", L)
    print("Lq =", Lq)
    print("W =", W)
    print("Wq =", Wq)
    print("Pw =", Pw)
    print("ρ =", p)
    print("P0 =", P0)
    print("Pk =", Pn)


def MM1M(arrival_rate, service_rate, population_size, m):
    #  M|M|1|m model
    la = arrival_rate
    Mu = service_rate
    n = population_size

    # calculate Po
    # Po : the probability that all servers are idle
    summation = 0
    trails = int(m)
    for n in range(trails):
        summation += ((math.factorial(m)) / math.factorial(m - n)) * pow((la / Mu), n)
    Po = int(1 / summation)

    # calculate Pn
    if m >= n:
        Pn = (math.factorial(m) / math.factorial(m - n)) * pow((la / Mu), n) * Po
    while m <= n:
        n = int(input("enter the population size : "))
        m = int(input("enter the number of customers that can be served at the same time "))
        Pn = (math.factorial(m) / math.factorial(m - n)) * pow((la / Mu), n) * Po

    # performance measures

    # L : average number of customers in the system
    L = m - (Mu / la) * (1 - Po)

    # L(q) : average number of customers in the queue
    L_queuing = m - (((Mu + la) / la) * (1 - Po))

    # W : average waiting time in the system
    Waiting_time = L / (la * (m - L))

    # w(q) : average waiting time in the queue
    Waiting_time_queue = L_queuing / (la * (m - L))

    # Pw : the probability that an arriving customer will wait
    Pw = 1 - Po

    # ρ : overall system effective utilization factor
    p = 1 - Po

    print("Queuing Model: M/M/1/m")
    print("λK : ", la)
    print("μk : ", Mu)
    print("average number of customers in the system : ", L)
    print("average number of customers in the queue : ", L_queuing)
    print("average waiting time in the system : ", Waiting_time)
    print("average waiting time in the queue : ", Waiting_time_queue)
    print(" the probability that an arriving customer will wait : ", Pw)
    print("utilization factor : ", p)
    print("Po : ", Po)
    print("Pn : ", Pn)


print("Enter probability distribution of the arrivals: ")
lambda_ = float(input())
print("Enter probability distribution of the service time: ")
mu = float(input())
print("Enter number of servers (type 'inf' for infinity): ")
n_servers = input()
if n_servers != "inf":
    n_servers = int(n_servers)
print("Enter system capacity (type 'inf' for infinity): ")
system_capacity = input()
if system_capacity != "inf":
    system_capacity = int(system_capacity)
print("Enter population size: ")
pop_size = int(input())
print("Enter system discipline: ")
discipline = input()

if n_servers == 1 and system_capacity == "inf":
    print("Enter number of customers that a server can serve at a time: ")
    n_customers = int(input())
    if n_customers == 1:
        MM1(lambda_, mu, pop_size)
    else:
        MM1M(lambda_, mu, pop_size, n_customers)
elif n_servers == "inf" and system_capacity == "inf":
    MM_infinity(lambda_, mu, pop_size)
elif n_servers != "inf" and n_servers != 1 and system_capacity == "inf":
    MMC(lambda_, mu, n_servers, pop_size)
else:
    MM1K(lambda_, mu, system_capacity, pop_size)

