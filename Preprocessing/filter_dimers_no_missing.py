#from prody import *
import glob

import os
import shutil


count = 0
outfile465 = open('missingresidues.txt','w')
for pdbfile in glob.glob("*.pdb"):
    missing = False
    #print (pdbfile)
    thisfile = open(pdbfile,'r')
    for line in thisfile:
        #print (line)
        if 'REMARK 465' in line:
            #print (pdbfile + ":" + line)
            outfile465.write(pdbfile + ":" + line)
            missing = True
    if missing == True:
        count += 1
        pass
        #print (pdbfile)
        #print (count)
    missing = False

outfile465.write('total count: ' + count)

    

# with open('NonABChains.txt', 'r') as f:
#      for line in f:
#          name = line.strip()
#          cwd = os.getcwd()
#          src_path = os.path.join(cwd, name)
#          dst_path = os.path.join (cwd + '/NonAB/', name)
#          shutil.copy(src_path, dst_path)

# for pdbfile in glob.glob("*.pdb"):
#     pdbname = pdbfile.split('_')[0]
#     pdbname = pdbname + '.pdb'
#     cwd = os.getcwd()
#     src_path = os.path.join(cwd, pdbfile)
#     dst_path = os.path.join (cwd, pdbname)
#     shutil.copy(src_path, dst_path)

# with open('goodscores.txt', 'r') as f:
#      for line in f:
#          name = line.strip() + '.pdb'
#          print (name)
#          cwd = os.getcwd()
#          src_path = os.path.join(cwd, name)
#          dst_path = os.path.join (cwd + '/good/', name)
#          shutil.move(src_path, dst_path)

# with open('needclean.txt', 'r') as f:
#      for line in f:
#          name = line.strip() + '.pdb'
#          print (name)
#          cwd = os.getcwd()
#          src_path = os.path.join(cwd, name)
#          dst_path = os.path.join (cwd + '/needclean/', name)
#          shutil.move(src_path, dst_path)

# with open('goodscores.txt', 'r') as f:
#      for line in f:
#          name = line.strip() + '_IA_score.json'
#          print (name)
#          cwd = os.getcwd()
#          src_path = os.path.join(cwd, name)
#          dst_path = os.path.join (cwd + '/goodscores/', name)
#          shutil.move(src_path, dst_path)

#twochains = []
# for pdb in glob.glob("*.pdb"):
#     pdbfile = parsePDB(pdb)
#     if pdbfile.numChains() == 2:
#         twochains.append(pdb)

# print(twochains)
# with open('twochains.txt', 'w') as f:
#     for line in twochains:
#         f.write(f"{line}\n")

# with open('twochains.txt', 'r') as tc:
#     for linetc in tc:
#         match = False 
#         #print ('linetc' + linetc)
#         with open('proc.txt', 'r') as pr:
#             for linepr in pr:
#                 if linetc == linepr:
#                     match = True
#         if match == False:
#             print (linetc)

# with open('matches.txt', 'r') as f:
#     for line in f:
#         name = line.strip() + '.pdb'
#         print (name)
#         cwd = os.getcwd()
#         src_path = os.path.join(cwd, name)
#         dst_path = os.path.join (cwd + '/err/', name)
#         shutil.copy(src_path, dst_path)

# with open('twochains.txt', 'r') as pdblines:
#     for line in pdblines:
#         line = line.strip() + '.pdb'
#         print (line)
#         pdb = parsePDB(line)
#         hv = pdb.getHierView()
#         for chain in hv:
#             print (chain)
            
            

         
# with open('chainlist.txt', 'r') as chainlist:
#     for count, line in enumerate(chainlist):
#         pass
#     count += 1
#     count3 = int(count/3)
    
# print (count3)
    
    
# with open('chainlist.txt', 'r') as chainlist:
#     outfile= open('ABChains.txt', 'w')
#     for x in range(count3):
#         pdb = chainlist.readline()
#         chain1 = chainlist.readline()
#         chain2 = chainlist.readline()
#         pdb = pdb.strip()
#         chain1 = chain1.strip()
#         chain2 = chain2.strip()
#         if chain1 == "Chain A" and chain2 == "Chain B":
#             #print (pdb + ' normal chain')
#             outfile.write(f"{pdb}\n")
#         #else:
#             #print (pdb + ' error chain')

