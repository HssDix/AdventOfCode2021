# %% read input
with open('sonar_sensory.txt', 'r') as f:
    sens = f.readlines()

# %% evaluate task 1
sens_num = [int(meas.replace('\n', '')) for meas in sens]
increments = [sens_num[i+1] - sens_num[i] for i in range(len(sens_num)-1)]

count_increments = lambda diffs: [dist>0 for dist in diffs]
incrs = count_increments(increments)

print('Sonar measurement depth increments: {}'.format(sum(incr)))

# %% evaluate task 2
increments_roll = [sens_num[i+3] - sens_num[i] for i in range(len(sens_num)-3)]
incrs_roll = count_increments(increments_roll)

print('Sonar measurement depth increments of rolling window: {}'.format(sum(incrs_roll)))
# %%
