from models.modeling import run_model

# # run example(without pretrained model)
# hist = run_model('/home/yeeunlee/ssho/data/fdata')

# run example(with pretrained model.h5)
hist = run_model('./data/8_data', init_model=None)