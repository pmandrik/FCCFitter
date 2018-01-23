python python/significance_plot.py -f "Data/Zprime_ee_fcc_v0.json" -n "ee" -p ee
python python/significance_plot.py -f "Data/Zprime_mumu_fcc_v0.json" -n "mumu" -p mumu
python python/significance_plot.py -f "Data/Zprime_ll_fcc_v0.json" -n "ll" -p ll
python python/significance_plot.py -f "Data/Zprime_ee_fcc_v0.jsonData/Zprime_mumu_fcc_v0.json  Data/Zprime_ll_fcc_v0.json" -n "ee mumu ll" -p ll_comb
