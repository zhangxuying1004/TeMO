# <p align="center"> <font color=#008000>TeMO</font>: Towards <font color=#FF0000>Te</font>xt-Driven 3D Stylization for <font color=#008000>M</font>ulti-<font color=#008000>O</font>bject Meshes </p>

####  <p align="center"> [Xuying Zhang](https://zhangxuying1004.github.io), [Bowen Yin](https://scholar.google.com/citations?hl=zh-CN&user=xr_FRrEAAAAJ), [Yuming Chen](https://scholar.google.com/citations?user=EweNbRAAAAAJ&hl=zh-CN), [Zheng Lin](https://scholar.google.com/citations?user=aCKl1R0AAAAJ&hl=zh-CN), [Yuheng Li](), [Qibin Hou](https://scholar.google.com/citations?user=fF8OFV8AAAAJ&hl=zh-CN), [Ming-Ming Cheng](https://scholar.google.com/citations?user=huWpVyEAAAAJ&hl=zh-CN)</p>

#### <p align="center"> [Paper Link](https://arxiv.org/pdf/2312.04248.pdf), accepted by <font color=#dd0000>CVPR 2024</font></p>


<table class="gif_table">
  <tbody>
    <tr>
     <td class="gif_td1"><img src="images/a-fire-dragon-an-ice-dragon.gif" width="180"/></td>
     <td class="gif_td2"><img src="images/A garfield cat and a brown horse.gif" width="180"/></td>
     <td class="gif_td3"><img src="images/a wicker vase and a candle in jeans.gif.gif" width="180"/></td>
     <td class="gif_td4"><img src="images/superman-ice-whale-fire-dragon.gif" width="180"/></td>
   </tr>
    <tr>
     <td class="gif_td1"><img src="images/A ginger cat is sitting on a grey leather sofa.gif" width="180"/></td>
     <td class="gif_td2"><img src="images/The batman is laying on a brick bed.gif" width="180"/></td>
     <td class="gif_td3"><img src="images/A brown squirrel is sitting on a bark chair.gif" width="180"/></td>
     <td class="gif_td4"><img src="images/A blue steel lamp and a cactus vase are placed on a wood table.gif" width="180"/></td>
   </tr>
  </tbody>
</table>

## 🛠️ Dependencies and Installation
```
conda env create --file temo.yml
conda activate temo
```
**Note1**: The below installation will fail if run on something other than a CUDA GPU machine. 
**Note2**: Installing clip by referring to [link](https://github.com/openai/CLIP.git).  
**Note3**: Installing kaolin by referring to [link](https://github.com/NVIDIAGameWorks/kaolin). If saying something like nvcc not found, you may need to set your CUDA_HOME environment variable to the 11.3 folder i.e. export CUDA_HOME=/usr/local/cuda-11.3, then retuning the installation.  
**Note4**: Installing Open3D by ```pip install open3d==0.14.1```.  

## 🤖 Training and Validation
1. Train: call the below shell scripts to generate example styles:
```
# a fire dragon and an ice dragon
./scripts/run_dual_dragon.sh
# A garfield cat and a brown horse
./scripts/run_cat_horse.sh
# ...
```

3. Validate: call the below shell scripts to generate gifs:
```
# a fire dragon and an ice dragon
./scripts/test_dual_dragon.sh
# A garfield cat and a brown horse
./scripts/test_cat_horse.sh
# ...
```

## 📖 Citation

If our work gives some inspiration to your research, please star this project and cite us. Thank you!

```
@article{zhang2023temo,
  title={TeMO: Towards Text-Driven 3D Stylization for Multi-Object Meshes},
  author={Zhang, Xuying and Yin, Bo-Wen and Chen, Yuming and Lin, Zheng and Li, Yunheng and Hou, Qibin and Cheng, Ming-Ming},
  journal={arXiv preprint arXiv:2312.04248},
  year={2023}
}
```
## 🤝 Acknowledgement
This repo is mainly built based on [TANGO](https://github.com/Gorilla-Lab-SCUT/tango), [Text2Mesh](https://github.com/threedle/text2mesh), and [X-Mesh](https://github.com/xmu-xiaoma666/X-Mesh). Thanks for their great work!
