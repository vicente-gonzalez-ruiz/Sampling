include $(HOME)/Makefile_templates/Makefile

rectangular.dat:	rectangular.py
			./rectangular.py
bartlett.dat:		bartlett.py
			./bartlett.py
hanning.dat:		hanning.py
			./hanning.py

spectrum_rectangular.dat:	rectangular.dat
				./spectrum.py rectangular
spectrum_bartlett.dat:		bartlett.dat
				./spectrum.py bartlett
spectrum_hanning.dat:		hanning.dat
				./spectrum.py hanning

default:	rectangular.dat spectrum_rectangular.dat\
		bartlett.dat	spectrum_bartlett.dat\
		hanning.dat	spectrum_hanning.dat

