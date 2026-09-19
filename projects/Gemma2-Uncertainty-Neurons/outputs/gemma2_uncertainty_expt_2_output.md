LogitVar - mean: 0.000004, std: 0.000001
Weight norms - mean: 0.332084, std: 0.050034
Null space fraction - mean: 0.113121, std: 0.047487
LayerNorm effect - mean: 0.012592, std: 0.033589

=== Uncertainty Neuron Candidates ===
Low LogitVar threshold: 0.000003
High weight norm threshold: 0.373571
High null space fraction threshold: 0.142683
Found 29 candidates (low LogitVar + high norm)
Found 8 strong candidates (+ high LayerNorm effect)

Top 5 strong candidate neurons:
  Neuron 1939: LogitVar=2.7109e-06, Weight norm=0.3819, Null space=0.1595, LayerNorm effect=0.0488
  Neuron 1974: LogitVar=1.8079e-06, Weight norm=0.3804, Null space=0.1470, LayerNorm effect=0.0790
  Neuron 2109: LogitVar=2.6296e-06, Weight norm=0.3746, Null space=0.1434, LayerNorm effect=0.0469
  Neuron 3461: LogitVar=2.2291e-06, Weight norm=0.3894, Null space=0.1460, LayerNorm effect=0.0627
  Neuron 6481: LogitVar=1.3609e-06, Weight norm=0.3870, Null space=0.1431, LayerNorm effect=0.0933

Testing neurons: [1939, 1974, 2109, 3461, 6481]

Mean entropy change: 0.0031
Mean loss change: -0.0172