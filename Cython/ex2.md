Call C from Cython

- Expose a C library function: ```gsl::gsl_sf_bessel_J0```.
- Compile and link and C file

To test the C files, compile ```*.c``` as:
```
gcc list.c -o list
```

Compile the Cython code (See the link libraries!):
```
python ex2_setup.py build_ext --inplace
```

Run it:
```
python ex2_run.py
```
