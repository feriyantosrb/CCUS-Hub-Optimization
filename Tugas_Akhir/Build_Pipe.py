import pandas as pd
import re

# Teks input
text = """
Optimal solution found (tolerance 1.00e-04)
Best objective 2.366637541571e+04, best bound 2.366637541571e+04, gap 0.0000%
arc:  ('TS38', 'source_2', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  1.2600000000001566
built:  1.0
weight:  5.88
crf:  0.1
duration:  30
transfer:  2.5720212268803198
build:  7.614395964000001
total:  10.18641719088032

arc:  ('TS22', 'source_3', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  2.7796089539003885
built:  1.0
weight:  7.91
crf:  0.1
duration:  30
transfer:  7.632852373392845
build:  10.243175523
total:  17.876027896392845

arc:  ('source_4', 'TS30', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  1.2600000000001566
built:  1.0
weight:  3.6
crf:  0.1
duration:  30
transfer:  1.5747068736001955
build:  4.661875080000001
total:  6.236581953600196

arc:  ('TS26', 'TS27', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.23470600684431814
built:  1.0
weight:  0.65
crf:  0.1
duration:  30
transfer:  0.05296198312707709
build:  0.8417274450000001
total:  0.8946894281270772

arc:  ('TS17', 'TS16', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.7687885544694415
built:  1.0
weight:  1.84
crf:  0.1
duration:  30
transfer:  0.49107905263782825
build:  2.3827361520000006
total:  2.873815204637829

arc:  ('source_6', 'TS21', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.24766489952099993
built:  1.0
weight:  38.74999999999996
crf:  0.1
duration:  30
transfer:  3.3316766447256163
build:  50.179905374999954
total:  53.51158201972557

arc:  ('source_8', 'TS4', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.8003318924616876
built:  1.0
weight:  6.85
crf:  0.1
duration:  30
transfer:  1.9032128980846343
build:  8.870512305
total:  10.773725203084634

arc:  ('TS27', 'TS13', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.23470600684431814
built:  1.0
weight:  13.350000000000003
crf:  0.1
duration:  30
transfer:  1.0877576534561222
build:  17.287786755000006
total:  18.37554440845613

arc:  ('source_8', 'sink_4', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.45966810753831194
built:  1.0
weight:  10.830000000000002
crf:  0.1
duration:  30
transfer:  1.7282219100133431
build:  14.024474199000004
total:  15.752696109013346

arc:  ('TS13', 'TS10', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.23470600684431814
built:  1.0
weight:  2.87
crf:  0.1
duration:  30
transfer:  0.23384752549955576
build:  3.716550411
total:  3.950397936499556

arc:  ('TS2', 'sink_6', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.29998803885903286
built:  1.0
weight:  4.279999999999999
crf:  0.1
duration:  30
transfer:  0.44573258612375677
build:  5.542451484
total:  5.988184070123757

arc:  ('TS3', 'TS2', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.29998803885903286
built:  1.0
weight:  14.800000000000008
crf:  0.1
duration:  30
transfer:  1.541318288465328
build:  19.165486440000016
total:  20.706804728465343

arc:  ('TS30', 'TS38', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  1.2600000000001566
built:  1.0
weight:  1.57
crf:  0.1
duration:  30
transfer:  0.6867471643200853
build:  2.0330955210000003
total:  2.719842685320086

arc:  ('source_5', 'TS26', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  1.0034945613137596
built:  1.0
weight:  4.25
crf:  0.1
duration:  30
transfer:  1.4805757449546348
build:  5.503602525000001
total:  6.9841782699546355

arc:  ('TS21', 'sink_8', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.24766489952099993
built:  1.0
weight:  2.3000000000000003
crf:  0.1
duration:  30
transfer:  0.19775112988048846
build:  2.978420190000001
total:  3.1761713198804893

arc:  ('TS39', 'TS31', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  4.709017698060208
built:  1.0
weight:  13.860000000000005
crf:  0.1
duration:  30
transfer:  22.657929974287242
build:  17.948219058000006
total:  40.60614903228725

arc:  ('TS31', 'sink_2', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  4.709017698060208
built:  1.0
weight:  7.36
crf:  0.1
duration:  30
transfer:  12.031916638582544
build:  9.530944608000002
total:  21.562861246582546

arc:  ('sink_2', 'TS29', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.2454694577786076
built:  1.0
weight:  23.220000000000013
crf:  0.1
duration:  30
transfer:  1.9787291695454832
build:  30.069094266000018
total:  32.0478234355455

arc:  ('source_3', 'TS18', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  4.219608953900389
built:  1.0
weight:  4.12
crf:  0.1
duration:  30
transfer:  6.035261587583227
build:  5.335257036000001
total:  11.370518623583227

arc:  ('source_7', 'TS25', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  6.7396089539003885
built:  1.0
weight:  36.44999999999997
crf:  0.1
duration:  30
transfer:  85.28230080870298
build:  47.20148518499996
total:  132.48378599370295

arc:  ('TS23', 'source_7', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  4.219608953900389
built:  1.0
weight:  34.689999999999976
crf:  0.1
duration:  30
transfer:  50.816316619723786
build:  44.92234625699997
total:  95.73866287672377

arc:  ('TS29', 'sink_9', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.24546945777850274
built:  1.0
weight:  1.3800000000000001
crf:  0.1
duration:  30
transfer:  0.11759889121324717
build:  1.7870521140000002
total:  1.9046510052132473

arc:  ('sink_3', 'TS1', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  5.933001440871646
built:  1.0
weight:  1.3800000000000001
crf:  0.1
duration:  30
transfer:  2.842367426593169
build:  1.7870521140000002
total:  4.629419540593169

arc:  ('TS16', 'sink_11', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.17202418705122688
built:  1.0
weight:  2.55
crf:  0.1
duration:  30
transfer:  0.15228473499257023
build:  3.3021615150000003
total:  3.4544462499925706

arc:  ('source_1', 'TS22', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  2.7796089539003885
built:  1.0
weight:  8.23
crf:  0.1
duration:  30
transfer:  7.941640332872707
build:  10.657564419000002
total:  18.59920475187271

arc:  ('TS18', 'TS23', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  4.219608953900389
built:  1.0
weight:  0.46
crf:  0.1
duration:  30
transfer:  0.6738398859923022
build:  0.5956840380000001
total:  1.2695239239923022

arc:  ('TS25', 'sink_3', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  6.7396089539003885
built:  1.0
weight:  2.3000000000000003
crf:  0.1
duration:  30
transfer:  5.381324879561511
build:  2.978420190000001
total:  8.359745069561512

arc:  ('sink_3', 'sink_5', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.32349712041743917
built:  1.0
weight:  6.36
crf:  0.1
duration:  30
transfer:  0.7142565178013458
build:  8.235979308000001
total:  8.950235825801347

arc:  ('TS16', 'TS15', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.5967643674182146
built:  1.0
weight:  0.46
crf:  0.1
duration:  30
transfer:  0.09529879135687577
build:  0.5956840380000001
total:  0.6909828293568759

arc:  ('TS11', 'TS9', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.5967643674182146
built:  1.0
weight:  8.5
crf:  0.1
duration:  30
transfer:  1.7609559272466173
build:  11.007205050000001
total:  12.76816097724662

arc:  ('TS15', 'TS11', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.5967643674182146
built:  1.0
weight:  18.840000000000003
crf:  0.1
duration:  30
transfer:  3.903107019920738
build:  24.397146252000006
total:  28.300253271920745

arc:  ('TS10', 'sink_10', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.23470600684431814
built:  1.0
weight:  2.55
crf:  0.1
duration:  30
transfer:  0.2077739338062255
build:  3.3021615150000003
total:  3.509935448806226

arc:  ('TS9', 'sink_7', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.5967643674182146
built:  1.0
weight:  3.68
crf:  0.1
duration:  30
transfer:  0.7623903308550062
build:  4.765472304000001
total:  5.5278626348550075

arc:  ('TS37', 'TS39', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  2.5490176980600516
built:  1.0
weight:  15.030000000000006
crf:  0.1
duration:  30
transfer:  13.30021032223327
build:  19.46332845900001
total:  32.76353878123328

arc:  ('source_6', 'source_1', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  1.0086266519604399
built:  1.0
weight:  38.17999999999996
crf:  0.1
duration:  30
transfer:  13.368818929445915
build:  49.44177515399994
total:  62.81059408344586

arc:  ('TS26', 'TS17', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.7687885544694415
built:  1.0
weight:  27.85000000000001
crf:  0.1
duration:  30
transfer:  7.432908486936697
build:  36.06478360500001
total:  43.497692091936706

arc:  ('sink_7', 'TS3', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.29998803885903286
built:  1.0
weight:  24.66000000000002
crf:  0.1
duration:  30
transfer:  2.568169526591554
build:  31.933844298000025
total:  34.50201382459158

arc:  ('TS1', 'sink_1', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  5.933001440871646
built:  1.0
weight:  93.59999999999974
crf:  0.1
duration:  30
transfer:  192.78666023849266
build:  121.20875207999967
total:  313.9954123184923

arc:  ('source_1', 'TS37', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  2.5490176980600516
built:  1.0
weight:  2.87
crf:  0.1
duration:  30
transfer:  2.53969418661407
build:  3.716550411
total:  6.25624459761407

arc:  ('source_2', 'TS39', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  2.1600000000001565
built:  1.0
weight:  2.55
crf:  0.1
duration:  30
transfer:  1.9121440608001383
build:  3.3021615150000003
total:  5.214305575800139

arc:  ('TS4', 'sink_1', 0)
slope:  0.1157192
intercept:  0.4316551
flow:  0.8003318924616876
built:  1.0
weight:  51.69999999999993
crf:  0.1
duration:  30
transfer:  14.364395157806639
build:  66.94970600999991
total:  81.31410116780656
"""

