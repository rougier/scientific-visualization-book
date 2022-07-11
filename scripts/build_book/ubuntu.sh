#!/usr/bin/env bash

if [[ $# -ne 4 ]]; then
    echo "Illegal number of parameters"
    exit 2
fi


start=$(date +%s)
ctan_url=$1
download_dir=$2
venv_dir=$3
project_dir=$4


echo "Install TeX Live (basic scheme)"
mkdir -p $download_dir
cd $download_dir
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xzvf install-tl-unx.tar.gz
cd install-tl-*/

export TEXLIVE_INSTALL_PREFIX=$HOME/texlive
export TEXLIVE_INSTALL_TEXDIR=$HOME/texlive
perl install-tl -scheme scheme-basic -portable -no-interaction -repository $ctan_url/systems/texlive/tlnet/ 

echo -e '\n#texlive\nexport PATH="$PATH:$HOME/texlive/bin/x86_64-linux"\n' >> ~/.bashrc
source ~/.bashrc


echo "Install additional TeX Live packages"
tlmgr install -repository $ctan_url/systems/texlive/tlnet/ latexmk ean13isbn ean ocr-b helvetic enumitem units emptypage biblatex quoting titlesec tocloft mdframed zref needspace biber xetex xcolor pdfpages hologo float pgf parskip fontspec microtype listings caption booktabs pdflscape


echo "Update OS package sources info"
sudo apt-get update


echo "Create virtual environment"
sudo apt-get -y install python3-pip python3-venv
mkdir -p $venv_dir
python3 -m venv $venv_dir/scientific-visualization-book
source $venv_dir/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install docutils==0.17


echo "Clone the repository"
sudo apt-get -y install git
mkdir -p $project_dir
cd $project_dir
git clone https://github.com/rougier/scientific-visualization-book
cd scientific-visualization-book


echo "Build the book"
make clean && make all


end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"
