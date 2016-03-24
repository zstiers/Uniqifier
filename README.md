# Uniqifier
This is a simpler python tool designed to help dig up changed lines in large text-based files, particularly one's generated via SysInternal's string.exe. It takes in two files and outputs diffs that only contain real words. The reason it does this is so that human readable strings that get dumped into executables can be hard to find but are still there for people willing to go hunting.
This tool was not designed to be run without diffing so if you really want a full result then pass in an empty file for one of the files to diff.
