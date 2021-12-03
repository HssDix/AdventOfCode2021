# %% read input
with open('diagnostic_input.txt', 'r') as f:
    diag_rep = f.readlines()

# %% Part One
diag_rep_bits = [[line[i]=='1' for line in diag_rep] for i in range(12)]

calculate_gamma_rate = \
    lambda diag_rep_bits: [sum(bit) >= len(bit)/2 for bit in diag_rep_bits]
calculate_epsilon_rate = \
    lambda diag_rep_bits: [sum(bit) < len(bit)/2 for bit in diag_rep_bits]

bitify = lambda array: ''.join(['1' if bl else '0' for bl in array])
gamma_rate_bin = bitify(calculate_gamma_rate(diag_rep_bits))
epsilon_rate_bin = bitify(calculate_epsilon_rate(diag_rep_bits))

gamma_rate = int(gamma_rate_bin, 2)
epsilon_rate = int(epsilon_rate_bin, 2)
power_consumption = gamma_rate * epsilon_rate

print(f'The power consumption is: {power_consumption}')

# %% Part Two

transpose = lambda matrix: \
    [[row[col_idx] for row in matrix] for col_idx in range(len(matrix[0]))]

def decode(diagnose, calculate_function):
    i = 0
    while len(diagnose)>1:
        gamma_rate = calculate_function(transpose(diagnose))
        diagnose = [line for line in diagnose  if line[i] == gamma_rate[i]]
        i += 1
    return bitify(diagnose[0])

oxygen_generator_rating_bin = decode(transpose(diag_rep_bits), calculate_gamma_rate)
CO2_scrubber_rating_bin = decode(transpose(diag_rep_bits), calculate_epsilon_rate)

oxygen_generator_rating = int(oxygen_generator_rating_bin, 2)
CO2_scrubber_rating = int(CO2_scrubber_rating_bin, 2)
life_support_rating = oxygen_generator_rating * CO2_scrubber_rating

print(f'The life support rating is: {life_support_rating}')
