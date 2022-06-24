# Summary

## Motivation

smap on RPI?

## Recommended Readings

## Requirements

Based on the current running sMAP server at EN 3088, we want to achieve the followings:

1. Deploy the following software/programs on Raspberry Pi (RPI)
2. smap stack (simple measurement and actuation profile with built-in databases)
   1. sources (twistd smap)
   2. ReadingDB
   3. powerdb2
   4. archiver (twistd smap-archiver)
3. Add customized control logic into sMap stack, such as GGMR/Adaptive learning written in python.
3. **Small form computer, no internet access**

## Known

1. The above requirements need to be installed on Ubuntu 14.04 Trusty (Linux Mint 17.1 Rebecca)
2. We need to find a way to install Ubuntu 14.04 Trusty on RPI. (**Almost impossible**)

## Alternatives/Workarounds

1. [Smap · PyPI](https://pypi.org/project/Smap/) 
   1. Deploy on RPI ✅
   2. sources (twistd smap)✅
   3. ReadingDB
   4. powerdb2
   5. archiver (twistd smap-archiver)
2. [BAC0 · PyPI](https://pypi.org/project/BAC0/)
   1. Deploy on RPI ✅
   2. Similar measurement and actuation logic as smap-stack.✅
   3. Need to configure databases✅
3. RPI+Amazon Web Services?
4. Does it have to be local machine?

## Closest state

Linux Mint Rebecca Cannot install pip -> OK ✅

Ubuntu 22.04 -> OK ✅
