from vyshkat.console import ConsoleApp
from vyshkat.container import build_container

if __name__ == "__main__":
    build_container().resolve(ConsoleApp).run()