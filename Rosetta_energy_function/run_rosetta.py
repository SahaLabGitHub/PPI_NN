# Importing required module
import subprocess
import glob
 
for pdbfile in glob.glob("*.pdb"): 
    pdbname = pdbfile.split('.')[0]
    subprocess.run(f'minimize.default.linuxgccrelease -s {pdbname}.pdb -run:min_type lbfgs_armijo_nonmonotone -run:min_tolerance 0.0001 -min_all_jumps true -use_input_sc true -ex1 -ex2 -extrachi_cutoff 1 -no_his_his_pairE true -no_optH false -ignore_unrecognized_res -overwrite -ndruns 5 -out:file:scorefile {pdbname}_min_score.json -out:file:scorefile_format json -out:path:all /home/uwm/fortierr/PPI/PDBbind_PP/twochains/min_pdb; rosetta_scripts.default.linuxgccrelease -s /home/uwm/fortierr/PPI/PDBbind_PP/twochains/min_pdb/{pdbname}_0001.pdb -parser:protocol interface_analysis.xml -ignore_unrecognized_res -no_his_his_pairE -out:file:score_only ifa.sc -no_optH false -ex1 -ex2 -use_input_sc -run:min_type lbfgs_armijo_nonmonotone -extrachi_cutoff 1 -linmem_ig 10 -atomic_burial_cutoff 0.01 -sasa_calculator_probe_radius 1.2 -out:file:scorefile_format json -out:path:all /home/uwm/fortierr/PPI/PDBbind_PP/twochains/IA -out:file:scorefile {pdbname}_IA_score.json',shell=True )
