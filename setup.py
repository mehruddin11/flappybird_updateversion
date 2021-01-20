import cx_Freeze
executables =[cx_Freeze.Executable("flappy bird.py")]
cx_Freeze.setup(
    name = "game",
    options = {"build_exe":
               {"packages":["pygame"],
                        "include_files":
                        ["background-day.png","base.png","blue-bird.png","gameover.jpg","pipe-red.png","hit.wav","wing.wav", "point.wav","image.png"]}},
    executables = executables
    )
