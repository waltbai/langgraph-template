"""Command line interface."""

from dotenv import load_dotenv

from example.graph import graph


def main():
    """Main."""
    load_dotenv()
    agent = graph().compile()
    for chunk in agent.stream(
        input={},
        context={},
        stream_mode="updates",
    ):
        print(chunk)


if __name__ == "__main__":
    main()
