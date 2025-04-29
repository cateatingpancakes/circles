Don't forget to make a virtual environment and/or install the `requirements.txt`, if you don't already have them.
# Sample outputs
To produce results for any dimension, run `any_dimension.py`. To produce 2D results, but with a visualization of the solution drawn in matplotlib, run `main.py`. Adjust the parameters as needed.
## 3 dimensions
The following was an output produced for `CIRCLE_NO=12` and `DIMENSION=3`.
```
Found best solution:
[ 2.26308577e-01 -2.93471028e-01 -1.96536493e+00  2.75454609e-01
 -1.65951657e+00  1.08172511e+00 -1.21036234e+00  1.56725720e+00
  2.80584967e-01 -1.53690125e+00  3.11397784e-01 -1.24135636e+00
 -1.87208852e+00 -3.23075633e-01  6.25225179e-01 -4.15306300e-01
  7.91557923e-04  1.95640460e+00  1.78824464e+00  4.88775836e-01
 -7.50520002e-01 -9.37269822e-01 -1.66647988e+00 -5.86830587e-01
  8.71122341e-02  1.56559469e+00 -1.24150170e+00  1.48747224e+00
  1.87276522e-02  1.33681587e+00  1.22684283e+00 -1.43380206e+00
 -6.62622886e-01  7.49570812e-01  1.74132992e+00  6.37113805e-01]
Iteration: 4/10, cost = 2.402591662697716e-06
```
The low cost suggests this is a solution.

For `CIRCLE_NO=13`, however, the following output was produced:
```
Found best solution:
[ 1.81117399e-01 -1.02009541e+00  1.71073282e+00 -1.80749372e+00
 -3.20606189e-01 -7.93836288e-01 -5.30798955e-01 -1.72758269e+00
 -8.56575851e-01  1.03187159e+00  6.45798219e-01  1.58688044e+00
 -1.31686393e+00  1.45746751e+00 -3.76414705e-01 -4.82817760e-01
  4.53928486e-01 -1.88701805e+00  1.03980535e+00 -7.39710864e-01
 -1.54001045e+00 -9.37449960e-01  9.19038196e-01  1.50882657e+00
  3.40398682e-01  1.92950847e+00  4.01406919e-01 -1.52330931e+00
 -8.72249417e-01  9.58497497e-01  1.07821391e+00 -1.67564803e+00
  1.72235639e-01  1.99952987e+00 -1.81307334e-03  4.33313944e-02
  1.11334408e+00  1.18373181e+00 -1.16586802e+00]
Iteration: 5/10, cost = 0.180959337731782
```
The high cost suggests that, no matter how much we run the gradient descent, there will be overlaps, so we are likely not to have any solutions for 13 circles.
## 2 dimensions
Here are some solutions with drawings for the simpler case `DIMENSION=2`.

![5 circles](https://github.com/cateatingpancakes/circles/blob/main/outputs/5circles.png)
This solution had 5 circles, and there seems to be space left over, so we should try more circles.

![6 circles](https://github.com/cateatingpancakes/circles/blob/main/outputs/6circles.png)
This solution has 6 circles, and it's the [optimal solution](https://en.wikipedia.org/wiki/Kissing_number#Known_greatest_kissing_numbers) for 2D.

![7 circles](https://github.com/cateatingpancakes/circles/blob/main/outputs/7circles.png)
The solution has 7 circles, and they overlap (`cost=0.48991`), so we should remove a circle.