# with open('chainlist.txt', 'r') as chainlist:
#     outfile= open('NonABChains.txt', 'w')
#     for x in range(count3):
#         p = 0
#         pdb = chainlist.readline()
#         chain1 = chainlist.readline()
#         chain2 = chainlist.readline()
#         pdb = pdb.strip()
#         chain1 = chain1.strip()
#         chain2 = chain2.strip()
#         if chain1 == "Chain A" and chain2 == "Chain B":
#            p += p
#         else:
#             outfile.write(f"{pdb}\n")
#             #print (pdb + ' error chain')



#from prody import *
# import glob
# import os
# import shutil



# import subprocess
# import glob
# with open('chainlist.txt', 'r') as chainlist:
#      for count, line in enumerate(chainlist):
#          pass
#      count += 1
#      count3 = int(count/3)
    
# with open('chainlist.txt', 'r') as chainlist:
#     #outfile= open('NonABChains.txt', 'w')
#     for x in range(count3):
#         p = 0
#         pdb = chainlist.readline()
#         chain1 = chainlist.readline()
#         chain2 = chainlist.readline()
#         pdb = pdb.strip()
#         chain1 = chain1.strip()
#         chain2 = chain2.strip()
#         if chain1 == "Chain A" and chain2 == "Chain B":
#            p += p
#         else:
#             chain1 = chain1.split(' ')[1]
#             chain2 = chain2.split(' ')[1]
#             chains = chain1+chain2       
#             subprocess.run(f'python2.7 /home/uwm/fortierr/Downloads/rosetta_bin_linux_2021.16.61629_bundle/main/tools/protein_tools/scripts/clean_pdb.py {pdb} {chains}',shell=True )


# import subprocess
# import glob
# with open('chainlist.txt', 'r') as chainlist:
#      for count, line in enumerate(chainlist):
#          pass
#      count += 1
#      count3 = int(count/3)
    
# with open('chainlist.txt', 'r') as chainlist:
#     #outfile= open('NonABChains.txt', 'w')
#     for x in range(count3):
#         p = 0
#         pdb = chainlist.readline()
#         chain1 = chainlist.readline()
#         chain2 = chainlist.readline()
#         pdb = pdb.strip()
#         chain1 = chain1.strip()
#         chain2 = chain2.strip()
#         if chain1 == "Chain A" and chain2 == "Chain B":
#            p += p
#         else:
#             chain1 = chain1.split(' ')[1]
#             chain2 = chain2.split(' ')[1]
#             chains = chain1+chain2       
#             subprocess.run(f'python2.7 /home/uwm/fortierr/Downloads/rosetta_bin_linux_2021.16.61629_bundle/main/tools/protein_tools/scripts/clean_pdb.py {pdb} {chains}',shell=True )


# Run for NonAB Chains
# import glob
# import subprocess
# for pdbfile in glob.glob("*.pdb"):
#     pdbname = pdbfile.split('.')[0]
#     chains = pdbfile[5] + '_' + pdbfile[6]
#     subprocess.run(f'minimize.default.linuxgccrelease -s {pdbname}.pdb -run:min_type lbfgs_armijo_nonmonotone -run:min_tolerance 0.0001 -min_all_jumps true -use_input_sc true -ex1 -ex2 -extrachi_cutoff 1 -no_his_his_pairE true -no_optH false -ignore_unrecognized_res -overwrite -ndruns 5 -out:file:scorefile {pdbname}_min_score.json -out:file:scorefile_format json;rosetta_scripts.default.linuxgccrelease -s {pdbname}_0001.pdb -parser:protocol interface_analysis.xml -parser:script_vars interface={chains} -ignore_unrecognized_res -no_his_his_pairE -out:file:score_only ifa.sc -no_optH false -ex1 -ex2 -use_input_sc -run:min_type lbfgs_armijo_nonmonotone -extrachi_cutoff 1 -linmem_ig 10 -atomic_burial_cutoff 0.01 -sasa_calculator_probe_radius 1.2 -out:file:scorefile_format json -out:file:scorefile {pdbname}_IA_score.json',shell=True )


dimerscores = open('dimerscores.csv','r')
outfile = open('newscores.csv','w')
for scline in dimerscores:
    #print (scline)
    pdb1 = scline.split(',')[0]
    #print ('pdb1: ' + pdb1)
    kdlist = open('PP_Kd_index.csv', 'r')
    match = False
    for kdline in kdlist:
        pdb2,res,kd = kdline.split(',')
        if pdb1 == pdb2:
            #print (pdb1 + ' ' + pdb2 + ' ' + kd)
            match = True
            newline = scline.strip() + ',' + res + ',' + kd
            #print (scline)
            outfile.write(newline)
    kdlist.close()
    #         #print (newline)
    #         #outfile.write(newline)
outfile.close()
        
    