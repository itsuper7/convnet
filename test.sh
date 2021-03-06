#!/usr/bin/sh
## exp_name=JPS_act_12_exp_4_accv_fc_j0
## exp_name=JPS_act_14_exp_2_accv
## exp_name=JPS_act_12_exp_4_accv
## exp_name=JPS_act_3_exp_8_accv
## exp_name=JPS_act_12_exp_4_accv_half_fc_j2
## exp_name=ASM_act_4_exp_5
## exp_name=JointInd_act_14_exp_2
## exp_name=ASM_act_14_exp_2
## exp_name=ASM_act_12_exp_4
## exp_name=residual_act_4_exp_5
## exp_name=JPS_act_5_exp_10_accv_half2_fc_j2
## exp_name=JPS_act_12_exp_4_accv_finetune_fc_j2
# exp_name=JPS_H80K_All_exp_12
exp_name=ASM_act_12_exp_4

JT=t175
EP=200
BSIZE=1024
macid=13
## DP=croppedrelskelmixjtplus
## DP=croppedrelskelmixjtmultilabel
## DP=croppeddhmlperelskeljtdoublelind   
## DP=relskeljt
## DP=croppeddhmlperelskeljt
## DP=croppeddhmlpepairwisereljt
## DP=memfeat
## DP=croppedrelskelpairjt
## DP=memjtpredanglemix
## DP=memjtpredanglemix
## DP=memjtpredknnmixlind
## DP=memjtpredknnmix_t
## DP=memjtpredmix
## DP=memjtpredmix
## DP=memjtpredknnmix_t
DP=croppeddhmlperelskelrandpairjt
## DP=croppeddhmlperelskelrandjt
testfreq=15


## ASM)act_all_exptest_11
##
# TrainRange=0-0
# TestRange=0-911743

## pct       
# TrainRange=0-19999
# TestRange=20000-34526

## for HumanEva_exp_1
#Train [0, 18503)(18503), validate [18503, 35999)(17496), Test [35999, 100945)(64946)
# TrainRange=0-18502
# TestRange=18503-35998
## for HumanEva valid 
#Train [0, 14171)(14171), validate [14171, 28715)(14544), Test [28715, 93661)(64946)
# TrainRange=0-14170
# TestRange=14171-28714

# HumanEva_exp_t  FOR FULL EXPERIMENT, PAY ATTENTION######
# TrainRange=0-28714
# TestRange=14171-28714

## for exp 10  <---------------------------HERE HERE HERE
# TrainRange=0-72435
# TestRange=72436-103079

## for exp 10  Half 2 <---------------------------HERE HERE HERE
# TrainRange=0-72435
# TestRange=72436-103079

## for exp 9
# TrainRange=0-79411
# TestRange=79412-107715

## for exp 8 
# TrainRange=0-158787
# TestRange=158788-223031


# # for exp 7
# TrainRange=0-318215
# TestRange=318216-416107

# # for exp 6
# TrainRange=0-1559751
# TestRange=1559752-2103095

# for exp 5    
# TrainRange=0-109423
# TestRange=109424-148731

# # For exp 4
TrainRange=0-76047
TestRange=76048-105367

## For H80K_All
# TrainRange=0-51242
# TestRange=51243-74405



##################
# For exp 1-3
# TrainRange=0-132743
# TestRange=132744-162007


## TEMP USE! Never 
# echo ONLY FOR TEST
# TrainRange=0-90707
# TestRange=90708-105367


#################
run_mac=c8k${macid}

/usr/bin/python convnet.py --data-path=/opt/visal/tmp/for_sijin/Data/H36M/H36MExp/folder_${exp_name} --save-path=/opt/visal/tmp/for_sijin/Data/saved/Test/${run_mac} --train-range=${TrainRange} --test-range=${TestRange} --layer-def=/home/grads/sijinli2/Projects/DHMLPE/doc/netdef/dhmlpe-layer-def-${JT}.cfg --layer-params=/home/grads/sijinli2/Projects/DHMLPE/doc/netdef/dhmlpe-layer-params-${JT}.cfg --data-provider=${DP} --test-freq=${testfreq} --epoch=${EP} --mini=256 --batch-size=${BSIZE}
