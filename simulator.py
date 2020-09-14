import numpy as np
from environment import Environment

# seeding the random generator
np.random.seed(1)

env = Environment(ls1=10,
                  lc=10,
                  ls2=10,
                  nr_agents=4,
                  states=[0.0, 1.0, 0.0, 10.0, 0.0, 3.0, 0., 200.],
                  time_cost=1,
                  destinations=[29.0, 29.0, 25.0, 29.0],
                  conflict_cost=100.0,
                  nr_actions=2)

terminated = False

while not terminated:
    actions_lst = np.random.randint(low=0, high=env.nr_actions, size=(env.nr_agents))
    _, _, terminated_lst, _ = env.step(actions_lst)
    env.render('images_for_animation')
    terminated = terminated_lst.all()
