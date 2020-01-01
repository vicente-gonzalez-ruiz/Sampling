function retval=rectangle_lw (n, b)
  retval = zeros (n, 1);
  t = floor (1 / b);
  retval(1:t, 1) = ones (t, 1);
endfunction

function retval = triangle_lw (n, b)

%  if (nargin != 2)
%    print_usage ();
%  endif

  retval = 1 - (0 : n-1)' * b;
  retval = max ([retval'; (zeros (1, n))])';

endfunction

% Ventana rectangular
w0 = [ (rectangle_lw (1000, 1/1000)) ];

% Ventana de Hanning
w1 = [ hanning(1000) ];

% Ventana Triangular
w2 = w = [ [0:1/500:1]'; triangle_lw(499,1/500) ];

todas = [ w0, w1, w2 ];

%save -ascii "rectangular-t.dat" w0
%save -ascii "Hanning-t.dat" w1
%save -ascii "triangular-t.dat" w2
save -ascii "ventanas.dat" todas
