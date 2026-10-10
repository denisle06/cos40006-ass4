"""Command-line tool that reports statistics about some text.

Usage:
    python textstats.py --text "hello world"
    python textstats.py --file notes.txt
    echo "hello world" | python textstats.py
"""
import argparse
import sys
from collections import Counter


def analyse(text, top):
    words = text.lower().split()
    cleaned = [w.strip(".,;:!?\"'()[]{}") for w in words]
    cleaned = [w for w in cleaned if w]
    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(text.splitlines()),
        "most common": Counter(cleaned).most_common(top),
    }


def main():
    parser = argparse.ArgumentParser(description="Count characters, words and lines in text.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--text", help="text to analyse")
    source.add_argument("--file", help="path to a text file to analyse")
    parser.add_argument("--top", type=int, default=3, help="how many common words to show (default 3)")
    args = parser.parse_args()

    if args.text is not None:
        text = args.text
    elif args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            sys.exit(f"error: cannot read {args.file}: {e.strerror}")
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("provide --text, --file, or pipe text via stdin")

    stats = analyse(text, args.top)
    print(f"Characters: {stats['characters']}")
    print(f"Words:      {stats['words']}")
    print(f"Lines:      {stats['lines']}")
    print("Most common words:")
    for word, count in stats["most common"]:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
