FROM ubuntu:22.04 AS herd7
LABEL "about"="Herdtools7 & tracesynth project env"

#ARG DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt update && apt-get install -y --no-install-recommends wget ca-certificates apt-utils


RUN apt-get update && apt-get install -y pkg-config

RUN apt-get update && apt install -y opam sudo libgmp-dev


RUN useradd --create-home --shell /bin/bash synth
# passwordless sudo access for ASAN and installing extra tools:
RUN echo "apr ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# RUN usermod -aG sudo fuzzer
USER root
WORKDIR /home/synth

#RUN opam update && opam install -y "herdtools7"

RUN sudo apt-get update && sudo apt-get install -y \
  m4 bubblewrap aspcud rsync curl git



RUN sudo apt install -y --no-install-recommends openssh-server nano



RUN curl -L https://mirror.racket-lang.org/installers/7.4/racket-7.4-x86_64-linux.sh -o racket.sh

WORKDIR /home/synth
RUN git clone https://github.com/rmculpepper/custom-load.git
RUN git clone https://github.com/tonyg/racket-rfc6455.git
RUN git clone https://github.com/emina/rosette.git
RUN git clone https://github.com/jamesbornholt/ocelot.git

#COPY racket-7.4-x86_64-linux.sh racket.sh

RUN chmod +x racket.sh && \
    ./racket.sh --in-place --dest /usr/racket && \
    ln -s /usr/racket/bin/* /usr/local/bin/ && \
    rm racket.sh

#RUN wget https://mirror.racket-lang.org/installers/8.2/racket-8.2-x86_64-linux.tar.gz&& \
#    tar -xzf racket-8.2-x86_64-linux.tar.gz&& \
#    cd racket-8.2-x86_64-linux&& \
#    sudo ./install.sh



ENV PATH="/usr/racket/bin:$PATH"


# RUN raco pkg config --set catalogs \
#     "https://pkgs.racket-lang.org" \
#     "https://download.racket-lang.org/releases/8.2/catalog/" && \
#     for i in 1 2 3; do raco pkg install --auto ocelot && break || sleep 5; done


# openssh-client
RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-client && \
    rm -rf /var/lib/apt/lists/*


# memsynth
WORKDIR /home/synth
RUN cd custom-load && \
    raco pkg install

WORKDIR /home/synth
RUN mv racket-rfc6455 rfc6455 && \
    cd rfc6455 && \
    raco pkg install

RUN apt-get update && apt-get install -y libcairo2 libpango1.0-0


WORKDIR /home/synth
RUN cd rosette && \
    git checkout 3.2 && \
    raco pkg install

WORKDIR /home/synth
RUN cd ocelot && \
    raco pkg install

ARG CACHEBUSTER=1

WORKDIR /home/synth

RUN git clone https://github.com/uwplse/memsynth.git
# COPY  memsynth-master memsynth


RUN apt-get update && apt-get install -y \
    python3 \
    python3-distutils \
    git \
    build-essential \
    cmake \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Z3Prover/z3.git /tmp/z3 \
    && cd /tmp/z3 \
    && git checkout z3-4.5.0 \
    && python3 scripts/mk_make.py --prefix=/opt/z3-4.5.0 \
    && cd build \
    && make -j$(nproc) \
    && make install \
    && rm -rf /tmp/z3

COPY run.sh /home/synth/memsynth/case-studies/synthesis/x86
COPY tso0-simple.rkt /home/synth/memsynth/case-studies/synthesis/x86
COPY tso0-unique-simple.rkt /home/synth/memsynth/case-studies/synthesis/x86
COPY tso0-unique.rkt /home/synth/memsynth/case-studies/synthesis/x86
COPY tso0.rkt /home/synth/memsynth/case-studies/synthesis/x86
COPY x86_simple.rkt /home/synth/memsynth/litmus/tests