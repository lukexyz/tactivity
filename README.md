
## Setup develoment environment with `nbdev`

* Ubuntu / WSL
```
conda create -n tactivity python=3.9 jupyter twine
conda activate tactivity  
pip install nbdev
git clone https://github.com/lukexyz/tactivity.git  
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

### Nbdev commands  

#### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


#### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 
