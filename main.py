from ssho.ssho-item-tagging-api.models.modeling import run_model

# # run example(without pretrained model)
# hist = run_model('/home/yeeunlee/ssho/data/fdata')

# run example(with pretrained model.h5)
hist = run_model('./data/dataset', init_model='model.h5')