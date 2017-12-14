#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('Sine wave plotting with matplotlib and numpy.')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(t, sin(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim((-2, 2))
ax1.set_ylabel('2 Hz')
l = ax2.set_xlabel('X-Axis Label')
l.set_color('g')
l.set_fontsize('large')

show()
