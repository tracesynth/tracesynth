# Artifact Appendix

## Abstract

This artifact encompasses the complete implementation of TraceSynth, comprising the following core components:
(1) A delay injection algorithm designed to trigger specific final states in litmus tests;
(2) A memory model synthesis algorithm based on execution traces, coupled with a mechanism for directed test generation.

To ensure reproducibility, we provide a fully containerized environment alongside all raw data and scripts necessary to regenerate the experimental results presented in the paper. Specifically, the artifact includes convenience scripts for reproducing the following experiments:
(1) Evaluation of TraceSynth using execution traces generated from the [herd] and [qemu-riscv64] simulators, as well as the [U740] and [C910] processors;
(2) Evaluation of the delay injection algorithm on the [C910] hardware;
(3) Evaluation of the MemSynth experimental environment

We recommend executing the experiments on a recent Ubuntu distribution, equipped with Docker, Python 3, and bash. All experiments can be completed within one day on a typical workstation.


## Artifact Checklist

- **Programs:** TraceSynth
- **Run-time environment:** Linux (e.g., Ubuntu 22.04), Docker
- **Hardware Requirements:** At least 16GB of RAM, C910 development board (Optional)
- **Experiments:** Includes a litmus test suite and C910 execution logs for experimental replay

- **Output Artifacts:** The artifact generates textual output (.txt and .log files) and graphical figures.

- **Experiment Workflow:** All experiments are orchestrated using a combination of Bash and Python scripts.

- **Disk Space Requirements:** The Docker image requires approximately 6 GB of disk space.

- **Execution Time (Approximate):** The execution time is approximately 5 hours for TraceSynth and 5 hours for MemSynth.

- **Public Availability:** Yes.

- **License**: MIT License.

- **Archived**: Yes. The artifact is archived and permanently available via the following:
        https://doi.org/10.5281/zenodo.16758525


## Description

### How to access

Via the github link(https://github.com/tracesynth/tracesynth.git) or doi(https://doi.org/10.5281/zenodo.16758525).

### Hardware Dependencies

Although some experiments utilize data originally obtained from a C910 development board, we provide comprehensive pre-collected execution logs, enabling full reproduction without requiring access to the physical hardware. Additionally, for partial experiments requiring execution on real hardware, we offer optional support for running on a C910 device.


### Software Dependencies

- A Linux distribution (e.g., Ubuntu 22.04)
- Docker


### Installation

To set up the environment, run the following command:


```
docker load -i tracesynth.tar
docker run -it tracesynth /bin/bash
```

Alternatively, the image can be built from a Dockerfile:

```
cd docker 
docker build -t tracesynth .
```



### Experimental Procedure

After installation, the following commands should be executed to initialize the experimental environment:

```
conda init  
exec bash  
conda activate tracesynth
```



The experiments can be run using provided scripts. To reproduce all experiments related to TraceSynth, execute:

```
cd /home/synth/tracesynth/tests/experiment  
./run.sh  
```

We also provide a script for Experiment 1 on C910 hardware, which can be executed as follows:

```
./run_with_C910.sh hostname port username password hostpath
```


For experiments related to MemSynth, execute the following commands:

```
docker load -i memsynth.tar
docker run -it memsynth /bin/bash
export PATH=/opt/z3-4.5.0/bin:$PATH
export LD_LIBRARY_PATH=/opt/z3-4.5.0/lib:$LD_LIBRARY_PATH
cd /home/synth/memsynth/case-studies/synthesis/x86
./run.sh
```



### Expected Results

For TraceSynth, all experimental results are stored in:

```
/home/synth/tracesynth/tests/results
```



For MemSynth, all experimental results are stored in:


```
/home/synth/memsynth/case-studies/synthesis/x86
```


