Total number of neurons: 9216 Candidate uncertainty neurons: 29 === Top 29 Candidate Neuron Details === Neuron 128: LogitVar=2.7168e-06, Weight norm=0.3749, Projection norm=7.5957 Neuron 965: LogitVar=2.9987e-06, Weight norm=0.3746, Projection norm=6.9326 Neuron 1064: LogitVar=2.4596e-06, Weight norm=0.3740, Projection norm=7.9744 Neuron 1689: LogitVar=2.9800e-06, Weight norm=0.3849, Projection norm=7.2090 Neuron 1939: LogitVar=2.7109e-06, Weight norm=0.3819, Projection norm=8.2010 Neuron 1974: LogitVar=1.8079e-06, Weight norm=0.3804, Projection norm=11.7652 Neuron 2058: LogitVar=2.8152e-06, Weight norm=0.3798, Projection norm=7.3561 Neuron 2109: LogitVar=2.6296e-06, Weight norm=0.3746, Projection norm=7.5450 Neuron 2181: LogitVar=2.9502e-06, Weight norm=0.3828, Projection norm=8.2366 Neuron 2656: LogitVar=2.0785e-06, Weight norm=0.4504, Projection norm=12.3741 Neuron 2928: LogitVar=2.1863e-06, Weight norm=0.3940, Projection norm=10.4847 Neuron 3461: LogitVar=2.2291e-06, Weight norm=0.3894, Projection norm=9.5513 Neuron 5002: LogitVar=2.8972e-06, Weight norm=0.3741, Projection norm=7.1418 Neuron 5076: LogitVar=2.9435e-06, Weight norm=0.3751, Projection norm=7.0612 Neuron 5252: LogitVar=2.7797e-06, Weight norm=0.3746, Projection norm=7.3431 Neuron 5255: LogitVar=2.9615e-06, Weight norm=0.3746, Projection norm=6.9586 Neuron 5430: LogitVar=2.5580e-06, Weight norm=0.4415, Projection norm=10.7516 Neuron 5807: LogitVar=2.8230e-06, Weight norm=0.3779, Projection norm=7.2902 Neuron 5974: LogitVar=2.7327e-06, Weight norm=0.3766, Projection norm=7.3155 Neuron 6053: LogitVar=2.6743e-06, Weight norm=0.3882, Projection norm=8.9018
...
 Selecting top 5 neurons for further validation: [128, 965, 1064, 1689, 1939]

--- [LOW_UNCERTAINTY] 'One meter equals one hundred' ---
基线熵: 1.7959
零化熵: 1.8193 (Δ: +0.0234)
均值熵: 1.7998 (Δ: +0.0039)
Top-3预测: centimeters | millimeters | and
✅ Experiment completed! Tested 51 sentences
=== Results Analysis by Uncertainty Type ===
📊 EPISTEMIC (12 samples)
   Baseline entropy: 3.1203 ± 1.3983
   Zero intervention effect: -0.0034 ± 0.0070
   Mean intervention effect: -0.0007 ± 0.0069
   Proportion with zero intervention increasing entropy: 41.7%
   Proportion with mean intervention increasing entropy: 50.0%
📊 ALEATORIC (16 samples)
   Baseline entropy: 3.0936 ± 0.7819
   Zero intervention effect: -0.0018 ± 0.0051
   Mean intervention effect: -0.0008 ± 0.0022
   Proportion with zero intervention increasing entropy: 18.8%
   Proportion with mean intervention increasing entropy: 18.8%
📊 LINGUISTIC (14 samples)
   Baseline entropy: 2.9932 ± 0.5849
   Zero intervention effect: 0.0010 ± 0.0048
   Mean intervention effect: 0.0013 ± 0.0037
   Proportion with zero intervention increasing entropy: 71.4%
   Proportion with mean intervention increasing entropy: 57.1%
📊 LOW UNCERTAINTY (9 samples)
   Baseline entropy: 2.0993 ± 1.2471
   Zero intervention effect: 0.0089 ± 0.0124
   Mean intervention effect: 0.0038 ± 0.0063
   Proportion with zero intervention increasing entropy: 66.7%
   Proportion with mean intervention increasing entropy: 44.4%

Overall intervention effects:
  Zero intervention average effect: 0.0005
  Mean intervention average effect: 0.0006
The uncertainty role of neurons [128, 965, 1064, 1689, 1939] is not obvious