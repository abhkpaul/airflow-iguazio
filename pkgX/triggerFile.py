import mlrun as m

def triggerRuns():

    runFileA = m.new_function(
        name="runFileA",
        command="pkgA/runFileA.py testFuncA",
        kind="local"
    )
    runFileC = m.new_function(
        name="runFileC",
        command="pkgA/runFileB.py testFuncB",
        kind="local")

    runFileA.run()
    runFileC.run()


if __name__ == "__main__": triggerRuns()