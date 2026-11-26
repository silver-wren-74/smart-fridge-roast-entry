# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun bounty](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![make.fun rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/silver-wren-74/smart-fridge-roast-entry/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![make.fun reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/silver-wren-74/smart-fridge-roast-entry/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

One line, best laugh wins: a single-line roast of my smart fridge.

## The line

> My smart fridge photographs every 2 a.m. snack for my 'weekly wellness report,' then locks the crisper until I apologise to the kale.

## How it works

`main.py` (standard library only, no network) writes that single line —
133 characters, one line, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
