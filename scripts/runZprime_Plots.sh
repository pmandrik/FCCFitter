python python/limitplot.py -f "Outputs/fcc_v02/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_fcc_v02" -p "Z\' \rightarrow \mu\mu~~FCC" -s "pp_Zprime_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_fcc_v02" -p "Z\' \rightarrow ee~~FCC" -s "pp_Zprime_VALUETeV_ll"
python python/limitplot.py -f "Outputs/fcc_v02/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v02" -p "Z\' \rightarrow ll~~FCC" -s "pp_Zprime_VALUETeV_ll"

#python python/limitplot.py -f "Outputs/combined_fcc_v01/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_fcc_v01" -p "Z\' \rightarrow ll~~FCC" -s "pp_Zprime_VALUETeV_ll"

#python python/limitplot.py -f "Outputs/cms/Zprime/ee/Zprime_ee_*TeV/Limits/*" -n "Zprime_ee_cms" -p "Z\' \rightarrow ee~~CMS" -s "pp_Zprime_VALUETeV_ll"
#python python/limitplot.py -f "Outputs/cms/Zprime/mumu/Zprime_mumu_*TeV/Limits/*" -n "Zprime_mumu_cms" -p "Z\' \rightarrow \mu\mu~~CMS" -s "pp_Zprime_VALUETeV_ll"
#python python/limitplot.py -f "Outputs/combined_cms/Zprime/ll/Zprime_ll*TeV/Limits/*" -n "Zprime_ll_cms" -p "Z\' \rightarrow ll~~CMS" -s "pp_Zprime_VALUETeV_ll"

#python limitplot.py -f "Zprime_ll_*TeV/Limits/*" -n "Zprime_ll_fcc_v01" -p "Z\' \rightarrow ll"


python python/limitplot.py -f "Outputs/fcc_v02/Zprime/tt/Zprime_tt_*TeV/Limits/*" -n "Zprime_tt_fcc_v02" -p "Z\' \rightarrow #bar{t} t~~FCC" -s "pp_Zprime_VALUETeV_ttbar"
python python/limitplot.py -f "Outputs/fcc_v02/RSG/ww/RSG_ww_*TeV/Limits/*" -n "RSG_ww_fcc_v02" -p "RSG' \rightarrow WW~~FCC" -s "pp_RSGraviton_VALUETeV_ww"
