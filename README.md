# Towards Multiple References Era - Addressing Data Leakage and Limited Reference Diversity in NLG Evaluation
This is the repository for [Towards Multiple References Era - Addressing Data Leakage and Limited Reference Diversity in NLG Evaluation](https://arxiv.org/abs/2308.03131) by
Xianfeng Zeng, Yijin Liu, Fandong Meng and Jie Zhou.

This repository contains code to generate reference with chatgpt, and the references generated for WMT22 general translation by us are available for download [**here**](https://drive.google.com/file/d/1AYvhFYpqYJjpwHk_Q28-x-aezrTjtnEq/view?usp=drive_link).

To evaluate on your own result, please download the references and run the folloing command:
```
sh eval.sh ${PATH_TO_REFERENCE} ${PATH_TO_YOUR_RESULT} flores200
```

To generate references from chatgpt for your own data, please run the following command:
```
python chatgpt.py ${PATH_TO_SOURCE} ${PATH_TO_HUMAN_REFERENCE} ${PATH_TO_OUTPUT}
```

## Citation

If you find this useful in your research, please consider citing this repo and also the [paper](https://arxiv.org/abs/2308.03131):
	
    @article{zeng2023towards,
	  title={Towards Multiple References Era--Addressing Data Leakage and Limited Reference Diversity in NLG Evaluation},
	  author={Zeng, Xianfeng and Liu, Yijin and Meng, Fandong and Zho, Jie},
	  journal={arXiv preprint arXiv:2308.03131},
	  year={2023}
	}
