function retval = rectangle_lw (n, b)

  if (nargin != 2)
    print_usage ();
  endif

  retval = zeros (n, 1);
  t = floor (1 / b);

  retval(1:t, 1) = ones (t, 1);

endfunction

function retval = triangle_lw (n, b)

  if (nargin != 2)
    print_usage ();
  endif

  retval = 1 - (0 : n-1)' * b;
  retval = max ([retval'; (zeros (1, n))])';

endfunction

% Ventana rectangular
w0 = [ zeros(1000,1); rectangle_lw(20, 1/20); zeros(1000,1) ];
W = fft(w0);
r = real(W);
i = imag(W);
spectrumH0 = log(1+sqrt((r .* r) + (i .* i)));

% Ventana de Hanning
w1 = [ zeros(1000,1); hanning(20); zeros(1000,1) ];
W = fft(w1);
r = real(W);
i = imag(W);
spectrumH1 = log(1+sqrt((r .* r) + (i .* i)));

% Ventana Triangular
w2 = w = [ zeros(1000,1); [0:0.1:0.9]'; triangle_lw(10,0.1); zeros(1000,1) ];
W = fft(w2);
r = real(W);
i = imag(W);
spectrumH2 = log(1+sqrt((r .* r) + (i .* i)));

todo = [spectrumH0, spectrumH1, spectrumH2];

save -ascii "espectro_ventanas.dat" todo

%__gnuplot_set__ terminal fig color textspecial
%__gnuplot_set__ noxtics
%__gnuplot_set__ noytics
%__gnuplot_set__ xlabel "w"
%__gnuplot_set__ ylabel "M\'odulo del Espectro"
%__gnuplot_set__ output "espectro_ventanas.fig"
%__gnuplot_plot__ [0:500] (spectrumH0) title "Rectangular", (spectrumH1) title "Hanning", (spectrumH2) title "Triangular"
