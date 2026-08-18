[![Contributors](https://img.shields.io/github/contributors/bgzo-sandbox/make-vxna-great-again.svg?style=for-the-badge)](https://github.com/bgzo-sandbox/make-vxna-great-again/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/bgzo-sandbox/make-vxna-great-again.svg?style=for-the-badge)](https://github.com/bgzo-sandbox/make-vxna-great-again/network/members)
[![Stargazers](https://img.shields.io/github/stars/bgzo-sandbox/make-vxna-great-again.svg?style=for-the-badge)](https://github.com/bgzo-sandbox/make-vxna-great-again/stargazers)
[![Issues](https://img.shields.io/github/issues/bgzo-sandbox/make-vxna-great-again.svg?style=for-the-badge)](https://github.com/bgzo-sandbox/make-vxna-great-again/issues)
[![Licence](https://img.shields.io/github/license/bgzo-sandbox/make-vxna-great-again.svg?style=for-the-badge)](https://github.com/bgzo-sandbox/make-vxna-great-again/blob/template/LICENCE)
[![Telegram](https://img.shields.io/badge/-telegram-black.svg?style=for-the-badge&logo=telegram&colorB=555)](https://t.me/imbGZo)


# VXNA Alternatives

This is a replacement for https://www.v2ex.com/xna, for the following reasons:

1. No censor, or small censor;
2. More open, more transparent;

The latest blog collected by v2ex is https://www.v2ex.com/xna/s/543, yet the public index (https://www.v2ex.com/xna) only shows `472` entries. The 71 missing blogs — removed for unknown reasons — are exactly why this project exists.

Latest source pull status: see [docs/status/latest-fetch-status.md](docs/status/latest-fetch-status.md).
This page is overwritten on each fetch run and only keeps the latest execution result.

Blocked sources are configured in [config/block.yaml](config/block.yaml).
Use `blocked_root_domains` with website root domains such as `example.com`.
Blocked domains are skipped during fetch and excluded from README and status output.


## Last Week Blog

| Date | Title | Summary |
| --- | --- | --- |
| 2026-08-18 | [Sweep LLM 功耗控制调度策略研究(一)](https://eduardoqian.com/archives/sweep-llm-gong-hao-kong-zhi-diao-du-ce-lue-yan-jiu-yi) | 8月份了，趁着开学之前，抽时间整理一下暑假做的Reasearch Assistant的工作内容整理。 研究内容 现状 项目主要是基于博士后做的SWEEP-LLM runtime 调度器的进一步扩展。这个调度器尝试解决的问题是在PD分离的异构GPU混合集群上，调度传入请求，使请求能够在满足TTFT/T |
| 2026-08-18 | [不该露怯的人](https://blog.solazy.me/20260818/) | 今天想聊聊「露怯」这个词 |
| 2026-08-18 | [SeeDNorm: Self-Rescaled Dynamic Normalization](https://mer.run/posts/seednorm-self-rescaled-dynamic-normalization/) | 有实验有理论，主要是想把RMSNorm丢掉的长度信息用温和的方式补充回去，看起来效果也还可以。实验里面有小模型测试的东西，之后可以学一下他们的setup。另外里面关于方差的一些分析感觉可以挪用到AsyncT上去。 |
| 2026-08-18 | [Rethinking Attention: Polynomial Alternatives to Softmax in Transformers](https://mer.run/posts/rethinking-attention-polynomial-alternatives-to-softmax-in-transformers/) | 作者认为softmax有效是因为它将Attention矩阵的Frobenius范数控制在了O(sqrt(N))量级，从而稳定了训练，因此提出用多项式激活代替softmax、在期望意义上实现相似的范数控制。理论推完发现这文章没中，ICLR2026得分2222，一下子就不想看下去了。感觉实验和理论都不是… |
| 2026-08-18 | [Attention Residuals](https://mer.run/posts/attention-residuals/) | Kimi团队关于Residual Addition的扩展。看起来某种意义上算是复杂的拓扑结构，说不定在现在的硬件上会有优势？ |
| 2026-08-18 | [A Unified View of Attention and Residual Sinks: Outlier-Driven Rescaling is Essential for Transformer Training](https://mer.run/posts/a-unified-view-of-attention-and-residual-sinks-outlier-driven-rescaling-is-essential-for-transforme/) | Qwen团队，分析LLM中的Outliers是如何产生的、有什么影响。 |
| 2026-08-18 | [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](https://mer.run/posts/gated-attention-for-large-language-models-non-linearity-sparsity-and-attention-sink-free/) | NIPS2025 Best Paper。Qwen的。实验实在是过于solid了，真有钱啊。 |
| 2026-08-18 | [Nested Learning: The Illusion of Deep Learning Architectures](https://mer.run/posts/nested-learning-the-illusion-of-deep-learning-architectures/) | 谷歌新作，号称“深度学习新范式”。提到了异步，具体指的是让模型靠近输入的位置的更新频率高于靠后的位置，这个思路和之前Sakana AI的那个文章有点像。但文章里面的东西感觉全都是Fast Weight Programming的内容，arxiv的文章全文也一直没挂出来。 |
| 2026-08-18 | [Kimi Linear: An Expressive, Efficient Attention Architecture](https://mer.run/posts/kimi-linear-an-expressive-efficient-attention-architecture/) | Kimi Linear，有比较详细的实验&Scale Up。有Linear Attention可以去掉RoPE这个结论还是比较惊喜的。 |
| 2026-08-18 | [Speed Always Wins: A Survey on Efficient Architectures for Large Language Models](https://mer.run/posts/speed-always-wins-a-survey-on-efficient-architectures-for-large-language-models/) | AI Lab关于”广义“LLM推理加速的工作，包括Linear Attention，Sparse Attention，Diffusion LLM，Applications等。 |
| 2026-08-18 | [Neuromorphic Principles for Efficient Large Language Models on Intel Loihi 2](https://mer.run/posts/neuromorphic-principles-for-efficient-large-language-models-on-intel-loihi-2/) | ICLR2025 Workshop，基于HAQ实现的Matmul-Free SNN LLM（虽然只做了370M参数的实验）部署到Loihi2上，实现了相比于Qwen-500M 模型3×Throughput和2×能效。但说实话文章内容关键点都没怎么讲，也没有什么特别很exciting的东西。 |
| 2026-08-18 | [Parallelizing Linear Transformers with the Delta Rule over Sequence Length](https://mer.run/posts/parallelizing-linear-transformers-with-the-delta-rule-over-sequence-length/) | DeltaNet |
| 2026-08-18 | [Flash-LLM: Enabling Cost-Effective and Highly-Efficient Large Generative Model Inference with Unstructured Sparsity](https://mer.run/posts/flash-llm-enabling-cost-effective-and-highly-efficient-large-generative-model-inference-with-unstru/) | VLDB2024，阿里的工作，看起来工程特别扎实。LLM任务上只通过对weight做sparse load就能在decode阶段获得3-4倍的提速。 |
| 2026-08-18 | [SpikingBrain-瞬息 1.0技术报告：原生国产自主可控类脑脉冲大模型](https://mer.run/posts/spikingbrain-%E7%9E%AC%E6%81%AF-10%E6%8A%80%E6%9C%AF%E6%8A%A5%E5%91%8A%E5%8E%9F%E7%94%9F%E5%9B%BD%E4%BA%A7%E8%87%AA%E4%B8%BB%E5%8F%AF%E6%8E%A7%E7%B1%BB%E8%84%91%E8%84%89%E5%86%B2%E5%A4%A7%E6%A8%A1%E5%9E%8B/) | 李国齐老师组的新工作技术报告。说实话，我并不觉得这是一个正经的SNN-LLM工作，感觉已经完全是Linear Attention国产化的工作了。很难评价。 |
| 2026-08-18 | [MLP Memory: Language Modeling with Retriever-pretrained External Memory](https://mer.run/posts/mlp-memory-language-modeling-with-retriever-pretrained-external-memory/) | 用MLP学习并代替RAG中kNN输出的概率分布。 |
| 2026-08-18 | [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://mer.run/posts/native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention/) | ACL2025 Best Paper，DeepSeek新作。分层KV Cache提高稀疏度，在训练和推理阶段同时提高性能。 |
| 2026-08-18 | [T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge](https://mer.run/posts/t-mac-cpu-renaissance-via-table-lookup-for-low-bit-llm-deployment-on-edge/) | T-MAC, 用LUT加速BitNet系列的工作，在CPU上跑，后续还有一个工作叫T-MAN是在移动端的高通CPU里面的NPU上跑LUT加速。 |
| 2026-08-18 | [HYTE: Flexible Tiling for Sparse Accelerators via Hybrid Static-Dynamic Approaches](https://mer.run/posts/hyte-flexible-tiling-for-sparse-accelerators-via-hybrid-static-dynamic-approaches/) | ISCA2025，做稀疏数据流分块的，后半截没什么精力看了，现在的工作还没做稀疏编码。 |
| 2026-08-18 | [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://mer.run/posts/swin-transformer-hierarchical-vision-transformer-using-shifted-windows/) | 看看Shift-Window Attention。 |
| 2026-08-18 | [SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and O(T) Complexity](https://mer.run/posts/spikevideoformer-an-efficient-spike-driven-video-transformer-with-hamming-attention-and-ot-comple/) | 用汉明距离替换Attention中的点乘操作，避免出现Spike错开的情况。中间的做法比较有趣，但是实验感觉做的一般般，尤其是claim了自己有硬件实现的情况下energy计算还用的是纯算法的计算，并且FPGA的具体实现也没有透露，说了也没有说清楚。精度没有超过ANN2SNN的SOTA。重点还是需要… |
| 2026-08-18 | [Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN](https://mer.run/posts/sparse-spiking-neural-network-exploiting-heterogeneity-in-timescales-for-pruning-recurrent-snn/) | ICLR 2024 Spotlight, 利用Lyapunov Noise进行SNN Pruning。 |
| 2026-08-18 | [Prosperity: Accelerating Spiking Neural Networks via Product Sparsity](https://mer.run/posts/prosperity-accelerating-spiking-neural-networks-via-product-sparsity/) | HPCA在投的一篇SNN加速器文章，里面的“Product Sparsity”本质是减少相同内容的重复计算，和一般讨论的稀疏是两种不同的概念。 |
| 2026-08-18 | [Recurrent Residual Module for Fast Inference in Videos](https://mer.run/posts/recurrent-residual-module-for-fast-inference-in-videos/) | CVPR2018， DiffEncode + 稀疏加速，但感觉太老了。 |
| 2026-08-18 | [Efficient Spatially Sparse Inference for Conditional GANs and Diffusion Models](https://mer.run/posts/efficient-spatially-sparse-inference-for-conditional-gans-and-diffusion-models/) | NIPS2022上一篇比较有影响力的论文，对GAN和扩散模型做推理加速的工作，提出了Spatially Sparse Inference，仅在被编辑区域上稀疏地应用卷积滤波器，同时对未编辑区域复用缓存的特征 |
| 2026-08-18 | [SlowFast Networks for Video Recognition](https://mer.run/posts/slowfast-networks-for-video-recognition/) | 多分支CNN，会不会有一些分支能学到更加相似的帧间变化？ |
| 2026-08-18 | [DeltaCNN: End-to-End CNN Inference of Sparse Frame Differences in Videos](https://mer.run/posts/deltacnn-end-to-end-cnn-inference-of-sparse-frame-differences-in-videos/) | 利用CNN Layer的“线性”特征在帧之间做feature的差分，并且做了CUDA加速。和ViStream几乎一样的思路，能不能解决我们现在的问题？ |
| 2026-08-18 | [Phi: Leveraging Pattern-based Hierarchical Sparsity for High-Efficiency Spiking Neural Networks](https://mer.run/posts/phi-leveraging-pattern-based-hierarchical-sparsity-for-high-efficiency-spiking-neural-networks/) | ISCA 2025, 基于结构化稀疏的SNN加速器。如果直接用LUT存，可能会出现需要保存的稀疏pattern数量太多，显存占用太严重，所以通过预先校准一级“结构化稀疏”，将Online Spike Activation变成一级可以完全用LUT算的L1 Sparse和稀疏度非常高的L2 Sparse… |
| 2026-08-18 | [Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness](https://mer.run/posts/temporal-flexibility-in-spiking-neural-networks-towards-generalization-across-time-steps-and-deploy/) | ICLR2025 Poster，似乎也在做Elastic inference？ |
| 2026-08-18 | [A Simple Framework for Contrastive Learning of Visual Representations](https://mer.run/posts/a-simple-framework-for-contrastive-learning-of-visual-representations/) | 对比学习SimCLR的论文。对比学习能对齐每一层的Feature吗？ |
| 2026-08-18 | [QKFormer: Hierarchical Spiking Transformer using Q-K Attention](https://mer.run/posts/qkformer-hierarchical-spiking-transformer-using-q-k-attention/) | QKFormer，NIPS2024 Spotlight，把Direct Training SNN在ImageNet和CIFAR上的点刷的特别高，感觉之后要做就避不开它。 |
| 2026-08-18 | [Transformers without Normalization](https://mer.run/posts/transformers-without-normalization/) | 何恺明新作，用DyT代替Norm，把同步操作变成了Element Wise的操作。新文章里面有用到，学习一下。 |
| 2026-08-18 | [Visualizing and Understanding the Effectiveness of BERT](https://mer.run/posts/visualizing-and-understanding-the-effectiveness-of-bert/) | 最近做SNN训练的过程中在研究怎么可视化训练过程中的Loss，在想新加入的方法会不会对模型的Loss Landscape有影响，一般讲Loss Landscape怎么做可视化的文章都会引用这篇文章对Loss Landscape的分析和做法。 |
| 2026-08-18 | [One-Minute Video Generation with Test-Time Training](https://mer.run/posts/one-minute-video-generation-with-test-time-training/) | 最近Demo很火的TTT视频生成，可以生成60s级别的长视频。学习一下TTT的东西，SNN的On-Chip Learning和TTT能不能做结合？ |
| 2026-08-18 | [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://mer.run/posts/evolution-strategies-as-a-scalable-alternative-to-reinforcement-learning/) | 这两天在弄SNN训练的事情，需要验证一下用的Surrogate Gradient的准确性，老师介绍读一下这篇文章，用Evolution Strategy验证一下现在梯度估计的准确性。 |
| 2026-08-18 | [SparTA: Deep-Learning Model Sparsity via Tensor-with-Sparsity-Attribute](https://mer.run/posts/sparta-deep-learning-model-sparsity-via-tensor-with-sparsity-attribute/) | sparTA，带稀疏优化的DNN编译器，把tensor的稀疏性作为一种重要属性考虑到编译过程中，生成高效的代码。 |
| 2026-08-18 | [Scalable Diffusion Models with Transformers](https://mer.run/posts/scalable-diffusion-models-with-transformers/) | Diffusion Transformer. |
| 2026-08-18 | [Conv2Former: A Simple Transformer-Style ConvNet for Visual Recognition](https://mer.run/posts/conv2former-a-simple-transformer-style-convnet-for-visual-recognition/) | 使用大kernel DS卷积替代self-attention。字节新加坡的工作。 |
| 2026-08-18 | [SpikeCV: Open a Continuous Computer Vision Era](https://mer.run/posts/spikecv-open-a-continuous-computer-vision-era/) | 事件相机开源框架。 |
| 2026-08-18 | [Neuromorphic computing at scale](https://mer.run/posts/neuromorphic-computing-at-scale/) | 发在Nature上的一篇review，讨论了SNN/神经模态计算社区现在面临的一些问题、挑战，和一些可能的发展方向。 |
| 2026-08-18 | [Titans: Learning to Memorize at Test Time](https://mer.run/posts/titans-learning-to-memorize-at-test-time/) | 从TTT改进而来的新架构，尝试通过TTT的方式改进模型的记忆能力。 |
| 2026-08-18 | [Segment Anything](https://mer.run/posts/segment-anything/) | Meta的SAM。 |
| 2026-08-18 | [SDiT: Spiking Diffusion Model with Transformer](https://mer.run/posts/sdit-spiking-diffusion-model-with-transformer/) | 脉冲Diffusion Transformer，里面的Transformer的结构是RWKV的。 |
| 2026-08-18 | [ConvUNeXt:An efficient convolution neural network for medical image segmentation](https://mer.run/posts/convunextan-efficient-convolution-neural-network-for-medical-image-segmentation/) | ConvNext + UNet，发在一个C刊上，借鉴学习一下，想想我的模块怎么设计。 |
| 2026-08-18 | [Rethinking the Membrane Dynamics and Optimization Objectives of Spiking Neural Networks](https://mer.run/posts/rethinking-the-membrane-dynamics-and-optimization-objectives-of-spiking-neural-networks/) | NIPS2024。主要研究的是静态任务中，推理前膜电位初始值设置对精度的影响。 |
| 2026-08-18 | [ConvNext V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://mer.run/posts/convnext-v2-co-designing-and-scaling-convnets-with-masked-autoencoders/) | ConvNext续作，引入了MAE。 |
| 2026-08-18 | [A ConvNet for the 2020s](https://mer.run/posts/a-convnet-for-the-2020s/) | CVPR2022。Meta的工作，在ViT相关工作占视觉大头的情况下重构纯卷积的网络，并且取得了很好的效果。 |
| 2026-08-18 | [Were RNNs All We Needed?](https://mer.run/posts/were-rnns-all-we-needed/) | 改进RNN，便于scale up |
| 2026-08-18 | [SparseRT: Accelerating Unstructured Sparsity on GPUs for Deep Learning Inference](https://mer.run/posts/sparsertaccelerating-unstructured-sparsity-on-gpus-for-deep-learning-inference/) | GPU上做MM相关的算子生成，利用load balancing和稀疏做加速，根据model生成PTX代码 |
| 2026-08-18 | [VPRTempo: A Fast Temporally Encoded Spiking Neural Network for Visual Place Recognition](https://mer.run/posts/vprtempo-a-fast-temporally-encoded-spiking-neural-network-for-visual-place-recognition/) | ICRA2024的论文，用Temporal Encoding的STDP Direct Training的SNN做场景识别的任务。太简单了 |
| 2026-08-18 | [Memory-Efficient Reversible Spiking Neural Networks](https://mer.run/posts/memory-efficient-reversible-spiking-neural-networks/) | 通过设计提高训练速度，降低显存占用的工作。 |
| 2026-08-18 | [SpikeMba: Multi-Modal Spiking Saliency Mamba for Temporal Video Grounding](https://mer.run/posts/spikemba-multi-modal-spiking-saliency-mamba-fortemporal-video-grounding/) | SNN+Mamba完成TVG时序视频定位任务，哈工大和北大的工作。 |
| 2026-08-18 | [Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection](https://mer.run/posts/integer-valued-training-and-spike-driven-inference-spiking-neural-network-for-high-performance-and-e/) | SpikeYOLO，中科院自动化所的工作，ECCV2024 Oral |
| 2026-08-18 | [SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN](https://mer.run/posts/spikezip-tf-conversion-is-all-you-need-for-transformer-based-snn/) | 游康师兄的工作，ANN2SNN的Transformer。 |
| 2026-08-18 | [SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence](https://mer.run/posts/spikingjelly-an-open-source-machine-learning-infrastructure-platform-for-spike-based-intelligence/) | 北大惊蛰，非常有影响力的SNN框架，实现了从数据编码、数据集整合到训练、硬件部署的全流程，SNN的torch级别的工作。发表在Science Advanced上。 |
| 2026-08-18 | [I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models](https://mer.run/posts/i-llm-efficient-integer-only-inference-forfully-quantized-low-bit-large-language-models/) | LLM的Interger-Only PTQ量化工作。 |
| 2026-08-18 | [The Minimum Equivalent DNF Problem and Shortest Implicants](https://mer.run/posts/the-minimum-equivalent-dnf-problem-andshortest-implicants/) | 证明MIN-DNF问题是完全的 |
| 2026-08-18 | [I-ViT: Integer-only Quantization for Efficient Vision Transformer Inference](https://mer.run/posts/i-vit-integer-only-quantization-for-efficient-vision-transformer-inference/) | 对ViT的纯整型量化，W8A8，中科院2023 ICCV |
| 2026-08-18 | [Efficient and Effective Methods for Mixed Precision Neural Network Quantization for Faster, Energy-efficient Inference](https://mer.run/posts/efficient-and-effective-methods-for-mixed-precision-neural-network-quantization-for-faster-energy-e/) | EAGL，声称只要用CPU在3秒内就能完成对ResNet的量化，效率远高于HAWQ等其他传统的方法 |
| 2026-08-18 | [Towards spike-based machine intelligence with neuromorphic computing](https://mer.run/posts/towards-spike-based-machine-intelligence-with-neuromorphic-computing/) | Nature上关于SNN的综述 |
| 2026-08-18 | [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://mer.run/posts/flashattention-fast-and-memory-efficient-exact-attention-with-io-awareness/) | Flash Attention，利用硬件结构加速Attention计算速度、减少内存占用的算法。核心是Tiling，Online Softmax和Kernel Fusion。 |
| 2026-08-18 | [WWW: What, When, Where to Compute-in-Memory](https://mer.run/posts/www-what-when-where-to-compute-in-memory/) | 一些关于存内计算的验证与思考。 |
| 2026-08-18 | [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://mer.run/posts/quantization-and-training-of-neural-networks-for-efficient-integer-arithmetic-only-inference/) | 谷歌的，第一篇完整跑通interger-only量化推理流程的工作。 |
| 2026-08-18 | [SpikeSim: An end-to-end Compute-in-Memory Hardware Evaluation Tool for Benchmarking Spiking Neural Networks](https://mer.run/posts/spikesim-an-end-to-end-compute-in-memory-hardware-evaluation-tool-for-benchmarking-spiking-neural-n/) | SNN部署的硬件设计or evaluation benchmark。 |
| 2026-08-18 | [PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU](https://mer.run/posts/powerinfer-fast-large-language-model-serving-with-a-consumer-grade-gpu/) | From IPADS, 利用模型预测LLM中需要激活的MoE or Neuron，减少资源消耗。 |
| 2026-08-18 | [Evaluating Spatial Accelerator Architectures with Tiled Matrix-Matrix Multiplication](https://mer.run/posts/evaluating-spatial-accelerator-architectures-withtiled-matrix-matrix-multiplication/) | GEMM data mapping的介绍，主要是各种脉动阵列相关的加速器。 |
| 2026-08-18 | [HAWQ: Hessian Aware Quantization of Neural Networks with Mixed-Precision](https://mer.run/posts/hawq-hessian-aware-quantization-of-neural-networks-with-mixed-precision/) | 模型量化经典方法，基于黑森矩阵，一种二阶信息的量化方法。 |
| 2026-08-18 | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://mer.run/posts/tvm-an-automated-end-to-end-optimizing-compiler-for-deep-learning/) | TVM。 |
| 2026-08-18 | [A Comprehensive Survey on Electronic Design Automation and Graph Neural Networks: Theory and Applications](https://mer.run/posts/a-comprehensive-survey-on-electronic-design-automation-and-graph-neural-networks-theory-and-applica/) | 图神经网络在EDA领域应用的综述。 |
| 2026-08-18 | [Towards Scalable GPU-Accelerated SNN Training via Temporal Fusion](https://mer.run/posts/towards-scalable-gpu-accelerated-snn-training-via-temporal-fusion/) | 意义不明，用Layer-By-Layer写了一下LIF就没别的Contribution了，发在了一个叫做ICANN的会上。工作量也太小了。 |
| 2026-08-18 | [Optimizing Bit-Serial Matrix Multiplication for Reconfigurable Computing](https://mer.run/posts/optimizing-bit-serial-matrix-multiplication-for-reconfigurable-computing/) | BISMO优化。 |
| 2026-08-18 | [Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures](https://mer.run/posts/roofline-an-insightful-visual-performance-model-for-floating-point-programs-and-multicore-architect/) | Roofline model，描述一个系统的性能是受内存制约还是受计算制约。 |
| 2026-08-18 | [A Hardware-Software Blueprint for Flexible Deep Learning Specialization](https://mer.run/posts/a-hardware-software-blueprint-for-flexible-deep-learning-specialization/) | VTA。 |
| 2026-08-18 | [BISMO: A Scalable Bit Serial Matrix Multiplication Overlay for Reconfigurable Computing](https://mer.run/posts/bismo-a-scalable-bit-serial-matrix-multiplication-overlay-for-reconfigurable-computing/) | BISMO。 |
| 2026-08-18 | [Code Transpilation for Hardware Accelerators](https://mer.run/posts/code-transpilation-for-hardware-accelerators/) | 基于Metalift，做的还很不完善。 |
| 2026-08-18 | [2026.8.18](https://www.justzht.com/2026-8-18/) | 八月中旬了，原本要把 J 出庭的故事补完的，但没啥时间写，因此流水账也跟着拖了，还是优先流水账，J 的故事 |
| 2026-08-18 | [2024](https://mer.run/posts/2024/) | 2024. |
| 2026-08-18 | [观《牛来》后记](https://www.ixiqin.com/2026/08/18/afterword-to-niu-lai/) | 先说评价：牛来这部电影在票价合适的时候，是可以考虑去看的；虽然制作稀烂，但故事本身的元素还行；现场也氛围很轻松，如果你去一个人很多的场次，会很欢乐。 最近《牛来》很火，作为一个乐子人，我自然也 … |
| 2026-08-18 | [人生第一次：站着干活](https://www.hecaitou.com/2026/08/first-time-ever-standing-on-the-job.html) | 此时此刻，我的电脑桌面距离地面 1.1 米，而我正站着打下这些字。 这一天我等了很久，但之前始终因缘无法具足。我知道站着打字对肌肉好，对眼睛好，对颈椎好，也知道很容易实现，可以选择升降桌或者桌面升降台。但是事情就是这样的，人对不正确的事情总是争分夺秒，为了那一点点做贼的快意。正确的事情却一拖再拖，随… |
| 2026-08-18 | [我玩了一下Polymarket预测市场](https://www.cheshirex.com/10904.html) | 昨晚逛推特看到有人在说Polymarket的空投，想了下之前了解到Polymarket是在去年了，但是没有上手 […] |
| 2026-08-18 | [门缝](https://mobius.blog/25423.html) | 夏天的咖啡厅，露台门被打开了一条门缝，是因为上一个进入的人并没有完整闭合好玻璃门，于是这个门缝开始往室内涌进大 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-18 | [记录下 Kimi 699 套餐 7 天的](https://versun.me/blog/tweet-2089514949106335946) | 记录下 Kimi 699 套餐 7 天的额度，大概在 1.5B token |
| 2026-08-18 | [Memos #2026-08-17](https://www.taober.blog/memos) | 01:46 意识到做任何的决定和行为，都只需要为自己负责。 其他人一部分会无条件地支持你，另一部分根本就不在乎你。 |
| 2026-08-17 | [Unreal updated](https://macsourceports.com/game/unreal) | The build of Unreal has been updated to version v227k_15 of the project |
| 2026-08-17 | [Quetoo updated](https://macsourceports.com/game/quetoo) | The build of Quetoo has been updated to version v1.0.73 of the project |
| 2026-08-17 | [Splatterlight updated](https://macsourceports.com/sourceport/spatterlight) | The build of Splatterlight for the Infocom series of games has been updated to version v1.5.4 of the project\n\nhttps://macsourceports.com/sourceport/… |
| 2026-08-17 | [李白写"汉家陵阙"时，那些早塌了，只剩这几座...](https://macin.org/2026/08/17/qu-xian-han-que/) | 阅读全文 → 有些地方，是专门用来唤醒前世的。 |
| 2026-08-17 | [你敢信，一个 27B 的qwen 3.8](https://versun.me/blog/tweet-2089475382915613085) | 引用 Artificial Analysis Intelligence Index puts Qwen3.8-27B at DeepSeek V4-Pro and GPT 5.6 Luna performance. This is the first time a local model has s… |
| 2026-08-17 | [R#115 RAS!](https://blog.sakanano.moe/journals/random_115) | 2026.8.11 ~ 2026.8.17 |
| 2026-08-17 | [有些事情没有答案，只有选择](https://blog.solazy.me/20260817/) | 选择，可能未必都需要经过计算 |
| 2026-08-17 | [已将我的 Nowledge mem 模型](https://versun.me/blog/tweet-2089350427506889110) | 已将我的 Nowledge mem 模型改为 qwen3.8-27b ，虽然慢了点，先用几天看看情况 |
| 2026-08-17 | [遛猫](https://mobius.blog/25433.html) | 楼下遇到一个遛猫的小女孩，因为用绳子勒着猫的脖子，有大人教育她别伤害猫。小女孩指了指我牵着的狗，说：我的猫比狗 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-17 | [观《老式喜剧》后记](https://www.ixiqin.com/2026/08/17/afterword-to-old-style-comedy/) | 因为小学背过《雷雨》，演过《雷雨》，我对于人艺就很好奇。后面从深圳去北京工作，有了机会，我就曽和太太一起去人艺看了《蔡文姬》，后面种种原因，就一直没看；那一场有杨立新和濮存晰，还挺好的，不过 … |
| 2026-08-17 | [我也申请了，了无音讯](https://versun.me/blog/tweet-2089290159728812135) | 引用 Kimi 全球大使计划有人进去了吗？ 我也申请了，了无音讯 |
| 2026-08-17 | [我有点看不明白了， 为啥好多人要花900](https://versun.me/blog/tweet-2089287218158531030) | 我有点看不明白了， 为啥好多人要花900刀买年费的 grok heavy，就因为原价是3000刀吗？ AI 时代，年费，900刀！ 我实在想不明白🤣 |
| 2026-08-17 | [哇咔财务管家，正式上架 Apple Store 啦](https://blog.ops-coffee.com/fire/wakaka-finance-app-listed-app-store.html) |  |
| 2026-08-17 | [牛来了坐在爱因斯坦的小板凳上](https://www.hecaitou.com/2026/08/the-cow-on-einsteins-little-bench.html) | 这个周末每天都有读者在留言区堵着问我：你看《牛来》了吗？你怎么看《牛来》？但我根本不想看啊！ 因为我的两个朋友为了争论《牛来》究竟是失败垃圾还是电影艺术创新，天天在群里吵架，每次点开都是黑压压几大屏幕的辩词，你来我往，没完没了，感觉是我在微信群里上某个成员全是杠王的 BBS，看得我头痛欲裂。 不至于… |
| 2026-08-17 | [牛来](https://yipai.me/post/2547.html) | 周末去看了《奥德赛》，感觉还行吧。就是时间有点太长了，九点开始，十一点半都过了才结束。看完回去再查下资料，了解下奥德赛原本的故事脉络，就凌晨一点了。同期上映的还有《牛来》。有人很反感这部《牛来》，在没人去看的时候，认为是粗制滥造，怎么审核通过的？票房起来之后，又认为是资本的操控。我倒是觉得挺正常的，… |
| 2026-08-17 | [让 Agent 调用网页版 5.6 Sol](https://shiquda.link/agent-call-chatgpt-web-5.6-sol/) | 分享一套让所有 Agent 免费「调用」5.6 Sol 的省额度方法 ，适合拥有自己的付费 ChatGPT 账户的朋友。 我们知道 ChatGPT 网页端进行对话时，是不消耗 Codex 的额度的。我们经常在网页上让 ChatGPT 去帮我们做网络检索、深度思考等工作，然后可能把它给出的方案再转发给… |
| 2026-08-17 | [过剩信息，剥夺我](https://mobius.blog/25416.html) | 这个标题没有实际意义，纯粹是因为我从坐着的这个视角看过去，有一个上班族刚好打开自己的笔记本电脑，而这句话是贴在 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-17 | [为啥最近 DHH 的 Omarchy 又](https://versun.me/blog/tweet-2089152283871428676) | 引用 看了DHH在Rails World上的演讲，真是开发者的嘴替，部署的复杂性、云端测试缓慢、本地开发问题、omarchi安装器、rails 8.1各种新功能、还有边缘计算，一个客户一个数据库等等。。。一个小时的演讲我竟然看完了。。。。 不得不说，牛逼的人确实有牛逼之处 为啥最近 DHH 的 Om… |
| 2026-08-16 | [大脑充血 Vol.94](https://www.geedea.pro/weekly/94/) | 怎么又到周一了，我上周做了什么……？生活似乎变得稳定，但也开始无聊起来了。我的文化体力还是没有恢复，抱歉了，我可能要过好久才能再写一篇书评了。不过与此同时，我又是怎么做到写了 那么长一篇《奥德赛》影评 ，竟然还有劲儿继续写第二篇的？我的大脑可真是神奇。 吾仅悉落 Nothing Makes Sens… |
| 2026-08-16 | [记首次 .NET 跨平台开发——Deepseek Harness Desktop](https://nigzu.com/csharp-dotnet-avalonia-deepseek-harness-client-ai/) | 史上增长最快的开源 Agent 框架 DeepSeek Harness（DSH）给我带来了 DIY 的乐趣。官方给的"命令行 + 网页"这套组合能用，但不方便用 |
| 2026-08-16 | [Memos 小记](http://www.uncoverman.com/my-memos-is-ready.html) | 喜 欢用微博、推特、小红书、朋友圈这类产品，它们共同特点都是短文，配图，随时随地。无摩擦写作，很适合随手记。 但是这些只言片语散落在各个平台，有不同的受众，被不同的公司掌握着数据和曝光，无法随意流动。 于是有个设想，能否拥有一个自己的短文平台？支持图文，支持 Mac 、 iOS 、 Windows… |
| 2026-08-16 | [放弃自证的减负感](https://blog.solazy.me/20260816/) | 有时候，需要允许别人误解自己，解释并没有那么重要 |
| 2026-08-16 | [WOWOWOWO 就等它了！我目前本地就](https://versun.me/blog/tweet-2088978001015054420) | 引用 Qwen 3.8 35B A3B almost confirmed! Spotted on github! while everyone's busy swapping qwen3.6 27b for the new qwen3.8 27b dense drop on their single… |
| 2026-08-16 | [什么是真正的痛苦](https://kaix.in/2026/0816/) | 这几天经常看到一段李娟和李诞的对话，对话中李娟说世界上真正的痛苦，只有一种，叫贫穷——所有痛苦都是虚构的，只有贫穷才是真实的痛苦。我相信李娟是真诚的，她有她的逻辑，她接着就说自己没资格谈痛苦，因为她现在有好几套房、物质充裕。 为了不造成误导，有必要说一句，她这些话的语境是说精神上的内耗与纠结是可以「… |
| 2026-08-16 | [重新思考Agent和编辑器](https://ecnelises.com/2026/08/rethinking-agents-and-editors/) | 最早进入公众视野的AI编程工具大概是GitHub Copilot或者Tabnine，使用方式类似一个扩展版的IDE补全：工具根据光标位置的上下文猜测用户想输入的代码，以虚色形式提示，可以按Tab落实。DeepSeek的API至今仍保留了这个功能。这个功能今天看来有点简朴甚至落后，但在ChatGPT诞… |
| 2026-08-16 | [突然觉得，不追求完美，接受混乱，接受不产](https://versun.me/blog/tweet-2088962538922782957) | 突然觉得，不追求完美，接受混乱，接受不产出，才是最难的 比如发呆，等一个人，看天黑，等朝阳，有些时刻，存在的意义就是存在本身，这些才是最稀缺的 |
| 2026-08-16 | [从订阅链接到自动分流：小白也能看懂的 Clash Verge 原理](https://www.shiguopeng.cn/posts/2026081617/) | 🤖 声明 ：本文由 AI 辅助整理生成，并经作者严格人工审阅校对。 前言 很多人用 Clash 时最困惑的是：机场、订阅和软件到底是什么关系？出问题除了换节点还能干嘛？ 本文剔除繁杂参数，通过 4 张核心架构图 和 3 分钟快速阅读 帮你搞懂它的核心逻辑。 1. 角色拆解：谁是干嘛的？ 可以通过下图… |
| 2026-08-16 | [git fetch 实现断点续传](https://blog.est.im/2026/stdout-33) | git fetch origin main --depth=1 一次只下一个 pack，包含所有缺失对象，国内这网络你懂的，断开就废了，然后从头下载，往往又出事； 老外不懂国内网络条件这么艰苦，只能自己让AI改造。结果： https://github.com/est/snippets/tree/ma… |
| 2026-08-16 | [Chris Sawyer's Locomotion updated](https://macsourceports.com/game/locomotion) | The build of OpenLoco for Chris Sawyer's Locomotion has been updated to version v26.08 of the project |
| 2026-08-16 | [Quake III: Arena updated](https://macsourceports.com/game/quake3arena) | The build of Quake3e for Quake III: Arena has been updated to the latest code of the project |
| 2026-08-16 | [VCMI updated](https://macsourceports.com/sourceport/vcmi) | The build of VCMI for the Heroes of Might and Magic III series of games has been updated to version 1.7.5 of the project\n\nhttps://macsourceports.com… |
| 2026-08-16 | [奥德修斯这个人](https://www.hecaitou.com/2026/08/Odysseus-the-Man.html) | 奥德赛和奥德修斯不是一回事，奥德修斯是人名，奥德赛是书名，意思是奥德修斯的故事，就像是岳飞和《说岳》一样。 无论从哪一个角度来看，奥德修斯都是讨人厌的家伙。诺兰选择马特·达蒙其实并不合适，此人太过正气，太过忠厚，观众因此而激发的怜悯和同情就显得有点便宜。在荷马史诗《奥德赛》的最后，读者对于奥德修斯的… |
| 2026-08-16 | [New Release: FLESHCANCER](https://macsourceports.com/game/fleshcancer) | FLESHCANCER is a horor-themed Boomer Shooter from Brazil, published by the same team as BRAZILIAN DRUG DEALER 3 . You take the role of someone who see… |
| 2026-08-16 | [DeepSeek 官方 Agent 部署实录：公网零端口暴露的安全玩法](https://www.wangwangit.com/DeepSeek%20%E5%AE%98%E6%96%B9%20Agent%20%E9%83%A8%E7%BD%B2%E5%AE%9E%E5%BD%95/) | dsh 部署到服务器 + 安全远程访问，小白能跟着做完的实操版 |
| 2026-08-16 | [≡ 008｜这一周莫比乌斯环转到了哪里？](https://mobius.blog/25394.html) | —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-15 | [我的世界一直下雨](https://www.geedea.pro/article/rain-never-stop/) | 我的草稿箱里有一篇关于神经多样性的文章一直没写得下去，这几天我才意识到，比起写一篇近似于学术综述的无聊文章，不如写点掏心窝子的话。当然，这也意味着这篇文章不会写得很有条理。 在我爷爷的六十岁大寿上，司仪要十二三岁的我站在台上说点祝福的话。我看着底下二十桌人，说不出一句话。站在我旁边的表哥很自然地说出… |
| 2026-08-15 | [我不敢随便推荐 App 了](https://blog.solazy.me/20260815/) | 有太多开发者找我自荐 App，希望我帮忙宣传，但是我对于这一行为非常谨慎。 |
| 2026-08-15 | [冷知识：博客的评论区不是广告区](https://blog.mfwt.top/index.php/archives/1529/) | 刷聚合站，刷到了ZyPlj（ZY知识库）的博文，大概是说，某AI（LLM，下同）中转站的老板，使用AI编写了脚本（或让其代为操作），向一组个人博客的评论区批量发送中转站的推广信息。看到这篇文章后... |
| 2026-08-15 | [黄鼠狼](https://godruoyi.com/posts/weasel/) | 我昨晚咬死三只鹅一只鸡。那是在一个农户家， 凌晨三点半。我从铁丝网的缺口悄悄地钻进了鸡圈，我看到鸡圈里面有三只鹅 |
| 2026-08-15 | [样式雷祖居 风水场域实探](https://yovey.me/yangstyle-lei-archives-with-fengshui/) | 近来在读王其亨主编《风水理论研究》，这本书是去年天津一行读丁垚《发现独乐寺》衍生来的，他在书中提到了自己的老师 … Continue reading "样式雷祖居 风水场域实探" |
| 2026-08-15 | [试用了一天，Qwen 3.8 27B 文](https://versun.me/blog/tweet-2088564791623418051) | 引用 这才是我的 Qwen 嘛，本地部署 Opus 4.6 性能的模型，还要啥自行车 mac mini m4 pro 64G 关掉thinking，实测 12 tokens/s https://twitter.com/Alibaba_Qwen/status/2088280188362867185 试… |
| 2026-08-15 | [《奥德赛》观后](https://www.hecaitou.com/2026/08/On-Watching-The-Odyssey.html) | 今天是周六，我在早上七点半起床，冒着雨打车去北京电影博物馆，为了赶上 9 点 20 那一场 IMAX GT 版的《奥德赛》。11 点多，我起身艰难穿过半排观众去洗手间。回来之后觉得再麻烦一遍这些同样早起的观众，破坏他们的观影体验实在是有点不道德，于是，我紧贴着 IMAX 厅的后墙，站了一个多小时看完… |
| 2026-08-15 | [诺兰的《奥德赛》采取了什么样的改编策略？](https://www.geedea.pro/article/odyssey/) | 笔者刚刚从电影院回到家，趁着记忆还很清晰来写影评。离开影院之前我记下了几个印象深刻的点，接下来我会逐个分析这些情节、人物、背景乃至主题层面的增删改究竟和原著有什么区别，同时我还会对比另外一部《奥德赛》的改编作品，音乐剧《EPIC：The Musical》，看看不同的创作者采用了什么样的改编策略，背后… |
| 2026-08-15 | [杂谈安全 - 《兔死狗烹之无患可除：当安全开始证明自己的存在》](https://www.impdx.vip/archives/tu-si-gou-peng-zhi-wu-huan-ke-chu-dang-an-quan-kai-shi-zheng-ming-zi-ji-de-cun-zai) | 杂谈安全 - 《兔死狗烹之无患可除：当安全开始证明自己的存在》 ——我们真的希望威胁彻底消失吗？ 一、鼠患，是我们的饭碗 【来客】： 你说无患可除，匠人便成祸患。可若真有鼠患，你们总该是有用的吧？ 【匠人】： 自然有用。 【来客】： 如何有用？ 【匠人】： 先寻鼠踪，再报鼠患；先论其凶，再定其险；最 |
| 2026-08-15 | [【公告】RSS 订阅地址优化说明](https://versun.me/blog/rss-feeds-by-content-type) | 最近，我给博客加上了「推特同步」功能，博客会自动抓取并发布我在 Twitter 上的所有发言。这个新特性让内容更丰富了，但也让原有的 RSS 订阅源变得有些冗杂。在此，向一直订阅我的朋友们说声抱歉。为提升阅读体验，我已对 RSS... |
| 2026-08-15 | [聊聊郭刚](https://blog.lhasa.icu/posts/life/2026-08-15-cultural-revolution-2/) | 欲加之罪，何患无辞 |
| 2026-08-15 | [香港 Day2・赞美之泉演唱会](https://blog.yasking.org/a/photos-hk-day2) | 第二天的天气也是阴的，听着外边儿淅沥沥的雨声和车压过路面的声音，也就没有早出去的心情，中午饿了就打算出去吃 … |
| 2026-08-15 | [克而不服](https://www.hecaitou.com/2026/08/Conquered-Yet-Unsubdued.html) | 每天我都会收到很多读者私信，向我提出各种问题。这些问题千奇百怪，但是其中有一个高频词引起了我注意，它就是「克服」。 粗略统计一下，十个问题里就有两三个是在询问如何才能「克服」什么，可以想见「克服」这两个字是多么深入人心。而我很疑惑，为什么有那么多人会本能地使用这个词，为什么在那么多种解决之道中他们会… |
| 2026-08-15 | [杂谈-《兔死狗烹》我们真的希望威胁彻底消失吗？](https://www.impdx.vip/archives/aqzt-tsgp1) | 灵感来自抖音@马走日 有声版： 文字版 【匠人】：我十五岁拜师学艺，二十岁自立门户。三十年光阴浮沉，我毕生所学，不过这一门手艺。 【来客】：何 |
| 2026-08-15 | [向云端｜西南自驾10 - 下司](https://blog.ops-coffee.com/r/2026-southwest-road-trip-10-xiasi.html) |  |
| 2026-08-15 | [完蛋了，自己的手打回复也出现了“不是。。](https://versun.me/blog/tweet-2088470014362005566) | 引用 @kevinmadevzh 同意，还有一个典型的问题就是，免费用户提需求提得比谁都勤，因为没有成本。 开发者很容易陷在这堆需求里自我感动，但对产品价值未必是正向的，付费门槛本身就是最好的需求过滤器 当然不是说免费反馈都没价值，而是没有付费门槛时，信号和噪音分不开，小团队扛不住这个筛选成本 完蛋… |
| 2026-08-15 | [1998，游戏厅外的世界](https://www.tortorse.com/archives/the-world-outside-the-arcade-1998/) | 九十年代的年轻人围坐在电视前玩格斗游戏 |
| 2026-08-15 | [我一直关注 Claw-Eval 排行榜，](https://versun.me/blog/tweet-2088448347418083808) | 我一直关注 Claw-Eval 排行榜，但它不更新了，太可惜了 https://claw-eval-live.github.io/ |
| 2026-08-15 | [中式番茄炒鸡蛋吃多了也会腻](https://mobius.blog/25388.html) | 在开始今天的话题之前，得叠好几重甲： 在看完《龙餐馆》之后，我突然有一种持续性的“生理不适”。这种生理不适不是 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-15 | [这才是我的 Qwen 嘛，本地部署 Op](https://versun.me/blog/tweet-2088424069603680550) | 引用 Performance of Qwen3.8-27B: 这才是我的 Qwen 嘛，本地部署 Opus 4.6 性能的模型，还要啥自行车 mac mini m4 pro 64G 关掉thinking，实测 12 tokens/s |
| 2026-08-15 | [Python 潮流周刊#163：在浏览器上运行 Numba](https://pythoncat.top/posts/2026-08-15-weekly/) | 分享了 12 篇文章，12 个开源项目 |
| 2026-08-15 | [HSBC汇丰澳洲宣布关闭，2%返现要凉了](https://www.ozexplorers.com/%E7%BE%8A%E6%AF%9B%E6%94%BB%E7%95%A5/2026/08/15/hsbc-australia-will-close-soon-no-more-cashback.html) | 7月底的时候，我收到了一封来自HSBC Australia的邮件： |
| 2026-08-14 | [克兰奇杀妻案](https://re.karlbaey.top/articles/return-to-dusk/the-clench-wife-murder-case/) | The Clench Wife-Murder Case, or Stitches, whatever. 1 四月刚把大门 … |
| 2026-08-14 | [DeepSeek Harness 论文《时空可组合性编程范式》中文白话](https://nigzu.com/deepseek-harness-cordis-programming-paradigm-spatiotemporal-composability-plain-explanation/) | DeepSeek 开源的智能体产品 deepseek-harness 采用“一切皆插件”的架构，其中核心插件框架 Cordis 的思想来自同期论文 《A Programming Paradigm for Spatiotemporal Composability》 |
| 2026-08-14 | [听艾怡良深圳演唱会](https://tianheg.co/posts/eve-ai-shenzhen-2026/) | 今天虽然是周六，但是也上了八小时班。到了晚上还有工作的事情找来，让人不胜其烦。本来看演唱会是很开心的事情，因为工作这种喜悦的情绪被削弱了。应援棒的灯光让我担心自己的眼睛会被闪瞎，实际也的确让我的眼睛不舒服。 |
| 2026-08-14 | [AI&#124;大模型智力测试,鹈鹕SVG生成](https://programnotes.cn/ai-test-v2/index.html) | simonwillison 最先提出的测试方案,提示词: Generate an SVG of a pelican riding a bicycle </blockquot |
| 2026-08-14 | [第一次走进互联网](https://www.tortorse.com/archives/first-step-into-the-internet/) | 上一篇的故事，停在那个没有从学校 286 屏幕里跑出来的马里奥上。 |
| 2026-08-14 | [逻辑自洽不等于事实完整](https://blog.solazy.me/20260814/) | 今天是一篇自省文 |
| 2026-08-14 | [当 AI 让人不再相信工作｜灵感电波 #134](https://www.linggandianbo.com/newsletter-134/) | AI 为什么先动摇了知识工作者对职业的信仰；一位小说家怎样利用机器的错误重获创作乐趣。另有一万步的真实来源、神经可塑性的自我提升神话，以及 20 个值得存下的 YouTube 视频。 |
| 2026-08-14 | [在 WSL2 中使用 Bitwarden SSH Agent](https://guchengf.me/blog/bitwarden-ssh-agent-on-wsl2/) | Bitwarden 桌面客户端可以充当 SSH Agent，让 SSH 私钥保存在 Bitwarden 保险库中，而不是直接存放在 ~/.ssh 目录。 在 Windows 中启用 Bitwarden SSH Agent 后，PowerShell 可以直接使用其中的密钥。但 WSL2 中的 Linu… |
| 2026-08-14 | [cndota 打的什么鬼东西啊，像是在打](https://versun.me/blog/tweet-2088204000407834772) | cndota 打的什么鬼东西啊，像是在打人机的心态，对面应该也感觉像打人机吧😂 第一天就全军覆没，唉，老人打不动，新人不愿打，cndota要断层了🤕 |
| 2026-08-14 | [独立开发者的英国公司报税（2026）](https://www.meettea.com/uk-company-tax-2026.html) | 给独立开发者与小微企业的英国公司报税实战指南：CT600、年度账目、Dormant 零申报，从流水归类到提交全流程。 |
| 2026-08-14 | [终结竞争：从护城河到商业终局的实战指南](https://www.meettea.com/business-moat-endgame.html) | 从护城河到商业终局的实战指南：彼得·蒂尔框架 + AI 时代的商业重构 |
| 2026-08-14 | [SkyWalking 每日写入 ES 数据量过大排查与降采样](https://199604.com/3646) | SkyWalking 每日写入 ES 数据量过大排查与降采样 记录时间：2026-08-13 环境：dyck […] |
| 2026-08-14 | [GLM-5.3 发布了，基座模型和 GL](https://versun.me/blog/tweet-2088145366592192969) | 引用 Introducing GLM-5.3: Built to Code. Ready for Cyber Defense. - Top-tier coding and agentic capabilities, achieved through post-training on the 743B… |
| 2026-08-14 | [灵魂插件 MCP](https://kaix.in/2026/0814/) | 最近咖啡馆工作依然忙碌，身体上倒完全适应，但是越来越觉得费神。对我而言，身体上放松的方式不是躺下，而是摆弄花花草草，继续劳作，晚上睡个好觉。精神上则是看看让自己愉快的书，或者捡起随手丢在一边的废弃代码让脑子换个运转的方向。 所以这几天，在我三米高的琴叶榕底下，折腾出来一个「甄仁岛灵魂插件」。简单说，… |
| 2026-08-14 | [什么都不想做的时候](https://www.hecaitou.com/2026/08/when-you-feel-like-doing-nothing.html) | 人就是会有这样的时候，什么都不想做，但又没有严重到需要求医问药的程度。自己也觉得这样下去会是个麻烦，可也不知道有什么办法解除。于是就上网跑来问我，而我只能回答说：人就是会有这样的时候。 用我自己为例，看起来一年三百六十五天都在更新，有时候还不止一篇，很勤奋很充实很有韧性的样子。只有我自己最清楚，一年… |
| 2026-08-14 | [Memos: DeepSeek 在我的轻量使用场景下 API 价格涨幅近 4 倍](https://blog.yasking.org/a/1786674900) | 我把过去 30 天的 DeepSeek 账单让 AI 分析，整理出在我的使用场景下的成本结构，缓存命中 96.88%、缓存未命中 2.55%、输出 0.56%，圆整成 … |
| 2026-08-14 | [清风与明月](https://hux.ink/posts/aliveness/) | 最近愈发意识到自己管理能力的欠缺，找来一本《硬核晋升》读。作者 Julie Zhuo 曾任 Facebook 产品设计副总裁，她在序言中提到，自己有一个自我教育的办法：写博客。 我知道我早上起床的时候是谁，但是我想我这一天下来一定是变了很多回了，在未来的某天，我想象着自己回顾自己写的所有帖子，可以好… |
| 2026-08-14 | [Memos: 博客支持 LaTeX 数学公式渲染](https://blog.yasking.org/a/1786673760) | 给博客加了 LaTeX 数学公式支持，方案是 KaTeX + 构建时预渲染为静态 HTML，语法为 $...$ / $$...$$ ，这里记录几个示例。 行内公式 正文里插入公式不用 … |
| 2026-08-14 | [去日你自己吧](https://mobius.blog/25378.html) | 当然，标题是对“Go fuck yourself”的字面直译，实际上这句应该被翻译成“滚远点”。 我很喜欢看英 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-14 | [gemini 3.7 flash 也出来](https://versun.me/blog/tweet-2088054404809454022) | 引用 Introducing Gemini 3.7 Flash : ) - it is fast! - 50% lower price than 3.6 flash (through end of year) - strong intelligence increase in only ~3 wee… |
| 2026-08-14 | [Starryblu：OCBC 还是舍不得丢掉中国用户啊](https://www.meettea.com/digital-refugee/starryblu.html) | 熊猫速汇做的 Starryblu，切到 SGD 充值会给你开一个同名新加坡 OCBC 账户。配合 Wise 可零费用实时转入，也能微信支付宝花、国内 ATM 取现。 |
| 2026-08-13 | [学习周刊-总第276期-2026年第33周](https://wiki.eryajf.net/pages/630ab4/) | 如要阅读全文，点击标题跳转。 学习周刊-总第276期 &#124; Clauge &#124; clipmon &#124; Worklog &#124; Monica &#124; amytis &#124; CodingNS &#124; software_guard &#124; agent-island |
| 2026-08-13 | [科技爱好者周刊（第 408 期）：你需要知道的 AI 缓存知识](http://www.ruanyifeng.com/blog/2026/08/weekly-issue-408.html) | 这里记录每周值得分享的科技内容，周五发布。 本杂志 开源 ，欢迎 投稿 。另有 《谁在招人》 服务，发布程序员招聘信息。合作请 邮件联系 （yifeng.ruan@gmail.com）。 封面图 浙江台州的椒江滨江公共空间生态绿廊，象征涟漪从水面蔓延，涌上岸边，堆积成丘。（ via ） 你需要知道的… |
| 2026-08-13 | [这是我看过&lt;关于LLM是如何工作的](https://versun.me/blog/tweet-2088038009702940699) | 这是我看过 最直观的解释😂 |
| 2026-08-13 | [内测结束了，聊聊 DeepSeek Harness 的使用体验](https://digua.moe/posts/20260813-dsh.html) | > > 我最大的感受是：如果只把 DSH 当成一个 Coding Agent，很容易低估它。 在 X 上看到崔天翼老师发的内测招募后，我带着 ChatLab 报了名，第二天晚上就收到了邀请 |
| 2026-08-13 | [一把开不了门的钥匙](https://tianheg.co/posts/locked-out/) | 我住的地方比较特殊，是工业园区内部的宿舍楼，3 和 4 楼是公司宿舍，5 楼对外出租。我就住 5 楼。 |
| 2026-08-13 | [今日站点异常流量的分析](https://blog.mfwt.top/index.php/archives/1526/) | 人家说，三天不打上房揭瓦，今天倒好，三天不更，就开始有什么东西来揭瓦了。真希望他们能明白，『短暂停更一段时间』的意思是笔者暂时不更新，去打游戏了，不代表我不看站点的运行情况，也不代表我不会分析流... |
| 2026-08-13 | [兜底的代价](https://blog.solazy.me/20260813/) | 兜底到底会把自己兜成什么 |
| 2026-08-13 | [从Vibe Coding到AI Agent：一个喂养系统的完整实践](https://imzlp.com/posts/84248/) | 今年对我来说是个非常意义重大的一年：我娃出生了。在新生的喜悦中，也不免有很多焦虑——总担心不能科学地喂养宝宝、有什么纰漏。在月子中心时，月嫂会比较规律的喂养信息记录——什么时间喝奶、睡了多久，几次大小便，有没有吃AD等，都会记录下来，可以追踪喂养状态。 但她们是通过纸笔记录，不够数字化。 当回家之后… |
| 2026-08-13 | [ds harness 来啦来啦](https://versun.me/blog/tweet-2087888143542530371) | 引用 🧩 DeepSeek Harness v0.1 is now available in Developer Preview! 🔹 We’re opening it up to developers building agent harnesses worldwide and open-sour… |
| 2026-08-13 | [黑群晖断电后无法启动：用 RR 引导无损恢复全记录](https://blog.hoopan.net/851.html) | 黑群晖因突发停电导致引导 U 盘损坏而无法启动，通过 RR 引导（RedPill-Rotor）重做引导盘，无损恢复原系统与数据的完整排查记录。 |
| 2026-08-13 | [Memos: 博客添加了一个 /ping 路由](https://blog.yasking.org/a/1786613642) | 访问： https://blog.yasking.org/ping 国内返回「Served by EdgeOne CDN and sourced from Cloudflare Page.」，海外返回「Served by Cloudflare Pages.」 借助 EdgeOne 和 Cloudfl… |
| 2026-08-13 | [立秋](https://www.jackpu.com/li-qiu-6/) | 今日立秋，自己却拔了牙齿； 本来不在计划之内的，但是看媳妇拔智齿恢复很轻松, 医生的建议可拔可不拔中选择了前者。 做的最正确的决定，就是拔牙前去体验了海底捞79元的午餐套餐，六荤三素，加麻辣的锅底。拔的的时候由于麻药的作用，感觉不到什么，直到几个小时候，才感觉到牙龈的疼痛。 其实拔牙最不好的体验，除… |
| 2026-08-13 | [完成重构了，效果不错，比我预想中的要快很](https://versun.me/blog/tweet-2087819397251690746) | 引用 最近我让 Kimi K3 用 go 语言重构了我的博客系统 Rables，原先是用 Rails 写的，内存占用至少 500 MB 起，重构后，只有 16 MB 左右，不要太爽了 https://github.com/versun/rables 完成重构了，效果不错，比我预想中的要快很多，总共消… |
| 2026-08-13 | [Plants vs. Zombies updated](https://macsourceports.com/game/pvz) | The build of PvZ Portable for Plants vs. Zombies has been updated to version 0.2.1 of the project |
| 2026-08-13 | [Odamex updated](https://macsourceports.com/sourceport/odamex) | The build of Odamex for the DOOM engine series of games has been updated to version 12.3.0 of the project\n\nhttps://macsourceports.com/sourceport/oda… |
| 2026-08-13 | [Ambermoon updated](https://macsourceports.com/game/ambermoon) | The build of Ambermoon.net for Ambermoon has been updated to version v1.13.7 of the project |
| 2026-08-13 | [怎样想决定了是个怎样的人](https://www.hecaitou.com/2026/08/Your-Thought-Is-Your-Mindset.html) | 关于人和人之间的巨大想法差异，有件事让我一直记忆犹新。那是十多年前的事情了，当时我有个创业项目刚刚出了一点点头，看起来非常有希望，就喜滋滋地去找一位前辈讨教，如何才能做大做成。 去到前辈家，他很耐心地听完我的做法和想法，却并没有直接回答我的问题，而是反问我：「你一直都在和我说如何做成，那你有没有考虑… |
| 2026-08-13 | [当一只章鱼在一间全是镜子的房间会如何理解自己？](https://mobius.blog/25371.html) | 本着越不正经的标题聊越正经的话题，今天要开启一个需要花很长时间持续进行的话题。 本来之前还欠了一个“结构化拖延 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-13 | [看来昨晚的 ds 和 grok 还是给到](https://versun.me/blog/tweet-2087706688233332929) | 引用 Old news actually from a bunch of days ago, but crossed that 15M. Enjoy a nice reset everyone. Landing in the next hour or so, go /fast. 看来昨晚的 ds 和… |
| 2026-08-12 | [十九支唢呐](https://godruoyi.com/posts/an-old-man-decides-to-die/) | 五一回家，村里死了一个老头。发现他的时候，尸体已经硬了。没人知道具体是几点走的，可能是凌晨，也可能是半夜 |
| 2026-08-12 | [别拿病历本做宣发](https://blog.solazy.me/20260812/) | 又看到李雪健老师的新闻…… |
| 2026-08-12 | [Kimi 新规：老套餐过期7天就不能续订](https://versun.me/blog/tweet-2087532872433594796) | Kimi 新规：老套餐过期7天就不能续订了。。 |
| 2026-08-12 | [Kimi 最近是不是卡到货了，明显稳定耐](https://versun.me/blog/tweet-2087457668457984009) | Kimi 最近是不是卡到货了，明显稳定耐用了很多 我一个早上9点20开始的 swarm+goal+max 会话，到现在竟然还没断，已经进行到第11轮了 在以前，我还没遇到过能超过8轮的，而且中午也没有被429打断 |
| 2026-08-12 | [如何在控制台解析并按照格式输出 Markdown 内容](https://www.banzhuanriji.com/work/render-markdown-in-terminal/) | 用 Python + ANSI 转义码，在终端里把 Markdown 渲染得有模有样——标题带颜色、代码块带背景、列表带圆点，不依赖任何第三方库，复制就能跑。 |
| 2026-08-12 | [最近碎碎念](https://blog.thetbw.xyz/archives/thoughts-share-260812) | 也是一段时间没有更新博客了，随便写写。 最近我订阅的博客列表也比平时安静了很多，其他中文平台的貌似也没有往日那么活跃了，不知道是不是我最近比较闲，刷的比较多的缘故，不过之前我上班因该刷的更多才是，像是我的世界陷入死寂一样。 距离最近找工作过去了一个多月了，一直没什么好的机会，实在没什么好太多说的，面… |
| 2026-08-12 | [Sequoia Capital合伙人分享：应该追逐热点？还是忽略？](https://wenfeixiang.com/2026/08/what-the-internet-hyped-vs-what-got-built-from-hacker-news/) | 追逐热点？还是忽略它？这一直是创投圈争执的问题。有人喜欢追风口、顺势而为；有人喜欢挖掘水下、坐冷板凳。如果我们 […] |
| 2026-08-12 | [更换驾驶证](https://www.hecaitou.com/2026/08/renewing-my-drivers-license.html) | 我有一本驾驶证，最近快要到期，需要更换，这件事让我头大。 只要一想到服务窗口，想到排队领号，想到备齐文件之类的事情，我就头皮发麻。多年来，我总是想尽一切办法躲避这样的场合，能委托就委托，能代办就代办。坦白说，我不喜欢手续，也不喜欢流程，更不喜欢审批。这些东西在我眼里比大山还要高，接触一下比迷宫还复杂… |
| 2026-08-12 | [社会规则与稻草人](https://ceynri.cn/blog/socialization/) | 立在田里的稻草人，不是为了抓住麻雀，而只是为了让麻雀相信那里有人。 |
| 2026-08-12 | [现在几点？](https://mobius.blog/25356.html) | 遛狗的时候，一个玩滑板车的小男孩突然问我：叔叔现在几点？ 我看了看手机，回答了他。他似乎有些不太确信此刻的时间 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-12 | [想不到 Mojo 还活着，简单回顾了下：](https://versun.me/blog/tweet-2087343369412579461) | 想不到 Mojo 还活着，简单回顾了下： - 2023.5 出道，放话比 Python 快 3.5 万倍 - 2025 年从"语言"转向"推理基础设施"，推出 MAX 推理框架 - 2026.6 公司被高通 39 亿美元收购了。。 - 磨了三年到 1.0，承诺秋天开源编译器 四年半，3.8 亿融资进… |
| 2026-08-12 | [API for agent，有意思](https://versun.me/blog/tweet-2087339309301191003) | API for agent，有意思 [tweet-2077422545142534275-0b04cea4.jpg] |
| 2026-08-11 | [修复 h5player 脚本在巴哈姆特持续注入 CSS](https://blog.bgzo.cc/20260811-fix-h5player-bahamut-fix-width.html) | 很喜欢 h5player 的截图功能，喜欢到了刚需的程度！它强大到自己可以让网页上的一切视频都能截图，甚至做到下载。虽然它如今已经适配 37+ 网站，但它还是不对付我常用的两个看番网站： 1. https//ani.gamer.com.tw/ 2. https//anime1.me 这个问题我 22… |
| 2026-08-11 | [梭罗碥石刻：不知缘由裂成两半](https://macin.org/2026/08/11/suo-luo-bian/) | 阅读全文 → 这周去了一趟（弗罗里）达州渠县。 |
| 2026-08-11 | [DIVING INTO HK](https://re.karlbaey.top/articles/rocky-road/diving-into-hk/) | 多用了点 emoji 表达情绪。🤪图片比较多，记得连着 Wi-Fi 看。快说谢谢流量侠。 距离上一回去 HK，已经有十个 … |
| 2026-08-11 | [简化与收敛](https://z.arlmy.me/posts/ZArlmyMe/Decrease_20260811/) | 「简化与收敛。」 |
| 2026-08-11 | [《让她降落》](https://blog.solazy.me/20260811/) | 今天聊聊音乐 |
| 2026-08-11 | [批量修改主机名后 Java 应用抛 UnknownHostException 的排查与处置](https://199604.com/3643) | 批量修改主机名后 Java 应用抛 UnknownHostException 的排查与处置 记录时间：2026 […] |
| 2026-08-11 | [互联网来到我身边以前](https://www.tortorse.com/archives/internet-before-it-came-to-me/) | 九十年代的电脑、游戏机和游戏杂志 |
| 2026-08-11 | [How I Use Hermes](https://www.bboy.app/2026/08/11/how-i-use-hermes/) | Introduction I came across the Hermes Agent project around the end of last year and gave it a try. I’ve been using it for over half a year now, and I… |
| 2026-08-11 | [我是怎么用 Hermes 的](https://www.bboy.app/2026/08/11/%E6%88%91%E6%98%AF%E6%80%8E%E4%B9%88%E7%94%A8-hermes-%E7%9A%84/) | 简介 大概去年年末看到 Hermes Agent 这个项目，试了下。用了大半年，现在离不开了。今天聊聊我的用法。 Hermes 是什么，我是怎么装的 简单说，Hermes 是一个跑在本地的 AI 助手 CLI。你可以通过 Telegram 跟它聊天，它背后调大模型，然后直接操作你的电脑——读文件、写… |
| 2026-08-11 | [Whey Protein and Creatine](https://www.bboy.app/2026/08/11/whey-protein-and-creatine/) | Introduction I’m 30, an ops engineer, sitting in front of a computer all day. I won’t talk about my height, but my weight — you probably won’t believe… |
| 2026-08-11 | [蛋白粉和肌酸](https://www.bboy.app/2026/08/11/%E8%9B%8B%E7%99%BD%E7%B2%89%E5%92%8C%E8%82%8C%E9%85%B8/) | 简介 我 30 岁，运维，天天坐电脑前面。身高就不说了，体重说出来你可能不信：45kg。 对，你没看错，一个成年男人，45kg。瘦了二十多年，从来没进过健身房，全是自己在家练。最近又把这事捡起来了，顺手买了蛋白粉和肌酸。现在用支架一次能做 50 个俯卧撑了，离大佬差得远，但对我来说已经是人生巅峰。写… |
| 2026-08-11 | [20260811的胡言乱语](https://www.bboy.app/2026/08/11/20260811%E7%9A%84%E8%83%A1%E8%A8%80%E4%B9%B1%E8%AF%AD/) | 简介 欢迎关注我的频道，不时发送垃圾消息 https://t.me/bboyapp 或者关注我的 twitter https://twitter.com/bboysoulcn |
| 2026-08-11 | [Random Thoughts - 20260811](https://www.bboy.app/2026/08/11/random-thoughts-20260811/) | Introduction Welcome to follow my channel, where I occasionally share random messages https://t.me/bboyapp Or follow me on Twitter https://twitter.com… |
| 2026-08-11 | [在南方](https://z.arlmy.me/posts/ZArlmyMe/South_20260811/) | 「在南方。」 |
| 2026-08-11 | [好久不见](https://ameow.xyz/archives/blog-cdn-update) | 最近几个月都感觉没什么内容更新，所以就没有写周刊。 今天翻邮件的时候发现七牛云的 CDN SSL 证书过期了，导致博客的图片其实挂了差不多半个月。于是花了一个早上把数据迁移到腾讯云，成本差不多，证书可以自动化管理，年纪大了就是不爱折腾。迁移过程一路顺利没有踩太多坑，翻了下博客的照片都可以正常访问了，… |
| 2026-08-11 | [SpotAsk：不是所有的问题，都需要打开 ChatGPT](https://shiquda.link/spotask-not-every-question-needs-chatgpt/) | SpotAsk：不是所有的问题，都需要打开 ChatGPT 我为什么想做 SpotAsk 最近我开始在 macOS 上生活，顺手做了自己的第一款 macOS 桌面应用：SpotAsk。 起因很普通。我打开 ChatGPT，很多时候并不是要处理什么复杂任务。更多时候，只是想弄明白一个概念、翻译一段话、… |
| 2026-08-11 | [Grafana cluster变量出现Kafka垃圾值的排查与清理](https://199604.com/3641) | Grafana cluster变量出现Kafka垃圾值的排查与清理 记录时间：2026-08-08 环境：RK […] |
| 2026-08-11 | [清华大学 TUNA 镜像站宣布：正式移除 Anaconda、OpenWrt、Flutter、GitLab EE 软件镜像](https://blog.renfei.net/posts/1626402130325676144) | 清华大学 TUNA 镜像站因存储资源受限，正式移除 Anaconda、OpenWrt、Flutter 和 GitLab EE 软件镜像，原有访问将跳转到教育网联合镜像站或上游。 |
| 2026-08-11 | [不建群的人](https://www.hecaitou.com/2026/08/The-Non-Group-Person.html) | 最近看到两条读者提问，彼此看起来差别很大，但在我眼里完全是一回事： 1、你为什么不建一个读书群？ 2、在陌生的城市里工作，总感到孤独怎么办？ 那就去参加一个读书群好了---如果我这么回答是不是有点冷血，有点不道德？ 熟悉我的读者都知道，我不大加群，尤其是大群，尤其是学习群、打卡群、社交群。因为这件事… |
| 2026-08-11 | [Pi 打败了Oh My Pi 🤣](https://versun.me/blog/tweet-2086992544861507602) | Pi 打败了Oh My Pi 🤣 [tweet-2086814491920974069-7228c7aa.jpg] |
| 2026-08-11 | [污染源](https://mobius.blog/25346.html) | 我从小得到老师最多的评价，是一句被我视为“褒奖”的话：十处打锣九处都有你。 倒不是我这个人好热闹，而是很多事情 […] —— 感谢订阅 莫比乌斯 ，如你有任何疑问、观点交流，请前往 创作者频道 ，或 私信 联系。 |
| 2026-08-11 | [这个有意思，就是安装麻烦了些，建议简化下](https://versun.me/blog/tweet-2086985748298051749) | 这个有意思，就是安装麻烦了些，建议简化下安装方式 [tweet-2086846424051044750-fc837d1a.mp4] |
| 2026-08-11 | [青岛威海自驾游（2026）](https://krya.com/post/qingdaoweihai/) | 这次一共五个人：我们一家三口，加上媳妇的闺蜜和她妈妈。四个大人带一个小孩，长途开车其实并不拥挤，路上反而多了不少聊天的话题。 图片拍摄的设备有索尼a7M3（50mm定焦镜头），以及前不久购入了大疆Osmo Pocket 4，或者iPhone直出。 从成都出发，耗时14天，总行程4902公里，加油17… |
| 2026-08-11 | [最近一个月有玩过 Blender MCP](https://versun.me/blog/tweet-2086978334110658688) | 最近一个月有玩过 Blender MCP 的要注意了，有一个供应链投毒事件 CVE-2026-66004，建议尽快排查一下 https://www.kimi.com/share/19fee49f-65a2-84f3-8000-0000d35140db [tweet-20869783341106586… |

## Vibe Coding

### GitHub copilot

Make sure to keep `.github/instructions` folder clean and simplest, or it may make context understanding and code generation worse, such as, `agent`, `instructions` and `prompts` should not conflict each other.

The **priority** of them should be like this:

Personal Instructions > Repository Instructions > Agent > Prompts > Your messages.

And get the template for GitHub Copilot from https://github.com/doggy8088/github-copilot-configs/tree/main/.github


## Common Steps:

- Read the documentation in `docs/memories` to understand the project structure, design and tech stack.
- Check the features in `docs/implementation-plans` to see if there are any questions or clarifications needed.
- Plan the simplest implementation steps in `docs/implementation-plans`, then list it append to the existing plans, and make every step clear enough for anyone to pick up and execute, and also make sure to include the verification steps for each implementation step.
- Then start implementation based on the plan step by step, and you should make sure keep these things:
  - Only when the verification steps are passed, you can move on to the next step, otherwise you should fix the problems until the verification steps are passed.
  - Link the related files, functions, or types in the codebase as much as possible, and also link the related plans if there are any. 
  - Make sure to record progress and what you have done in every step in the plan and things in other files.
  - Update the documents in `docs/memories` if there are any design changes or tech stack changes during the implementation.


## Roadmap

I use obdisian to manage roadmap of this project, and I will update it here when I have a clear plan for the next steps.

- [x] Add basic structure and files[^template-inspired].
- [x] Add Vibe coding support [^vibe-coding-inspired].

[^template-inspired]: Template inspired by https://github.com/kelseyhightower/nocode, https://github.com/othneildrew/Best-README-Template

[^vibe-coding-inspired]: https://github.com/tukuaiai/vibe-coding-cn

See the [open issues](https://github.com/bgzo-sandbox/make-vxna-great-again/issues) for a full list of proposed features (and known issues).
-->

## Contributing

Any contributions made are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat(module):add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Top contributors:

<a href="https://github.com/bgzo-sandbox/make-vxna-great-again/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bgzo-sandbox/make-vxna-great-again" alt="contrib.rocks image" />
</a>

## License

All code is licensed under the AGPL-3.0 license. See `LICENSE` for more information.
