import os 

samples = 1000
algorithms = ['rsa', 'dilithium2', 'dilithium3', 'dilithium4', 'falcon512', 'falcon1024', 'rsa3072_dilithium2', 'rsa3072_falcon512', 'p256_dilithium2', 'p256_falcon512', 'rsa3072_dilithium3', 'p256_dilithium3', 'p384_dilithium4', 'p521_falcon512']

for algorithm in algorithms:
    rsa_bits_array = [2048, 3072, 4096]

    if algorithm == 'rsa':
        for bits in rsa_bits_array:
            