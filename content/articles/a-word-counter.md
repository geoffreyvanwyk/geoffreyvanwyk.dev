---
title: A Word Counter | Introduction
description: How to replicate the GNU wc (word counter) commandline utility programme using the Oclif commandline framework
author: Geoffrey van Wyk
image:
  src: ../word-tiles.jpg
  alt: pile of word tiles
tags:
  - tutorial
  - series
  - commandline
  - computer
  - programming
  - typescript
  - oclif
published: true
---

After having learned a programming language—such as [TypeScript](https://www.typescriptlang.org)—the computer programmer is ready to build a full-fledged programme in that language. Of the various platforms on which to build a programme, the commandline is the simplest, because its user interface is much simpler than graphical and web interfaces. Most of the programmer's time is spent on the business logic of turning inputs into outputs, instead of cumbersome user interface details.

When building a commandline programme, there are many aspects to consider before even starting on the business logic, such as how to:

- parse the arguments and options supplied to the command,
- build a multicommand program,
- format output,
- programmatically test the command,
- document the command's usage.

The purpose of a commandline framework—such as [Oclif](https://oclif.io)—is to solve all these issues for the programmer. Some programmers feel that they want to have a fundamental understanding, which means building the application from scratch. But, by using a framework, they can benefit from the experience of others and achieve their goal of a full-fledged programme in the newly-learned programming language much faster.

After having built the programme, they can study the framework's internals and even contribute new features. Ultimately, it may lead them to discover a more efficient approach that can lead to a better framework.

When learning a new framework, programmers sometimes make the mistake of first specifying a new program, then attempting to build it using the new framework. The quickest way is to implement an existing specification.

The specifications for commandline applications are conveniently recorded in their manual pages, accessed via the `man` command. The help screen for a command, displayed using the `--help` option, gives an even more succinct representation. The help screen for the GNU `wc` command is shown below.

```
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --help             display this help and exit
      --version          output version information and exit
```

The `wc` command can be used to count how many lines, words, bytes or characters a file contains. It has two forms of usage as shown at the top of the help screen. The forms of usage are distinguished from each other by the combination of options and arguments that can be used together. For the sake of simplicity, this tutorial only deals with the first form.

In the usage form `wc [OPTION]... [FILE]...`, the brackets mean the option or argument (in this case FILE) does not have to be supplied. The ellipsis `...` means more than one option or argument can be supplied. The `FILE` argument must be the file system path to the file. For the sake of simplicity, this tutorial assumes at least one FILE argument is required.

In this tutorial series, I will use Ubuntu 20.04. The reader can follow along on any operating system, but some of the installation instructions might differ. To follow along as closely as possible, rather use a virtual machine on Mac OS. On Windows, use either a virtual machine or [Windows Subsystem for Linux](https://aka.ms/wsl).

In the next article in this series, we will start with the installation of the prerequisites.
