import threading
import time
import random

class Nood_e(threading.Thread):
    def __init__(self, node_id, total_nodes):
        super(Nood_e, self).__init__()
        # node id
        self.nod_idtfn = node_id
        # total number of nodes
        self.tot_node = total_nodes
        # next node
        self.neghbr = (node_id + 1) % total_nodes
        # election flag
        self.flag_electn = False
        # leader id
        self.lead_idtfn = None

    def run(self):
        # Showcasing delays which are random
        time.sleep(random.uniform(1, 3))
        if self.nod_idtfn == 0:
            self.begin_electn()

    def begin_electn(self):
        self.flag_electn = True
        # In the beginning value of leader_id set to own node_id initially
        self.lead_idtfn = self.nod_idtfn
        print(f"Node {self.nod_idtfn} has started election.")
        self.elctn_notif()

    # Function to send the message of election
    def elctn_notif(self):
        print(f"Node {self.nod_idtfn} has sent election message to Node {self.neghbr}.")
        time.sleep(1)
        self.neighbor_node().receive_elctn_notif(self.nod_idtfn, self.lead_idtfn)

    # Function to receive the message of election
    def receive_elctn_notif(self, send_idtfn, send_leader_idtfn):
        # In case not already participating in election
        if not self.flag_electn:
            print(f"Node {self.nod_idtfn} has received election message from Node {send_idtfn}. ")
            if send_leader_idtfn is not None and (self.lead_idtfn is None or send_leader_idtfn > self.lead_idtfn):
                self.lead_idtfn = send_leader_idtfn
                print(f"Node {self.nod_idtfn} is now participating in election, the lead_idtfn updated to {send_leader_idtfn}. ")
                # Now start participating in election
                self.begin_electn()
            else:
                print(f"Node {self.nod_idtfn} received lower / None lead_idtfn thus election message ignored. ")
        else:
            print(f"Node {self.nod_idtfn} has received election message but not participating in election.")


    def neighbor_node(self):
        return nod_e[self.neghbr]

# Keeping track of Number of nodes
no__nodes = 5

# Creation of nodes
nod_e = [Nood_e(i, no__nodes) for i in range(no__nodes)]

# Initiation of threads
for node in nod_e:
    node.start()

# Joining the threads
for node in nod_e:
    node.join()

# Here we will figure out the leader
def display_election_result(nod_e):
    # figure out the leader
    lea_der = max(nod_e, key=lambda x: x.lead_idtfn)
    print(f"\nHurray! The elections are concluded.")
    print(f"The elected Leader is: Node {lea_der.lead_idtfn}")

# Now calling function to display results of election
display_election_result(nod_e)


