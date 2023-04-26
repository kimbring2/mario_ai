# Introduction
Training a Deep Learning agent for the Super Mario Bros 3 game. This game is more challenging to the agent than [Sonic game](https://github.com/kimbring2/SonicTheHedgehog2-Tensorflow2) because it requires more complex movement and longer memory ability.

# Requirement
- OpenAI Gym 0.21.0 version
- Gym Retro: https://github.com/openai/retro
- ROM file of the Super Mario Bros. 3 (USA) (Rev A): https://wowroms.com/en/roms/nintendo-entertainment-system/super-mario-bros.-3/23771.html

| :warning: WARNING          |
|:---------------------------|
| There are various kind of ROM version for SMB3. Among them, you need to download the file which as the 'Rev A' tag in the name. Otherwise, Gym Retro can not import it. |

<img src="images/smb3_version.png" width="500">

After installing the Gym Retro and downloading the ROM file, please run the below command for importing the ROM into Gym Retro.

```
$ python -m retro.import /home/[your user name]/[rom_file_folder]
```

You should see the 'Imported 1 games' message to run the game. It says 'Imported 1 games' if there is some problem in your ROM file. 

<img src="images/retro_rom_import.png" width="500">


```
$ python -m retro.import /home/[your user name]/[rom_file_folder]
```

Next, you should copy the stage files into your Gym Retro installing location. Please run the below Python code to see the path.

```
$ import retro
$ retro.__file__
```

Move to data/stable/SuperMarioBros3-Nes folder of root path of the Gym Retro. Then, copy [all state files](https://github.com/kimbring2/mario_ai/tree/main/states) of this repositoty under that folder.

Your folder structure should looks like below image.

<img src="images/retro_folder_structure.png" width="500">

At last, you are ready to run the Super Mario Bros 3 at Gym Retro. Run below command, you can play the game as human agent.

```
$ python -m retro.examples.interactive --game SuperMarioBros3-Nes
```

You can play the game by the arrow keys, z, x key. 

<img src="images/smb3_state_1.gif" width="500">

If you want to run the specific level of game, run below command.

```
$ python -m retro.examples.interactive --game SuperMarioBros3-Nes --state SuperMarioBros3.DarkLand.Level1.state
```
