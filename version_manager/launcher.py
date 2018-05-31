import sys


print("Running on %s" % sys.version)


from version_manager.mainapp import main


def launch():
    main()


if __name__ == '__main__':
    launch()
