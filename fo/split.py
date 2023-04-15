class SplitCommand:
    NAME = "split"
    HELP = "Split directory into smaller subdirectories"

    def prepare(self, parser):
        parser.add_argument("--source", required=True)
        parser.add_argument("--size", required=True)

    def execute(self, args):
        print(args)
