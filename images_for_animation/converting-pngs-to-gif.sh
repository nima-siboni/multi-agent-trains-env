#!/bin/bash

convert -delay 10 -loop 0 `ls -tr *png` animation.gif
