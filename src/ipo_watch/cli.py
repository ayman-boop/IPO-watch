"""Command-line entry point: `ipo-watch <command>`."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="ipo-watch")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("poll-edgar", help="Check EDGAR for new IPO filings once")
    sub.add_parser("collect-signals", help="Run all external signal collectors once")
    sub.add_parser("build-features", help="Rebuild feature_snapshots for active deals")
    sub.add_parser("run", help="Start the scheduler")
    args = parser.parse_args()
    raise SystemExit(f"'{args.command}' is not implemented yet")


if __name__ == "__main__":
    main()
