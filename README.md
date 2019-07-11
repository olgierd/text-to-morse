# Gnuradio CW transmitter - morse encoder

This script allows you to use "Vector Source" block in Gnuradio as morse code transmitter.

Simply run `$ ./ttm.py "cq sn0abc"`.
`-.-. --.- / ... -. ----- .- -... -.-.
(1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1)
`

The first line of the output contains human-readable string of dots and dashes, the second one can be directly pasted into "Vector Source" block in Gnuradio.