# Ekstrak data menggunakan regex
arc = re.findall(r"arc:\s+\(([^)]+)\)", text)
slope = re.findall(r"slope:\s+([0-9.]+)", text)
intercept = re.findall(r"intercept:\s+([0-9.]+)", text)
flow = re.findall(r"flow:\s+([0-9.]+)", text)
built = re.findall(r"built:\s+([0-9.]+)", text)
weight = re.findall(r"weight:\s+([0-9.]+)", text)
crf = re.findall(r"crf:\s+([0-9.]+)", text)
duration = re.findall(r"duration:\s+([0-9.]+)", text)
transfer = re.findall(r"transfer:\s+([0-9.]+)", text)
build = re.findall(r"build:\s+([0-9.]+)", text)
total = re.findall(r"total:\s+([0-9.]+)", text)

# Konversi nilai ke dalam float
slope = [float(value) for value in slope]
intercept = [float(value) for value in intercept]
flow = [float(value) for value in flow]
built = [float(value) for value in built]
weight = [float(value) for value in weight]
crf = [float(value) for value in crf]
duration = [float(value) for value in duration]
transfer = [float(value) for value in transfer]
build = [float(value) for value in build]
total = [float(value) for value in total]

# Buat DataFrame dengan kolom-kolom yang sesuai
df = pd.DataFrame({
    'arc': arc,
    'slope': slope,
    'intercept': intercept,
    'flow': flow,
    'built': built,
    'weight': weight,
    'crf': crf,
    'duration': duration,
    'transfer': transfer,
    'build': build,
    'total': total
})

# Simpan hasil ke dalam file Excel
output_file = 'build_values.xlsx'
df.to_excel(output_file, index=False)

output_file
