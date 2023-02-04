import retro
print("retro.__file__: ", retro.__file__)

env = retro.make(game='SuperMarioBros3-Nes', state='SuperMarioBros3.GrassLand.Level1')

env.reset()

while True:
    _obs, _rew, done, _info = env.step(env.action_space.sample())
    env.render()