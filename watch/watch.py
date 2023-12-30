import sys
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match YouTube URLs in iframe src attributes
    pattern = r'<iframe .*?src="(https?://)?(www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"'

    match = re.search(pattern, s)

    if match:
        video_id = match.group(3)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
