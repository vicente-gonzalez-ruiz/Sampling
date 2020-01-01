#TMPs += rectangular.dat
rectangular.dat:	rectangular.py
			./rectangular.py
#TMPs += bartlett.dat
bartlett.dat:		bartlett.py
			./bartlett.py
#TMPs += hanning.dat
hanning.dat:		hanning.py
			./hanning.py

spectrum.dat:

TMPs += spectrum_rectangular.dat
spectrum_rectangular.dat:	rectangular.dat
				./spectrum.py rectangular
TMPs += spectrum_bartlett.dat
spectrum_bartlett.dat:		bartlett.dat
				./spectrum.py bartlett
TMPs += spectrum_hanning.dat
spectrum_hanning.dat:		hanning.dat
				./spectrum.py hanning

default:	rectangular.dat spectrum_rectangular.dat\
		bartlett.dat	spectrum_bartlett.dat\
		hanning.dat	spectrum_hanning.dat

include $(HOME)/Makefile_templates/Makefile

